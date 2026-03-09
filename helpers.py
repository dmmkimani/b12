import json
import hmac
import hashlib
from typing import Any

def sign_payload(payload: dict[str, Any], secret: str) -> tuple[str, str]:
    payload_str = json.dumps(payload, separators=(",", ":"), sort_keys=True)
    payload_bytes = payload_str.encode("utf-8")

    secret_bytes = secret.strip().encode("utf-8")
    signature = hmac.new(
        key=secret_bytes, 
        msg=payload_bytes, 
        digestmod=hashlib.sha256
    ).hexdigest()

    return payload_str, signature
    