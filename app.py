"""Extension declaration, capabilities, health check for Spendesk Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "spendesk-connector",
    version="0.1.0",
    display_name="Spendesk",
    icon="icon.svg",
    capabilities=["spendesk:manage"],
    description="Official Imperal connector for Spendesk (C29. Expense Management & Corporate Cards). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("spendesk_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} Spendesk connection(s) configured." if count else "Not connected yet."
    }
