"""HTML template rendering."""

from importlib.resources import files
from typing import Any


def render_template(template_path: str, context: dict[str, Any]) -> str:
    """Render a bundled template with simple {{ name }} placeholders."""
    template = (
        files("pagequill.templates")
        .joinpath(template_path)
        .read_text(encoding="utf-8")
    )

    rendered = template
    for key, value in context.items():
        if isinstance(value, list):
            replacement = ", ".join(str(item) for item in value)
        else:
            replacement = str(value)
        rendered = rendered.replace(f"{{{{ {key} }}}}", replacement)
    return rendered


class TemplateRenderer:
    """Render HTML templates."""

    def render(self, template_path: str, context: dict[str, Any]) -> str:
        return render_template(template_path, context)
