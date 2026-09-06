# Spendesk Connector — Preparation

## Product Scope
Build a comprehensive Imperal connector for **Spendesk** under category **C29. Expense Management & Corporate Cards**. The integration interacts directly with the official **Spendesk Public REST API v1** (`https://public-api.spendesk.com/v1`), providing full visibility and control over corporate payment cards, out-of-pocket expenses, payables, settlements, spend policies, merchant categorization, employee reimbursements, and automated compliance auditing.

## Official API Specifications
- **API Architecture:** RESTful JSON API
- **Base URL:** `https://public-api.spendesk.com/v1`
- **Core Endpoints:**
  - `GET /v1/me` — verify token privileges and company context
  - `GET /v1/payables` — list payables and expense entries
  - `GET /v1/payables/{id}` — detailed payable transaction
  - `GET /v1/cards` — virtual and physical spend cards
  - `GET /v1/settlements` — expense reports and settlements
  - `GET /v1/policies` — spend control limits and approval workflows
  - `GET /v1/merchants` — merchant categorization
  - `GET /v1/wallet-loads` / `GET /v1/wallet-summary` — company wallet and reimbursements
- **Authentication Model:** Bearer Token via `Authorization: Bearer <api_token>`
- **Mandatory Requirements:**
  - Strict error classification: HTTP 429 rate limits with Retry-After extraction, HTTP 401/403 differentiation (Standard B8/B10).
  - Sanitization of Bearer tokens in error traces and diagnostic payloads (Standard B8).
  - Multi-tenant connection tracking and isolation via `connection_id` (Standard B9).

## Delivery Gates
1. [x] Official API discovery completed with Spendesk Public API v1 specifications.
2. [x] Core resource endpoints and Bearer auth verified.
3. [x] Five mandatory specification documents authored.
4. [x] Client implemented with B8-B10 compliance, secret redaction, and 429/401 classification.
5. [x] Panel sidebar implemented conforming to UI_INTERFACE_STANDARD.md.
6. [x] Verification of functions, imports, and type hints passed.
7. [x] Deployment to Imperal platform completed.
8. [x] Pricing configured per PRICING_POLICY.md.
