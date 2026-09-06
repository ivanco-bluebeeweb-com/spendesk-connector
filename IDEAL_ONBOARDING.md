# Spendesk Connector — Ideal Onboarding Flow

1. **Portal Navigation:** User logs into Spendesk at `app.spendesk.com`.
2. **Token Generation:** Navigates to Settings > Advanced Settings > Your API Keys and generates a new API token.
3. **Imperal Configuration:** Pastes the token into the Spendesk sidebar form in Imperal Cloud.
4. **Verification & Storage:** Connector tests `GET /v1/me`, confirms connectivity, securely stores credentials, and activates the connection.
