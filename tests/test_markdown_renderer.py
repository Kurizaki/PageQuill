from pagequill.infrastructure.markdown.renderer import MarkdownRenderer


def test_markdown_renderer_renders_heading() -> None:
    assert "<h1>Hello</h1>" in MarkdownRenderer().render("# Hello")

