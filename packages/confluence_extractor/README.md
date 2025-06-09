# confluence_extractor

This package contains the `confluence_extractor` module used by the MCP server.
It relies on the [atlassian-python-api](https://pypi.org/project/atlassian-python-api/)
library to communicate with Confluence.

`ConfluenceClient.get_page` returns a page body in Confluence storage format
(XML). You can see this in
[`__init__.py`](../confluence_extractor/__init__.py#L24-L28), where the client
expands `body.storage`. The upstream library notes that this parameter returns
content in Confluence storage format as shown in its
[source code](https://github.com/atlassian-api/atlassian-python-api/blob/master/atlassian/confluence.py#L2230-L2235).

[Back to project README](../../README.md)
