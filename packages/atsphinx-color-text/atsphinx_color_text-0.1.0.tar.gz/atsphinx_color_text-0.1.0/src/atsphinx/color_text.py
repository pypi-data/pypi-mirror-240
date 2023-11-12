"""Text color changer for Sphinx."""
from typing import List, Optional

from docutils import nodes
from docutils.parsers.rst import roles
from docutils.parsers.rst.states import Inliner
from docutils.writers import Writer
from sphinx.application import Sphinx
from sphinx.config import Config

__version__ = "0.1.0"

COLORS = {
    "black": "#000000",
    "silver": "#c0c0c0",
    "gray": "#808080",
    "white": "#ffffff",
    "maroon": "#800000",
    "red": "#ff0000",
    "purple": "#800080",
    "fuchsia": "#ff00ff",
    "green": "#008000",
    "lime": "#00ff00",
    "olive": "#808000",
    "yellow": "#ffff00",
    "navy": "#000080",
    "blue": "#0000ff",
    "teal": "#008080",
    "aqua": "#00ffff",
}
"""Major named-colors.

Use "Standard colors" from
 `MDN <https://developer.mozilla.org/en-US/docs/Web/CSS/named-color>`_.
"""


class ColorText(nodes.Inline, nodes.TextElement):  # noqa: D101
    pass


def visit_color_text(self: Writer, node: ColorText):  # noqa: D103
    self.body.append(self.starttag(node, "span", "", style=node["style"]))


def depart_color_text(self: Writer, node: ColorText):  # noqa: D103
    self.body.append("</span>")


def create_color_role(code):
    """Generate role function from color-code(RGB)."""

    def _color_role(
        role: str,
        rawtext: str,
        text: str,
        lineno: int,
        inliner: Inliner,
        options: Optional[dict] = None,
        content: Optional[List[str]] = None,
    ):  # noqa: D103
        options = roles.normalized_role_options(options)
        messages = []
        node = ColorText(rawtext, text)
        node["style"] = f"color: {code}"
        return [node], messages

    return _color_role


def register_colors(app: Sphinx, config: Config):
    """Grenerate and register role for color-text.

    This func refs ``COLORS`` and conf.py to generate.
    """
    for name, code in COLORS.items():
        roles.register_canonical_role(f"color:{name}", create_color_role(code))


def setup(app: Sphinx):  # noqa: D103
    app.connect("config-inited", register_colors)
    app.add_node(ColorText, html=(visit_color_text, depart_color_text))
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
