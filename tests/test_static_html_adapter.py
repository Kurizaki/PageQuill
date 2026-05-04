from datetime import date

from pagequill.adapters.static_html import StaticHtmlAdapter
from pagequill.core.models import BlogPost


def make_post() -> BlogPost:
    return BlogPost(
        title="Hello",
        slug="hello",
        date=date(2026, 1, 1),
        description="A first post",
        tags=["intro", "updates"],
        markdown="# Hello",
        status="published",
    )


def test_static_html_adapter_uses_static_blog_paths() -> None:
    adapter = StaticHtmlAdapter()

    assert adapter.get_post_path(make_post()) == "blog/posts/2026-01-01-hello.html"
    assert adapter.get_posts_data_path() == "blog/data/posts.json"


def test_static_html_adapter_renders_post_html() -> None:
    html = StaticHtmlAdapter().render_post(make_post(), "<h2>Hello</h2>")

    assert "<title>Hello</title>" in html
    assert '<meta name="description" content="A first post">' in html
    assert "<time>2026-01-01</time>" in html
    assert "<h2>Hello</h2>" in html
    assert "intro, updates" in html


def test_static_html_adapter_creates_post_metadata() -> None:
    assert StaticHtmlAdapter().create_post_metadata(make_post()) == {
        "title": "Hello",
        "slug": "hello",
        "date": "2026-01-01",
        "description": "A first post",
        "tags": ["intro", "updates"],
        "url": "./posts/2026-01-01-hello.html",
    }
