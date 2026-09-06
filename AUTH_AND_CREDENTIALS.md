# Spendesk Connector — Authentication & Credentials

## Authentication Protocol
- **Method:** API Bearer Token
- **Header:** `Authorization: Bearer <api_token>`
- **Default Host:** `https://public-api.spendesk.com/v1`

## Security Compliance (Standards B1–B10)
- **B1-B5:** Secrets stored exclusively in encrypted context storage under `spendesk_connections`.
- **B7/B9:** Connection record schema includes unique `id`, user `label`, `masked_key`, and active status.
- **B8:** Bearer tokens are masked in logs and sanitised in all client error returns.
- **B10:** Verification endpoint `GET /v1/me` tests token validity before persisting credentials.
