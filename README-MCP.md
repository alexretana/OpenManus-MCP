# OpenManus MCP Server

A comprehensive Model Context Protocol (MCP) server that provides AI clients with powerful automation tools for various tasks including shell command execution, browser automation, file operations, Python code execution, and web searching.

## Features

### 🛠️ Available Tools

- **🖥️ Shell Commands** (`bash`) - Execute bash commands with persistent session management
- **🌐 Browser Automation** (`browser_use`) - Comprehensive web browser automation with Playwright
- **📁 File Operations** (`file_ops`) - File and directory management (copy, move, delete, etc.)
- **📝 Text Editor** (`str_replace_editor`) - Advanced file editing with search and replace
- **🐍 Python Execution** (`python`) - Execute Python code with timeout and safety restrictions
- **🔍 Web Search** (`web_search`) - Search the web using multiple search engines
- **🛑 Process Control** (`terminate`) - Terminate processes and cleanup resources

### 🎯 Key Capabilities

- **Persistent Sessions**: Shell commands maintain state across calls
- **Safety Features**: Python execution with timeout and sandboxing
- **Multi-Engine Search**: Automatic fallback across Google, Bing, DuckDuckGo, and Baidu
- **Advanced Browser Control**: Full page automation, screenshot capture, content extraction
- **Comprehensive File Management**: All standard file operations plus advanced features
- **Structured Responses**: Consistent JSON-formatted tool responses

## Quick Start

### Prerequisites

- Python 3.8+
- All dependencies listed in the project requirements

### Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

```bash
# Run the MCP server (stdio transport)
python mcp_server.py

# With debug logging
python mcp_server.py --log-level DEBUG
```

## Integration with Warp

### Automatic Configuration

Use the provided configuration file (`warp-mcp-config.json`):

```json
{
  "mcpServers": {
    "OpenManus": {
      "command": "python",
      "args": ["mcp_server.py"],
      "working_directory": "/path/to/OpenManus-MCP",
      "env": {
        "PYTHONPATH": "/path/to/OpenManus-MCP"
      }
    }
  }
}
```

### Manual Configuration in Warp

1. Open Warp settings
2. Navigate to AI → Manage MCP servers
3. Click "Add" and choose "CLI Server (Command)"
4. Configure:
   - **Command**: `python`
   - **Args**: `["mcp_server.py"]`
   - **Working Directory**: `/path/to/OpenManus-MCP`
   - **Environment Variables**: `{"PYTHONPATH": "/path/to/OpenManus-MCP"}`

## Tool Reference

### Shell Commands (`bash`)

Execute shell commands with persistent session management.

**Example Usage:**
```
Execute: ls -la
Execute: cd /tmp && pwd
Execute: python --version
```

**Features:**
- Persistent bash session
- Timeout protection
- Interactive command support
- Background process handling

### Browser Automation (`browser_use`)

Comprehensive browser automation capabilities.

**Available Actions:**
- `go_to_url` - Navigate to a URL
- `click_element` - Click on page elements
- `input_text` - Type text into form fields
- `scroll_down/up` - Scroll the page
- `extract_content` - Extract structured content
- `web_search` - Perform web searches
- `switch_tab` - Manage browser tabs

**Example Usage:**
```
Navigate to https://example.com
Click element at index 2
Input "search query" into element 5
Extract content with goal "find contact information"
```

### File Operations (`file_ops`)

Comprehensive file and directory management.

**Available Operations:**
- `list_directory` - List directory contents
- `create_directory` - Create directories
- `copy_file/directory` - Copy files and directories
- `move_file/directory` - Move files and directories
- `delete_file/directory` - Delete files and directories
- `get_file_info` - Get detailed file information
- `find_files` - Find files by pattern
- `change_permissions` - Change file permissions

**Example Usage:**
```
List directory: /home/user/documents
Copy file from /source/file.txt to /dest/file.txt
Find files in /project with pattern "*.py"
Get file info for /important/document.pdf
```

### Text Editor (`str_replace_editor`)

Advanced file editing with precision string replacement.

**Available Commands:**
- `view` - Display file contents
- `create` - Create new files
- `str_replace` - Replace text precisely
- `insert` - Insert text at specific lines
- `undo_edit` - Revert last change

**Example Usage:**
```
View file: /path/to/file.py
Replace "old_function()" with "new_function()" in /path/to/file.py
Insert "# New comment" at line 10 in /path/to/file.py
```

### Python Execution (`python`)

Execute Python code safely with timeout protection.

**Features:**
- Multiprocessing isolation
- Configurable timeout
- Output capture
- Error handling

**Example Usage:**
```
Execute Python: print("Hello, World!")
Execute Python: import math; print(math.pi)
Execute Python: [calculation or data processing code]
```

### Web Search (`web_search`)

Search the web using multiple search engines with automatic fallback.

**Features:**
- Multi-engine support (Google, Bing, DuckDuckGo, Baidu)
- Content fetching from results
- Structured result formatting
- Retry mechanisms

**Example Usage:**
```
Search: "Python programming tutorial"
Search with content: "latest AI developments" (fetch_content=true)
```

## Configuration Options

### Environment Variables

- `PYTHONPATH` - Ensure Python can find the app modules
- `OPENAI_API_KEY` - For LLM-powered content extraction
- `GOOGLE_API_KEY` - For enhanced Google search
- `BING_API_KEY` - For Bing search integration

### Server Configuration

The server supports various configuration options through the config system:

- Browser settings (headless mode, proxy, etc.)
- Search engine preferences and API keys
- Sandbox environment settings
- Timeout and safety parameters

## Development

### Adding New Tools

1. Create a new tool class inheriting from `BaseTool`:

```python
from app.tool.base import BaseTool, ToolResult

class MyCustomTool(BaseTool):
    name: str = "my_tool"
    description: str = "Description of what my tool does"
    parameters: dict = {
        "type": "object",
        "properties": {
            "param1": {"type": "string", "description": "Parameter description"}
        },
        "required": ["param1"]
    }
    
    async def execute(self, param1: str, **kwargs) -> ToolResult:
        # Tool implementation
        return ToolResult(output="Success!")
```

2. Register the tool in the server:

```python
# In OpenManusMCPServer._add_enhanced_tools()
self.tools["my_tool"] = MyCustomTool()
```

### Testing

Run the server in debug mode to test tool functionality:

```bash
python mcp_server.py --log-level DEBUG
```

## Security Considerations

- **Python Execution**: Code runs in a separate process with timeout protection
- **File Operations**: All file paths are validated and restricted to accessible areas
- **Browser Automation**: Runs in a controlled browser environment
- **Shell Commands**: Session-based execution with timeout protection

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure `PYTHONPATH` includes the project directory
2. **Browser Issues**: Check that browser dependencies are installed
3. **Permission Errors**: Verify file system permissions for operations
4. **Timeout Issues**: Adjust timeout settings for long-running operations

### Debug Mode

Run with debug logging to troubleshoot issues:

```bash
python mcp_server.py --log-level DEBUG
```

### Log Location

Logs are output to stderr and can be redirected:

```bash
python mcp_server.py 2> server.log
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Test thoroughly
5. Submit a pull request

## License

This project is based on the OpenManus framework. Please refer to the original project for licensing information.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the tool documentation
3. Open an issue on GitHub

---

**Note**: This MCP server provides powerful automation capabilities. Use responsibly and ensure proper security measures in production environments.
