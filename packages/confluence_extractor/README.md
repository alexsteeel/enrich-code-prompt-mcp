# confluence_extractor

This package contains the `confluence_extractor` module used by the MCP server.
It relies on the [atlassian-python-api](https://pypi.org/project/atlassian-python-api/)
library to communicate with Confluence.

[`ConfluenceClient.get_page`](./__init__.py#L24-L28) returns a page body in
Confluence storage format (XML). The client expands `body.storage` to retrieve
the raw XML. The upstream library confirms that this parameter returns
content in Confluence storage format as shown in its
[source code](https://github.com/atlassian-api/atlassian-python-api/blob/master/atlassian/confluence.py#L2230-L2235).

Credentials are read from the environment:

```
CONFLUENCE_URL
CONFLUENCE_USERNAME
CONFLUENCE_API_TOKEN
```

See `.env.example` for a full list including `CONFLUENCE_SPACE_KEY` used in tests.

[Back to project README](../../README.md)
