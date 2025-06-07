# MCP Server Project Requirements and Architecture

## 📦 Required Python Packages

### Multi-Agent Framework
```bash
pip install crewai crewai-tools
```

### Confluence Integration
```bash
pip install atlassian-python-api
```

### YouTrack Integration
```bash
pip install youtrack-python-openapi
```

### Vector Database
```bash
pip install chromadb
```

### Embeddings
```bash
pip install sentence-transformers
```

### Document Processing
```bash
pip install markdown2 python-markdown langchain-text-splitters markdownify beautifulsoup4 lxml
```

### Repository & Code Analysis
```bash
pip install gitpython tree-sitter tree-sitter-languages
```

### API Framework
```bash
pip install fastapi uvicorn python-multipart pydantic-settings httpx tenacity python-dotenv
```

### Frontend Development
```bash
# Flutter is installed separately - not a Python package
# See https://flutter.dev/docs/get-started/install
```

### Logging
```bash
pip install structlog rich
```

### Testing
```bash
pip install pytest pytest-asyncio pytest-cov pytest-mock
```

## 📁 Repository Structure

```
- packages/
  - confluence_extractor/
  - confluence_to_md/
  - youtrack_exporter/
  - md_vector_index/
  - code_vector_index/
  - agent_docs/
  - agent_code/
  - agent_issues/
- api/
  - FastAPI endpoints
  - OpenAPI documentation
- mcp/
  - Lightweight server to connect LLMs to FastAPI
- docker/
  - Dockerfile
  - docker-compose.yml
  - entrypoint.sh
- frontend/
  - Flutter web/mobile interface
- tests/
  - Unit/integration tests for each package
```

## 🏗️ Agents.md - System Architecture

```markdown
# Agents Architecture

## System Overview

The MCP Server uses CrewAI for multi-agent orchestration with the following specialized agents:

## Agent Definitions

### 1. Documentation Agent (agent_docs)
**Purpose:** Retrieve documentation chunks via semantic search from Confluence and other sources.

**Responsibilities:**
- Search Confluence pages including GitLab and yEd plugin content
- Parse Storage Format (XML) to Markdown
- Chunk documents with metadata preservation
- Perform semantic search on documentation
- Handle citations and source tracking

**Input:** 
```json
{
    "query": "<search text>",
    "top_k": 5,
    "filters": {
        "space": "optional_space_key",
        "type": "page|blogpost"
    }
}
```

**Output:**
```json
[
    {
        "text": "chunk content",
        "source": "confluence page url",
        "metadata": {
            "space": "SPACE_KEY",
            "page_id": "12345",
            "title": "Page Title"
        },
        "score": 0.85
    }
]
```

### 2. Code Agent (agent_code)
**Purpose:** Analyze and retrieve code from both local repository and external dependencies.

**Responsibilities:**
- Parse current repository using GitPython and tree-sitter
- Extract functions, classes, docstrings from Python files
- Support multiple languages (Python, JavaScript, Java, etc.)
- Index external package dependencies
- Generate usage examples from code context

**Input:**
```json
{
    "query": "<function name or description>",
    "top_k": 5,
    "filters": {
        "type": "function|class|module",
        "source": "local|external",
        "language": "python|javascript"
    }
}
```

**Output:**
```json
[
    {
        "code": "def function_name(args):\n    ...",
        "file": "src/module/file.py",
        "line_start": 42,
        "type": "function",
        "docstring": "Function documentation",
        "score": 0.92
    }
]
```

### 3. Issue Agent (agent_issues)
**Purpose:** Search and analyze YouTrack issues.

**Responsibilities:**
- Query YouTrack using JQL-like syntax
- Extract issue details and comments
- Convert to Markdown format
- Link related issues and documentation

**Input:**
```json
{
    "query": "<issue description or keywords>",
    "project": "optional_project_key",
    "status": ["In Progress", "Done"],
    "top_k": 10
}
```

**Output:**
```json
[
    {
        "issue_id": "PROJ-123",
        "title": "Issue Title",
        "description": "Issue description in markdown",
        "status": "In Progress",
        "assignee": "user@example.com",
        "score": 0.88
    }
]
```

## Vector Database Schema

### ChromaDB Collections

1. **docs_collection**
   - Confluence pages and documentation
   - Metadata: space, page_id, title, last_updated

2. **code_collection**
   - Repository and dependency code
   - Metadata: file_path, language, type, source

3. **issues_collection**
   - YouTrack issues
   - Metadata: project, status, assignee, created_date

## Embedding Models

- **Documentation**: `all-MiniLM-L6-v2` (384 dimensions)
- **Code**: `microsoft/codebert-base` (768 dimensions)
- **Issues**: `all-MiniLM-L6-v2` (384 dimensions)

## Agent Communication Flow

```
User Query → MCP Server → Agent Orchestrator
                              ↓
                    Route to Appropriate Agent(s)
                              ↓
                    Query Vector Database
                              ↓
                    Retrieve & Rank Results
                              ↓
                    Format Response → User
```

## API Endpoints

### FastAPI Routes
- `POST /agents/docs/search` - Documentation search
- `POST /agents/code/search` - Code search
- `POST /agents/issues/search` - Issue search
- `POST /agents/multi/search` - Multi-agent search
- `GET /agents/status` - Agent health status

### MCP Interface
- `/libs` - List installed libraries
- `/function-doc` - Get function documentation
- `/doc-search` - Search documentation
- `/code-search` - Search code
- `/issue-search` - Search issues
```

## 🔧 Complete Installation Command

```bash
pip install crewai crewai-tools atlassian-python-api youtrack-python-openapi \
    chromadb sentence-transformers markdown2 python-markdown \
    langchain-text-splitters markdownify beautifulsoup4 lxml \
    gitpython tree-sitter tree-sitter-languages fastapi uvicorn \
    python-multipart pydantic-settings httpx tenacity python-dotenv \
    structlog rich pytest pytest-asyncio pytest-cov pytest-mock
```

## 📱 Flutter Setup

```bash
# Install Flutter SDK
git clone https://github.com/flutter/flutter.git -b stable
export PATH="$PATH:`pwd`/flutter/bin"
flutter doctor

# Create Flutter frontend
cd frontend
flutter create . --platforms=web,ios,android
flutter pub add http provider
```

## 📋 Issue List

**Issue #1: Set up project structure**
- Initialize project with Poetry/pip
- Configure environment variables
- Set up logging with structlog
- Create directory structure

**Issue #2: Implement Confluence integration**
- Create Confluence client wrapper
- Parse Storage Format to Markdown
- Handle GitLab and yEd plugin content
- Implement pagination and error handling

**Issue #3: Implement YouTrack integration**
- Set up OAuth2 authentication
- Create issue export functionality
- Convert issues to Markdown
- Handle attachments and comments

**Issue #4: Set up ChromaDB vector storage**
- Initialize three collections (docs, code, issues)
- Configure persistence settings
- Implement connection pooling
- Create backup/restore functionality

**Issue #5: Implement document chunking**
- Create MarkdownHeaderTextSplitter
- Implement chunk overlap strategy
- Preserve metadata through chunking
- Handle special content (tables, code blocks)

**Issue #6: Build embedding pipeline**
- Configure sentence-transformers models
- Implement batch processing
- Add caching layer
- Monitor embedding performance

**Issue #7: Create Documentation Agent**
- Implement search functionality
- Add relevance scoring
- Generate citations
- Handle Confluence-specific content

**Issue #8: Create Code Agent**
- Parse local repository with GitPython
- Implement tree-sitter for multi-language support
- Extract functions, classes, docstrings
- Index external dependencies

**Issue #9: Create Issue Agent**
- Implement YouTrack search
- Parse issue metadata
- Link related issues
- Generate issue summaries

**Issue #10: Build agent orchestration**
- Create CrewAI agent manager
- Implement request routing
- Add multi-agent coordination
- Set up result aggregation

**Issue #11: Create FastAPI backend**
- Implement all API endpoints
- Add request validation
- Set up error handling
- Create OpenAPI documentation

**Issue #12: Build MCP server**
- Create proxy to FastAPI
- Implement MCP protocol
- Add request/response logging
- Handle authentication

**Issue #13: Create Flutter frontend**
- Set up Flutter project structure
- Create search interface for all agents
- Implement result visualization
- Add configuration screens
- Build for web and mobile platforms

**Issue #14: Create comprehensive tests**
- Unit tests for each component
- Integration tests for agents
- E2E tests for API

**Issue #15: Write documentation**
- API usage guide
- Deployment instructions
- Configuration reference
- Troubleshooting guide
