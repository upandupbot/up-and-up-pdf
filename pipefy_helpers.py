import requests
import os
from urllib.parse import unquote, urlparse

org_id = 301595318

def pipefy_graphql(query: str, variables: dict | None = None) -> dict:

    PIPEFY_API_URL = "https://api.pipefy.com/graphql"
    PIPEFY_ACCESS_TOKEN = os.getenv("PIPEFY_ACCESS_TOKEN")
    if not PIPEFY_ACCESS_TOKEN:
        raise RuntimeError("PIPEFY_ACCESS_TOKEN is not set")

    headers = {
        "Authorization": f"Bearer {PIPEFY_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {"query": query}
    if variables:
        payload["variables"] = variables

    response = requests.post(PIPEFY_API_URL, json=payload, headers=headers, timeout=30)
    if response.status_code != 200:
        raise RuntimeError(f"Pipefy request failed: {response.status_code}: {response.text}")

    data = response.json()
    if data.get("errors"):
        raise RuntimeError(f"Pipefy GraphQL errors: {data['errors']}")

    return data["data"]

def fetch_card(card_id: int) -> dict:
    """Retrieve Card details from Pipefy using card ID."""
    query = """
    query($cardId: ID!) {
      card(id: $cardId) {
        id
        title
        fields {
          name
          field { id }
          value
        }
      }
    }
    """

    data = pipefy_graphql(query, {"cardId": str(card_id)})

    card = data.get("card")
    if not card:
        raise ValueError(f"Card ID {card_id} not found")

    return card

def create_presigned_upload_url(org_id: int, filename: str) -> str:
    q = """
    mutation ($orgId: ID!, $fileName: String!) {
      createPresignedUrl(input: { organizationId: $orgId, fileName: $fileName }) {
        url
      }
    }
    """
    data = pipefy_graphql(q, {"orgId": str(org_id), "fileName": filename})
    url = (data or {}).get("createPresignedUrl", {}).get("url")

    if not url:
        raise RuntimeError(f"Failed to create presigned URL. Response: {data}")

    return url

def upload_bytes_to_presigned_url(url: str, file_bytes: bytes) -> None:
    """
    Uploads raw bytes to a Pipefy presigned S3 URL.
    Raises if upload fails.
    """
    headers = {
        "Content-Type": "application/pdf"
    }

    resp = requests.put(url, data=file_bytes, headers=headers)

    if resp.status_code not in (200, 201):
        raise RuntimeError(
            f"Failed to upload file to presigned URL "
            f"(status={resp.status_code}, body={resp.text})"
        )
    
def _s3_key_from_presigned_url(presigned_url: str) -> str:
    parsed = urlparse(presigned_url)

    # decode %20 etc.
    key = unquote(parsed.path.lstrip("/"))

    if not key:
        raise RuntimeError(f"Could not extract S3 key from presigned URL: {presigned_url}")

    return key

def attach_uploaded_file_to_card(card_id: int, presigned_url: str) -> bool:
    q = """
        mutation UpdateAttach($cardId: ID!, $fieldId: ID!, $newValue: [UndefinedInput!]!) {
        updateCardField(input: { card_id: $cardId, field_id: $fieldId, new_value: $newValue }) {
            success
        }
        }
    """
    s3_key = _s3_key_from_presigned_url(presigned_url)

    data = pipefy_graphql(q, {
        "cardId": str(card_id),
        "fieldId": "brief_attached",
        "newValue": [s3_key],
    })

    ok = (data or {}).get("updateCardField", {}).get("success")
    if ok is not True:
        raise RuntimeError(f"Failed to attach file to card. Response: {data}")

    return True

def upload_pdf_to_card(card_id: int, pdf_bytes: bytes, filename: str) -> dict:

    presigned_url = create_presigned_upload_url(org_id, filename)
    upload_bytes_to_presigned_url(presigned_url, pdf_bytes)
    attach_uploaded_file_to_card(card_id, presigned_url)

    return {
        "card_id": str(card_id),
        "filename": filename,
        "status": "attached"
    }

