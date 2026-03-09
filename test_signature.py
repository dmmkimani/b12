import os
import pytest
from helpers import sign_payload

def test_signature():
    signing_secret = os.getenv("SIGNING_SECRET")
    if not signing_secret:
        pytest.fail("SIGNING_SECRET is not set")

    payload = {
        "timestamp": "2026-01-06T16:59:37.571Z",
        "email": "you@example.com",
        "name": "Your name",
        "action_run_link": "https://link-to-github-or-another-forge.example.com/your/repository/actions/runs/run_id",
        "resume_link": "https://pdf-or-html-or-linkedin.example.com",
        "repository_link": "https://link-to-github-or-other-forge.example.com/your/repository"
    }

    _, signature = sign_payload(payload, signing_secret)
    
    assert signature == "c5db257a56e3c258ec1162459c9a295280871269f4cf70146d2c9f1b52671d45"
