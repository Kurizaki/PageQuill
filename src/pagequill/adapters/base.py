"""Adapter contracts."""

from typing import Protocol

from pagequill.core.models import BlogPost


class BlogAdapter(Protocol):
    """Protocol for static blog backends."""

    def render_post(self, post: BlogPost, html_content: str) -> str:
        """Render a blog post to its published representation."""
