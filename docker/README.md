# Docker Infrastructure

This folder contains Docker configurations used for development and testing.

`docker-compose.integration.yml` spins up a Confluence container for the
integration tests. It loads environment variables from `.env`. Start it with:

```bash
docker compose -f docker/docker-compose.integration.yml up -d
```
