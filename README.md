# Inverkids MCP Server

A Model Context Protocol (MCP) server that provides access to the Inverkids educational platform API. This server enables AI assistants to interact with educational content, user management, courses, and student evaluation data.

## Features

- **Authentication**: Secure login using enrollment ID and password
- **Catalog Management**: Access to modules, topics, activities, and learning texts
- **Course Management**: Retrieve course information and data
- **User Management**: Access user profiles and group information
- **Evaluation System**: Access to grades and student feedback
- **School Management**: Retrieve school information based on user permissions
- **MCP Protocol**: Native Model Context Protocol implementation using FastMCP

## Architecture

```
┌─────────────────┐
│   AI Assistant  │
│   (Claude)      │
└────────┬────────┘
         │
         │ MCP Protocol (stdio)
         ▼
┌─────────────────┐
│   MCP Server    │
│   (FastMCP)     │
└────────┬────────┘
         │
         │ HTTP/REST
         ▼
┌─────────────────┐
│  Inverkids API  │
│   (Backend)     │
└─────────────────┘
```

## Prerequisites

- Python 3.11+
- Access to Inverkids Backend API
- Claude Desktop app or MCP-compatible client

## Installation

### Local Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd inverkids-mcp-server
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
BACKEND_BASE_URL=https://your-backend-api.com
HTTP_TIMEOUT=30
MAX_RETRIES=3
AUTH_TIMEOUT=10
MCP_NAME=inverkids-mcp
LOG_LEVEL=INFO

# Optional: Default credentials for service identity
MCP_DEFAULT_ENROLLMENT_ID=your_enrollment_id
MCP_DEFAULT_PASSWORD=your_password
```

## Usage

### Claude Desktop Configuration

Add the server to your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "inverkids": {
      "command": "python",
      "args": ["/path/to/inverkids-mcp-server/start_mcp.py"],
      "env": {
        "BACKEND_BASE_URL": "https://your-backend-api.com",
        "MCP_DEFAULT_ENROLLMENT_ID": "your_enrollment_id",
        "MCP_DEFAULT_PASSWORD": "your_password"
      }
    }
  }
}
```

### Available MCP Tools

#### Authentication

**`login`** - Authenticate a user

```json
{
  "enrollment_id": "student123",
  "password": "password123"
}
```

Returns authentication token for subsequent requests. If default credentials are configured, can be called without parameters.

#### User Management

**`get_profile`** - Get current user profile

```json
{
  "token": "auth_token_here"
}
```

**`get_users`** - Get accessible users based on role

```json
{
  "token": "auth_token_here"
}
```

#### Catalog

**`get_full_catalog`** - Get complete catalog hierarchy

```json
{
  "level": "5",
  "white_label": "inverkids",
  "user_lang": "es",
  "token": "auth_token_here"
}
```

**`get_modules`** - Get learning modules (paginated)

```json
{
  "token": "auth_token_here",
  "level": "5",
  "white_label": "inverkids",
  "module_id": "optional",
  "limit": 10,
  "offset": 0
}
```

**`get_topics`** - Get topics (paginated)

```json
{
  "token": "auth_token_here",
  "module_id": "module_123",
  "level": "5",
  "limit": 10,
  "offset": 0
}
```

**`get_activities`** - Get activities (paginated)

```json
{
  "token": "auth_token_here",
  "topic_id": "topic_123",
  "include_content": false,
  "limit": 10,
  "offset": 0
}
```

**`get_texts`** - Get learning texts (paginated)

```json
{
  "token": "auth_token_here",
  "topic_id": "topic_123",
  "include_content": false,
  "limit": 10,
  "offset": 0
}
```

#### Courses

**`get_courses`** - Get all courses

```json
{
  "token": "auth_token_here"
}
```

**`get_courses_by_user_type`** - Filter courses by user type

```json
{
  "user_type": "student",
  "token": "auth_token_here"
}
```

**`get_courses_names`** - Get course names

```json
{
  "level": "5",
  "label": "inverkids",
  "token": "auth_token_here"
}
```

**`get_courses_data`** - Get full course data

```json
{
  "level": "5",
  "label": "inverkids",
  "token": "auth_token_here"
}
```

#### Groups

**`get_groups`** - Get accessible groups

```json
{
  "token": "auth_token_here"
}
```

**`get_groups_by_level`** - Filter groups by level

```json
{
  "level": "5",
  "token": "auth_token_here"
}
```

**`get_group_users`** - Get students in groups

```json
{
  "group_ids": ["group_1", "group_2"],
  "token": "auth_token_here"
}
```

#### Evaluation

**`get_grades`** - Get student grades (paginated)

```json
{
  "token": "auth_token_here",
  "level": "5",
  "group_id": "group_123",
  "student_id": "student_456",
  "limit": 50,
  "offset": 0
}
```

**`get_feedback`** - Get student feedback (paginated)

```json
{
  "token": "auth_token_here",
  "level": "5",
  "student_id": "student_456",
  "limit": 50,
  "offset": 0
}
```

#### Schools

**`get_schools`** - Get accessible schools

```json
{
  "token": "auth_token_here",
  "white_label": "inverkids"
}
```

## Project Structure

```
inverkids-mcp-server/
├── src/
│   ├── app/
│   │   ├── services/        # Business logic
│   │   └── validators/      # Input validation
│   ├── controllers/         # API controllers
│   ├── infrastructure/
│   │   ├── config/         # Configuration and constants
│   │   ├── decorators/     # Error handling, logging, auth
│   │   └── http/           # HTTP clients
│   ├── mcp/
│   │   ├── handlers/       # MCP tool handlers
│   │   ├── tools/          # MCP tool definitions
│   │   └── app.py          # FastMCP server instance
│   ├── models/             # Data models
│   └── utils/              # Utilities and exceptions
├── start_mcp.py            # MCP server entry point
└── requirements.txt        # Python dependencies
```

## Error Handling

The server includes comprehensive error handling with specific exception types:

- **ValidationError** (400): Invalid input parameters
- **AuthenticationError** (401): Authentication failed
- **AuthorizationError** (403): Insufficient permissions
- **ResourceNotFoundError** (404): Resource not found
- **RateLimitError** (429): Rate limit exceeded
- **BackendError** (500): Backend service error
- **NetworkError** (503): Network communication failure

All errors return structured responses:

```json
{
  "error": "ValidationError",
  "message": "Enrollment ID is required",
  "status_code": 400,
  "details": {
    "field": "enrollment_id"
  }
}
```

## Security

- All API endpoints require authentication tokens (except login)
- Tokens are validated before processing requests
- User access is automatically restricted based on role
- Passwords are validated for minimum length and format
- HTTP client includes automatic retry with exponential backoff
- Connection pooling for efficient resource usage
- Environment-based credential configuration

## Logging

The server uses structured JSON logging with the following features:

- Timestamp, level, logger name, message
- Module, function, and line number
- Extra contextual fields
- Exception stack traces
- Configurable log level via `LOG_LEVEL` environment variable

Example log entry:

```json
{
  "timestamp": "2025-01-20T10:30:45.123456",
  "level": "INFO",
  "logger": "src.infrastructure.http.backend_client",
  "message": "BackendClient initialized",
  "module": "backend_client",
  "function": "__init__",
  "line": 45,
  "base_url": "https://api.inverkids.com",
  "timeout": 30
}
```

## Development

### Running the Server Standalone

For testing without Claude Desktop:

```bash
python start_mcp.py
```

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black src/
ruff check src/
```

### Type Checking

```bash
mypy src/
```

## Troubleshooting

### Connection Errors

If you see connection errors, verify:

- Backend API URL is correct and accessible
- Environment variables are set correctly
- Firewall allows outbound connections

### Authentication Errors

- Verify enrollment ID and password are correct
- Check token is being passed to authenticated endpoints
- Ensure token hasn't expired
- Verify default credentials in configuration (if using service identity)

### Timeout Issues

Increase timeout values in `.env`:

```env
HTTP_TIMEOUT=60
AUTH_TIMEOUT=20
```

### Claude Desktop Integration Issues

- Check Claude Desktop logs for startup errors
- Verify Python path in configuration is correct
- Ensure all dependencies are installed in the correct environment
- Restart Claude Desktop after configuration changes

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

[Your License Here]

## Support

For issues and questions:

- Create an issue in the repository
- Contact the development team
- Check the documentation at [docs link]

## Changelog

### Version 1.0.0

- Initial release
- MCP server implementation using FastMCP
- Complete tool suite for Inverkids API
- Comprehensive error handling
- Structured logging
- Service identity support
