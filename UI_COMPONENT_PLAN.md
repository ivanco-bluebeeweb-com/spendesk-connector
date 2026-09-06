# Spendesk Connector — UI Component Plan

## Left Sidebar Design (`spendesk_sidebar`)
- **Root Container:** `ui.Stack(direction="v", gap=3, align="stretch")`
- **Header:** Title "Spendesk" + explanatory subtitle.
- **Connection Form:**
  - Connection label input (`ui.Input(param_name="label", placeholder="e.g. Acme Spendesk")`)
  - API Token input (`ui.Input(param_name="api_key", placeholder="Enter Spendesk API Token")`)
  - Submit button: `ui.Button("Connect Spendesk", variant="primary", size="sm")`
- **Help Modal:** `ui.Modal` detailing exact steps to generate the API token in Spendesk.
- **Compliance:** Full compliance with `UI_INTERFACE_STANDARD.md` (no duplicate helper texts, full-width layout).
