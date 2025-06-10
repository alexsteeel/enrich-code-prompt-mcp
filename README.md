# MCP Server

This repository contains a collection of utilities and agents for building the Multi-agent Control Plane (MCP) server.

## Environment

Copy `.env.example` to `.env` and fill in the Confluence credentials:

```
CONFLUENCE_URL
CONFLUENCE_USERNAME
CONFLUENCE_API_TOKEN
CONFLUENCE_SPACE_KEY
```

These variables are used by the integration tests and the Confluence client.

## Packages

- [agent_code](packages/agent_code/README.md)
- [agent_docs](packages/agent_docs/README.md)
- [agent_issues](packages/agent_issues/README.md)
- [code_vector_index](packages/code_vector_index/README.md)
- [confluence_extractor](packages/confluence_extractor/README.md)
- [confluence_to_md](packages/confluence_to_md/README.md)
- [md_vector_index](packages/md_vector_index/README.md)
- [youtrack_exporter](packages/youtrack_exporter/README.md)
- [docker](docker/README.md)

To spin up a local Confluence instance for integration tests:

```bash
docker compose -f docker/docker-compose.integration.yml up -d
```
