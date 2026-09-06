# Spendesk Connector — Discovery & API Specifications

## Vendor Details
- **Product:** Spendesk Corporate Spend Management
- **Documentation:** `https://developer.spendesk.com`
- **OpenAPI / Specification:** Spendesk Public REST API v1
- **Base Endpoint:** `https://public-api.spendesk.com/v1`

## Core Resources and Schemas
1. **Expenses / Payables:** Purchase requests, invoices, and card transactions.
2. **Cards:** Virtual single-use/recurring cards and physical company debit cards.
3. **Reports / Settlements:** Bundled expense claims awaiting review or settlement.
4. **Policies:** Spend approval limits, policy rules, and category allowances.
5. **Merchants:** Vendor profile, tax IDs, and MCC code categorization.
6. **Reimbursements:** Wallet disbursements and direct bank transfers.

## Security & Reliability Standards
- Automatic header redaction for Bearer tokens.
- Rate limit extraction from `Retry-After` header on HTTP 429.
- Full multi-tenant isolation via connection registry stored securely in context secrets.
