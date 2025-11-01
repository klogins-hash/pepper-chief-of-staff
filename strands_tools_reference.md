# Strands Agent Tools Reference

## Key Tool Categories

### Memory & Knowledge
- **mem0_memory**: Store user and agent memories across sessions for personalization
- **agent_core_memory**: Store/retrieve memories with Amazon Bedrock Agent Core Memory
- **elasticsearch_memory**: Store/retrieve memories with AWS Elasticsearch, FAISS, or OpenSearch backends
- **retrieve**: Retrieve information from Amazon Bedrock Knowledge Bases with optional metadata

### Web & Search
- **tavily_search**: Real-time web search optimized for AI agents with custom parameters
- **tavily_extract**: Extract structured content from web pages with advanced processing
- **tavily_crawl**: Crawl websites with filtering and extraction starting from a base URL
- **exa_search**: Neural and keyword web search with auto mode for optimal results
- **exa_get_contents**: Extract full content and summaries from URLs with live crawling fallback
- **bright_data**: Web scraping, search queries, screenshots, structured data extraction
- **browser**: Web automation: navigation, testing, form filling

### File Operations
- **file_read**: Reading configuration files, parsing code files, loading datasets
- **file_write**: Writing results to files, creating new files, saving output data
- **editor**: Advanced file operations like syntax highlighting, pattern replacement, and multi-file edits

### Code Execution
- **python_repl**: Run Python code snippets with state persistence and security features
- **code_interpreter**: Execute code in sandbox environments supporting multiple languages, persistent sessions, file operations
- **shell**: Executing shell commands, interacting with the operating system, running scripts

### Communication & Integration
- **http_request**: Making API calls, fetching web data, sending data to external services
- **a2a_client**: Discover and communicate with A2A-compliant agents, send messages between agents
- **slack**: Interact with Slack workspace for messaging/monitoring
- **mcp_client**: Connect to external MCP servers/load remote tools

### Cloud Services
- **use_aws**: Interact with AWS services (S3, EC2, etc.) for cloud resource management

### Utilities
- **calculator**: Perform advanced mathematical calculations and symbolic math
- **current_time**: Get current time in specified timezone
- **sleep**: Pause execution for specified seconds
- **cron**: Schedule recurring tasks
- **journal**: Create and manage structured logs and documentation
- **diagram**: Create diagrams (AWS, UML, class diagrams, etc.)

### Multi-Agent
- **swarm**: Coordinate multiple AI agents for collaborative or competitive problem solving
- **workflow**: Define and execute multi-step workflows
- **use_llm**: Create nested AI loops with custom prompts
- **batch**: Call multiple tools in parallel

### Media
- **generate_image**: Create AI-generated images
- **image_reader**: Process and analyze images for AI applications
- **nova_reels**: Generate high-quality videos via Amazon Bedrock Nova Reel
- **search_video**: Semantic video search via TwelveLabs
- **chat_video**: Interactive video analysis with TwelveLabs

### Control Flow
- **think**: Advanced reasoning and multi-step thinking
- **handoff_to_user**: Hand control to user for confirmation or input
- **stop**: Gracefully terminate agent execution
