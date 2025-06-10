from __future__ import annotations

import os
from datetime import datetime
from typing import Any, Dict, Iterable, Optional

from atlassian import Confluence
from requests import HTTPError

from packages.confluence_to_md import storage_to_markdown


class ConfluenceClient:
    """Wrapper around the Atlassian Confluence client."""

    def __init__(self, url: Optional[str] = None, username: Optional[str] = None, api_token: Optional[str] = None) -> None:
        url = url or os.getenv("CONFLUENCE_URL")
        username = username or os.getenv("CONFLUENCE_USERNAME")
        api_token = api_token or os.getenv("CONFLUENCE_API_TOKEN")
        if not all([url, username, api_token]):
            raise ValueError("Confluence credentials are not fully configured")
        self.client = Confluence(url=url, username=username, password=api_token)

    def get_page(self, page_id: str) -> str:
        """Return page content in Confluence storage format (XML)."""
        try:
            page = self.client.get_page_by_id(page_id, expand="body.storage")
            return page.get("body", {}).get("storage", {}).get("value", "")
        except HTTPError as exc:
            raise RuntimeError(f"Failed to fetch page {page_id}") from exc


    def get_page_markdown(self, page_id: str) -> str:
        """Convenience method to fetch a page and convert to markdown."""
        storage = self.get_page(page_id)
        return storage_to_markdown(storage)

    def get_space_pages(self, space: str) -> Iterable[Dict[str, Any]]:
        """Yield all pages from a space including storage content."""
        pages = self.client.get_all_pages_from_space(space, expand="body.storage")
        for page in pages:
            yield page

    def get_space_pages_updated_since(self, space: str, since: datetime) -> Iterable[Dict[str, Any]]:
        """Yield pages updated after the given timestamp."""
        iso = since.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        cql = f'space="{space}" and type="page" and lastmodified > "{iso}"'
        start = 0
        limit = 50
        while True:
            try:
                data = self.client.cql(cql, limit=limit, start=start, expand="body.storage")
            except HTTPError as exc:
                raise RuntimeError("Confluence search failed") from exc
            results = data.get("results", [])
            if not results:
                break
            for item in results:
                yield item.get("content") or item
            if len(results) < limit:
                break
            start += limit
