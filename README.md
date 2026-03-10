# B12 Application Submission Task

This repository implements the B12 application submission task: submitting a JSON payload via a GitHub Action, signed with HMAC-SHA256, to the B12 endpoint.

## Approach

- GitHub Action is triggered manually via the repository Actions tab, allowing submissions to be made on demand.
- The workflow executes `submit.py`.
- The script:
    - generates an ISO-8601 timestamp
    - canonicalizes the JSON payload (alphabetical keys, compact separators) to ensure consistent HMAC signatures
    - computes an HMAC-SHA256 signature and includes it in the header to authenticate the submission
    - POSTs the payload to the B12 endpoint
    - prints the returned receipt from the endpoint to confirm successful submission

## Testing

`test_signature.py` validates the signing logic against the spec, ensuring payload correctness and reproducibility between local and CI runs.

Tests can be run locally to confirm CI behavior matches the canonical HMAC signature using:

###### On Windows
```
set SIGNING_SECRET=[SECRET] & pytest
```

## Files

- `submit.py`: Python script that constructs the payload, signs it, and submits it
- `helpers.py`: Shared signing utilities
- `test_signature.py`: Test validating signature logic
- `.github/workflows/submit.yml`: GitHub Action workflow definition

## Running Locally

###### On Windows
```
pip install -r requirements.txt
set RUN_ID_URL="" & set SIGNING_SECRET=[SECRET] & python submit.py
```
