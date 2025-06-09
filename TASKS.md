## 📋 Issue List

### Issue #1: Set up project structure
#### AI Tasks
- Initialize the project with Poetry or pip
- Configure environment variables
- Set up logging with structlog
- Create the directory structure
#### Human Tasks
- Install dependencies using `poetry install`
- Verify logging output and environment configuration

### Issue #2: Implement Confluence integration
#### AI Tasks
- Create Confluence client wrapper exposing only `get_space_pages` and `get_space_pages_updated_since` to fetch page content in storage (XML) format
- Parse Storage Format to Markdown
- Handle GitLab and yEd plugin content
- Implement pagination and error handling
#### Human Tasks
- Run `docker compose -f docker/docker-compose.integration.yml up -d`
- Configure the Confluence trial license
- Execute the integration tests to ensure connectivity

### Issue #3: Implement YouTrack integration
#### AI Tasks
- Set up OAuth2 authentication
- Create issue export functionality
- Convert issues to Markdown
- Handle attachments and comments
#### Human Tasks
- Provide valid YouTrack credentials
- Run integration tests against a real YouTrack instance

### Issue #4: Set up ChromaDB vector storage
#### AI Tasks
- Initialize three collections (docs, code, issues)
- Configure persistence settings
- Implement connection pooling
- Create backup/restore functionality
#### Human Tasks
- Launch the database service and verify persistence across restarts

### Issue #5: Implement document chunking
#### AI Tasks
- Create `MarkdownHeaderTextSplitter`
- Implement chunk overlap strategy
- Preserve metadata through chunking
- Handle special content (tables, code blocks)
#### Human Tasks
- Validate chunking with large real-world documents

### Issue #6: Build embedding pipeline
#### AI Tasks
- Configure sentence-transformers models
- Implement batch processing
- Add caching layer
- Monitor embedding performance
#### Human Tasks
- Run the embedding pipeline with GPU resources and measure performance

### Issue #7: Create Documentation Agent
#### AI Tasks
- Implement search functionality
- Add relevance scoring
- Generate citations
- Handle Confluence-specific content
#### Human Tasks
- Evaluate search results manually for quality and relevance

### Issue #8: Create Code Agent
#### AI Tasks
- Parse local repository with GitPython
- Implement tree-sitter for multi-language support
- Extract functions, classes, docstrings
- Index external dependencies
#### Human Tasks
- Test the agent against large codebases to confirm accuracy

### Issue #9: Create Issue Agent
#### AI Tasks
- Implement YouTrack search
- Parse issue metadata
- Link related issues
- Generate issue summaries
#### Human Tasks
- Validate search results against a live YouTrack project

### Issue #10: Build agent orchestration
#### AI Tasks
- Create CrewAI agent manager
- Implement request routing
- Add multi-agent coordination
- Set up result aggregation
#### Human Tasks
- Run end-to-end scenarios to verify agent cooperation

### Issue #11: Create FastAPI backend
#### AI Tasks
- Implement all API endpoints
- Add request validation
- Set up error handling
- Create OpenAPI documentation
#### Human Tasks
- Deploy the API and run smoke tests

### Issue #12: Build MCP server
#### AI Tasks
- Create proxy to FastAPI
- Implement MCP protocol
- Add request/response logging
- Handle authentication
#### Human Tasks
- Verify server deployment and network accessibility

### Issue #13: Create Flutter frontend
#### AI Tasks
- Set up Flutter project structure
- Create search interface for all agents
- Implement result visualization
- Add configuration screens
- Build for web and mobile platforms
#### Human Tasks
- Run the Flutter app on each platform and perform manual UI testing

### Issue #14: Create comprehensive tests
#### AI Tasks
- Unit tests for each component
- Integration tests for agents
- E2E tests for API
#### Human Tasks
- Run the full test suite including Docker-based integration tests

### Issue #15: Write documentation
#### AI Tasks
- API usage guide
- Deployment instructions
- Configuration reference
- Troubleshooting guide
#### Human Tasks
- Proofread all documentation and confirm accuracy
