import os
import requests
from datetime import datetime, timezone
from helpers import sign_payload

def get_iso_timestamp():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

def submit():
    action_run_link = os.getenv("RUN_ID_URL")
    if not action_run_link:
        print("Action run link not found")
        exit(1)

    signing_secret = os.getenv("SIGNING_SECRET")
    if not signing_secret:
        print("SIGNING_SECRET not found")
        exit(1)

    payload = {
        "name": "David Kimani",
        "email": "dmmkimani@gmail.com",
        "resume_link": "https://drive.google.com/file/d/14Ugg9bGTwIU2a1D_qXVFXu9o_o3N0p1P/view?usp=sharing",
        "repository_link": os.getenv("REPO_URL", "https://github.com/dmmkimani/b12"),
        "action_run_link": action_run_link,
        "timestamp": get_iso_timestamp()
    }

    payload_str, signature = sign_payload(payload, signing_secret)

    headers = {
        "Content-Type": "application/json",
        "X-Signature-256": f"sha256={signature}"
    }

    url = "https://b12.io/apply/submission"
    try:
        response = requests.post(url, data=payload_str, headers=headers)
        if response.status_code == 200:
            receipt = response.json().get("receipt")
            print(f"Receipt: {receipt}")
        else:
            print(f"Request failed with status code {response.status_code}: {response.text}")
            exit(1)
    except Exception as e:
        print(f"An error occurred during the request: {e}")
        exit(1)

if __name__ == "__main__":
    submit()
