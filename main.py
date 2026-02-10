import os
import logging
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from pipefy_helpers import fetch_card, upload_pdf_to_card
from functions import safe_filename
from pdf_generate import build_pdf
from fastapi.responses import Response

load_dotenv()

# ---------------------------------------------------------------------------
#  Papertrail HTTP logging
# ---------------------------------------------------------------------------
PAPERTRAIL_TOKEN = os.getenv("PAPERTRAIL_TOKEN")
PAPERTRAIL_URL = "https://logs.collector.solarwinds.com/v1/log"

logger = logging.getLogger("up-and-up-pdf")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def log_to_papertrail(card_id, message):
    if not PAPERTRAIL_TOKEN:
        return
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    data = f"up-and-up-pdf: {stamp}, cardid {card_id}: {message}"
    try:
        requests.post(
            PAPERTRAIL_URL,
            auth=("", PAPERTRAIL_TOKEN),
            headers={"Content-Type": "text/plain; charset=utf-8"},
            data=data.encode("utf-8"),
            timeout=5,
        )
    except Exception as e:
        logger.warning(f"Papertrail logging failed: {e}")


# ---------------------------------------------------------------------------
#  FastAPI app
# ---------------------------------------------------------------------------
app = FastAPI()


class generate_pdfRequest(BaseModel):
    card_id: int


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/pipefy/generate-pdf")
async def generate_pdf_endpoint(request: Request):
    body = await request.json()

    # Support both direct {"card_id": 123} and Pipefy webhook {"data": {"card": {"id": 123}}}
    if "data" in body and "card" in body["data"]:
        card_id = int(body["data"]["card"]["id"])
    elif "card_id" in body:
        card_id = int(body["card_id"])
    else:
        raise HTTPException(status_code=400, detail="Could not extract card_id from payload")
    logger.info(f"Received PDF generation request for card_id={card_id}")
    log_to_papertrail(card_id, "PDF generation request received")

    try:
        card = fetch_card(card_id)
        title = card.get("title") or f"card_{card_id}"
        filename = f"Slipstream_Brief_{safe_filename(title)}.pdf"

        pdf_bytes = build_pdf(card_id)
        logger.info(f"PDF built for card_id={card_id}, size={len(pdf_bytes)} bytes")
        log_to_papertrail(card_id, f"PDF built, size={len(pdf_bytes)} bytes")

        result = upload_pdf_to_card(card_id, pdf_bytes, filename)
        logger.info(f"PDF uploaded and attached to card_id={card_id}")
        log_to_papertrail(card_id, "PDF uploaded and attached to card")

        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={"Content-Disposition": f'inline; filename="{filename}"'},
            status_code=200,
        )
    except ValueError as e:
        logger.error(f"Card not found: card_id={card_id} — {e}")
        log_to_papertrail(card_id, f"ERROR Card not found: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.exception(f"Failed to generate PDF for card_id={card_id}")
        log_to_papertrail(card_id, f"ERROR Failed to generate PDF: {e}")
        raise HTTPException(status_code=500, detail=str(e))
