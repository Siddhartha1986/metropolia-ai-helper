"""
Metropolia Nursing AI Helper - Flask Web Application

This demo application showcases:
1. A Finnish–English nursing vocabulary helper:
      - Searches nursing terms in FI/EN
      - Provides bilingual explanations
      - Includes clinical examples

2. A HuggingFace-based text summarizer:
      - Summarizes nursing notes or study material
      - Uses facebook/bart-large-cnn via HF Inference API
      - Demonstrates secure API token usage via environment variable

This project is submitted as part of the
Metropolia AI Student Assistant application.
Author: Siddhartha Lama
"""

# ============================================================
# Imports
# ============================================================
import os
import requests

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
)

# Import local nursing terms database
from nursing_terms import NURSING_TERMS

# Load variables from .env file
from dotenv import load_dotenv
load_dotenv()   

# Create Flask application
app = Flask(__name__)


# ============================================================
# Nursing Term Search Helper
# ============================================================

def find_nursing_term(query: str):
    """
    Try to find a matching nursing term based on Finnish or English keywords.
    Returns a dictionary with explanations and examples, or None.
    """
    q = query.lower().strip()

    for term in NURSING_TERMS:
        # Check Finnish variants
        for fi in term["fi_terms"]:
            if fi in q:
                return term

        # Check English variants
        for en in term["en_terms"]:
            if en in q:
                return term

    return None  # No match found


# ============================================================
# Hugging Face Summarizer Helper
# ============================================================

# HF Inference API endpoint (router handles model loading automatically)
HF_SUMMARY_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"


def summarize_with_hf(text: str) -> str:
    """
    Calls the HuggingFace Inference API to summarize text.
    Requires HF_API_TOKEN to be set as an environment variable.
    Returns summary text or an error message.
    """
    token = os.getenv("HF_API_TOKEN")

    if not token:
        return "HF_API_TOKEN is not set. Please configure your environment variable."

    # Authorization header
    headers = {"Authorization": f"Bearer {token}"}

    # Request payload with length limits
    payload = {
        "inputs": text,
        "parameters": {
            "max_length": 200,
            "min_length": 30,
        },
    }

    try:
        resp = requests.post(HF_SUMMARY_URL, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()  # Raises error for HTTP codes

        data = resp.json()

        # Normal summarization response
        if isinstance(data, list) and data and "summary_text" in data[0]:
            return data[0]["summary_text"]

        # Model still loading or other HF error
        if isinstance(data, dict) and "error" in data:
            return f"Hugging Face API error: {data['error']}"

        return f"Unexpected response: {data}"

    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"


# ============================================================
# Routes
# ============================================================

@app.route("/")
def index():
    """Home page with navigation to tools."""
    return render_template("index.html")


# ---------------------------
# Nursing Helper Page
# ---------------------------
@app.route("/nurse-helper", methods=["GET", "POST"])
def nurse_helper():
    """Search Finnish/English nursing terms and display explanations."""
    result = None
    query = ""

    if request.method == "POST":
        query = request.form.get("query", "")
        if query:
            term = find_nursing_term(query)
            result = term if term else "not_found"

    return render_template(
        "nurse_helper.html",
        query=query,
        result=result,
        terms=NURSING_TERMS
    )


# ---------------------------
# Summarizer Page
# ---------------------------

MAX_CHARS = 1500  # Max allowed text length for summarization


@app.route("/summarize", methods=["GET", "POST"])
def summarize():
    """
    Summarizes user-provided nursing text using HuggingFace API.
    Shows errors for too-long text or HF API issues.
    """
    original = ""
    summary = None
    error = None

    if request.method == "POST":
        original = request.form.get("text", "").strip()

        # Enforce length limit
        if len(original) > MAX_CHARS:
            error = (
                f"Text is too long ({len(original)} characters). "
                f"Please shorten it below {MAX_CHARS} characters."
            )
        elif original:
            summary = summarize_with_hf(original)

            # Detect various error messages and separate them
            if summary.startswith(("HF_API_TOKEN is not set",
                                   "Hugging Face API error",
                                   "Request error")):
                error = summary
                summary = None

    return render_template(
        "summarize.html",
        original=original,
        summary=summary,
        error=error,
    )


# ============================================================
# End of app
# ============================================================

