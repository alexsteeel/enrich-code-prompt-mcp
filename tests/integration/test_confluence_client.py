import os
import sys
from pathlib import Path
from datetime import datetime
import pytest

sys.path.append(str(Path(__file__).resolve().parents[2]))

from packages.confluence_extractor import ConfluenceClient


@pytest.mark.integration
def test_fetch_pages_from_space():
    space = os.getenv("CONFLUENCE_SPACE_KEY")
    url = os.getenv("CONFLUENCE_URL")
    username = os.getenv("CONFLUENCE_USERNAME")
    token = os.getenv("CONFLUENCE_API_TOKEN")
    if not all([space, url, username, token]):
        pytest.skip("Confluence credentials not configured")
    client = ConfluenceClient(url=url, username=username, api_token=token)
    pages = list(client.get_space_pages(space))
    assert pages, "Expected at least one page"


@pytest.mark.integration
def test_fetch_pages_updated_since():
    space = os.getenv("CONFLUENCE_SPACE_KEY")
    url = os.getenv("CONFLUENCE_URL")
    username = os.getenv("CONFLUENCE_USERNAME")
    token = os.getenv("CONFLUENCE_API_TOKEN")
    if not all([space, url, username, token]):
        pytest.skip("Confluence credentials not configured")
    client = ConfluenceClient(url=url, username=username, api_token=token)
    pages = list(client.get_space_pages_updated_since(space, datetime(1970, 1, 1)))
    assert pages, "Expected at least one updated page"
