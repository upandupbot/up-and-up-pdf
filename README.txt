Up & Up - Pipefy PDF Generator

Overview
This is a small FastAPI service that generates branded PDF briefs from Pipefy cards,
then attaches the PDF back to the card.

How it works
1. An API request is made with a Pipefy card ID (or a Pipefy webhook payload).
2. The card data is fetched from Pipefy via GraphQL.
3. Fields are normalized and formatted.
4. The PDF is generated using a predefined layout.
5. The PDF is returned as a binary response and attached to the card.

Requirements
- Python 3.x
- Pip packages from requirements.txt

Environment variables
- PIPEFY_ACCESS_TOKEN (required) API token for Pipefy
- PAPERTRAIL_TOKEN (optional) token for Papertrail HTTP logging

Local setup
1. Create and activate a virtual environment
   - python -m venv venv
   - .\venv\Scripts\Activate.ps1
2. Install dependencies
   - pip install -r requirements.txt
3. Create a .env file and set required variables
   - PIPEFY_ACCESS_TOKEN=your_token_here
   - PAPERTRAIL_TOKEN=optional_token_here
4. Run the API
   - uvicorn main:app --host 0.0.0.0 --port 8000

API endpoints
- GET /health
- POST /pipefy/generate-pdf
  - Accepts either {"card_id": 123} or a Pipefy webhook payload:
    {"data": {"card": {"id": 123}}}

Project structure
- main.py: FastAPI app and API endpoint
- pipefy_helpers.py: Pipefy GraphQL requests, uploads, and attachments
- pdf_generate.py: Builds the PDF, applies branding, renders sections
- layout.py: PDF layout (sections, field order, labels)
- functions.py: Formatting helpers (tables, bullets, attachments, values)
- up_slip_wide_spacing.png: Header logo used at the top of the PDF
- source-sans-pro.regular.ttf
- source-sans-pro.bold.ttf
  Source Sans Pro fonts used by the PDF

PDF details
- Format: A4 (portrait)
- Font: Source Sans Pro
- Header: Full-width logo
- Output: Returned as bytes

Publish to GitHub (step-by-step)
1. Create a new repository on GitHub (empty, no README or .gitignore).
2. In this project folder, initialize git:
   - git init
3. Add files and commit:
   - git add .
   - git commit -m "Initial commit"
4. Set the branch name to main:
   - git branch -M main
5. Add the GitHub remote (replace with your repo URL):
   - git remote add origin https://github.com/your-user/your-repo.git
6. Push:
   - git push -u origin main

Notes
- .env is ignored by .gitignore and will not be committed.
