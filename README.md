# MCP Server

This repository contains a collection of utilities and agents for building the Multi-agent Control Plane (MCP) server.

## Setup

This project uses [Poetry](https://python-poetry.org/) for dependency management. Install Poetry and then run:

```bash
poetry install
```

This reads `pyproject.toml` and creates a virtual environment with all dependencies. Run the tests with:

```bash
poetry run pytest -q
```

## Environment

Copy `.env.example` to `.env` and fill in the Confluence credentials. The
Confluence Docker container and test suite both load this file automatically:

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

To spin up a local Confluence instance for integration tests (it reads
credentials from `.env`):

```bash
docker compose -f docker/docker-compose.integration.yml up -d
```

For details on running the test suite and configuring the Confluence container, see [tests/README.md](tests/README.md).
