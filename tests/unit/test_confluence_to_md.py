import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from packages.confluence_to_md import storage_to_markdown


@pytest.mark.unit
def test_storage_to_markdown_simple():
    html = '<p>Hello <b>world</b></p>'
    md = storage_to_markdown(html)
    assert md.strip() == 'Hello **world**'


@pytest.mark.unit
def test_storage_to_markdown_yed_image():
    html = (
        '<ac:structured-macro ac:name="yEd">'
        '<ri:attachment ri:filename="diagram.png" />'
        '</ac:structured-macro>'
    )
    md = storage_to_markdown(html)
    assert md.strip() == '![diagram.png](diagram.png)'
