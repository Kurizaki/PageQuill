"""Static HTML blog adapter."""

from pagequill.core.models import BlogPost
from pagequill.infrastructure.html.template_renderer import render_template


class StaticHtmlAdapter:
    """Render posts for the bundled static HTML blog."""

    def get_post_path(self, post: BlogPost) -> str:
        return f"blog/posts/{post.date}-{post.slug}.html"

    def get_posts_data_path(self) -> str:
        return "blog/data/posts.json"

    def render_post(self, post: BlogPost, html_content: str) -> str:
        return render_template(
            "static_html/post.html",
            {
                "title": post.title,
                "date": post.date.isoformat(),
                "description": post.description,
                "content": html_content,
                "tags": post.tags,
            },
        )

    def create_post_metadata(self, post: BlogPost) -> dict:
        return {
            "title": post.title,
            "slug": post.slug,
            "date": post.date.isoformat(),
            "description": post.description,
            "tags": post.tags,
            "url": f"./posts/{post.date}-{post.slug}.html",
        }
