"""Markdown rendering infrastructure."""

from markdown_it import MarkdownIt


class MarkdownRenderer:
    """Render markdown to HTML."""

    def __init__(self) -> None:
        self._renderer = MarkdownIt()

    def render(self, markdown: str) -> str:
        return self._renderer.render(markdown)

