# Tests

Unit tests run without external services. Integration tests require a Confluence container or a real instance.

1. Copy `.env.example` to `.env` and fill in the Confluence variables.
2. Start the container:
   ```bash
   docker compose -f docker/docker-compose.integration.yml up -d
   ```
3. Run all tests:
   ```bash
   poetry run pytest -q
   ```
   Integration tests are marked with `@pytest.mark.integration` and will be skipped if the environment variables are missing.
