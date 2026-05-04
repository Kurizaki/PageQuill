"""Slug generation utilities."""

import re


def slugify(value: str) -> str:
    """Convert text into a URL-friendly slug."""
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "post"

