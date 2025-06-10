from __future__ import annotations

import re
from typing import Optional

from bs4 import BeautifulSoup
from markdownify import markdownify as md


def _handle_macros(soup: BeautifulSoup) -> None:
    """Convert certain Confluence macros into more useful HTML."""
    for macro in soup.find_all("ac:structured-macro", {"ac:name": "yEd"}):
        attachment = macro.find("ri:attachment")
        if attachment and attachment.has_attr("ri:filename"):
            img = soup.new_tag("img", src=attachment["ri:filename"], alt=attachment["ri:filename"])
            macro.replace_with(img)
        else:
            macro.decompose()

    for macro in soup.find_all("ac:structured-macro", {"ac:name": "gitlab"}):
        link = macro.find("a")
        if link and link.has_attr("href"):
            macro.replace_with(link)
        else:
            macro.decompose()


def storage_to_markdown(storage: str) -> str:
    """Convert Confluence storage format XML (XHTML) to Markdown."""
    soup = BeautifulSoup(storage, "lxml")

    _handle_macros(soup)

    html = str(soup)
    markdown = md(html, heading_style="ATX")

    # Collapse multiple blank lines
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip()
