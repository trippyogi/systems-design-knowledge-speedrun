#!/usr/bin/env python3
"""Pick a random systems design kata."""
import random

KATAS = [
    "URL shortener",
    "Pastebin",
    "Rate limiter",
    "Notification service",
    "News feed",
    "Chat system",
    "File storage",
    "Search autocomplete",
    "Webhook delivery platform",
    "Ticket booking / inventory reservation",
    "Metrics ingestion pipeline",
    "Multi-tenant SaaS API platform",
    "Collaborative document editing",
]

print(random.choice(KATAS))
