# 🏗️ OpenManus-MCP Project Structure

This document outlines the clean, focused structure of the OpenManus-MCP repository after cleanup.

## 📁 Root Directory

```
OpenManus-MCP/
├── 📄 README.md                    # Main project documentation
├── 📄 README-MCP.md               # Technical MCP integration guide
├── 📄 TUTORIAL.md                 # Comprehensive tutorial for all tools
├── 📄 LICENSE                     # MIT License
├── 🔧 mcp_server_working.py       # Main MCP server (primary entry point)
├── 🚀 start.bat                   # Windows startup script
├── ⚙️ setup.bat                   # Windows environment setup script
├── 📦 requirements-mcp.txt        # Simplified MCP dependencies
├── 📦 requirements.txt            # Full original dependencies
├── 🔗 warp-mcp-config.json        # Warp Terminal MCP integration config
├── 🐳 Dockerfile                  # Container configuration
├── 🔧 .gitignore                  # Git ignore rules
├── 🔧 .gitattributes              # Git attributes
└── 🔧 .pre-commit-config.yaml     # Pre-commit hooks configuration
```

## 🛠️ Core Application (`app/`)

### 📁 Tools Directory (`app/tool/`)

The heart of OpenManus-MCP - all automation capabilities:

```
app/tool/
├── 🌐 browser_use_tool.py         # Advanced browser automation (Playwright + AI)
├── 💻 bash.py                     # Shell command execution with persistent sessions
├── 📝 str_replace_editor.py       # File editing with precision string replacement
├── 🐍 python_execute.py          # Safe Python code execution
├── 📁 file_operations.py          # File system operations
├── 🔍 web_search.py               # Multi-engine web search
├── 🛑 terminate.py               # Process control and cleanup
├── 🔧 base.py                     # Base tool interface
└── 🔍 search/                     # Web search engine implementations
    ├── 🟢 google_search.py       # Google search implementation
    ├── 🔵 bing_search.py          # Bing search implementation
    ├── 🦆 duckduckgo_search.py    # DuckDuckGo search implementation
    └── 🟡 baidu_search.py         # Baidu search implementation
```

### 📁 Other App Directories

```
app/
├── 🤖 agent/                      # Agent implementations
├── 🔄 flow/                       # Workflow management
├── 📡 mcp/                        # MCP protocol implementations
├── 💭 prompt/                     # Prompt templates
├── 🏗️ sandbox/                    # Sandboxing functionality
├── 📊 chart_visualization/        # Data visualization tools
├── 🔧 config.py                   # Configuration management
├── 🤖 llm.py                      # LLM integrations
├── 📝 logger.py                   # Logging utilities
├── 🔗 schema.py                   # Data schemas
└── ⚡ exceptions.py               # Custom exceptions
```

## 🎯 Key Features by Tool

| Tool | Primary Use Case | Key Capabilities |
|------|------------------|------------------|
| 🌐 `browser_use` | Web automation | Playwright control, AI content extraction, tab management |
| 💻 `bash` | Shell operations | Persistent sessions, background processes, interactive support |
| 📝 `str_replace_editor` | File editing | Precise replacements, undo support, directory viewing |
| 🐍 `python` | Code execution | Process isolation, timeout protection, output capture |
| 📁 `file_ops` | File management | Directory operations, permissions, file info |
| 🔍 `web_search` | Information gathering | Multi-engine search, content fetching |
| 🛑 `terminate` | Resource control | Clean process termination |

## 🚀 Quick Start

1. **Setup**: `./setup.bat` (Windows) or manual installation
2. **Run**: `./start.bat` (Windows) or `python mcp_server_working.py`
3. **Integrate**: Add to Warp using `warp-mcp-config.json`

## 📚 Documentation Hierarchy

1. **README.md** → Overview and quick start
2. **TUTORIAL.md** → Comprehensive usage guide with examples
3. **README-MCP.md** → Technical integration details

## 🧹 Removed in Cleanup

- ❌ Old MCP server variants (`mcp_server_*.py` except working version)
- ❌ Original OpenManus standalone files (`main.py`, `run_*.py`, etc.)
- ❌ Language-specific READMEs (`README_*.md`)
- ❌ Development-specific directories (`.github/`, `.vscode/`, `config/`, `assets/`)
- ❌ Original project metadata (`CODE_OF_CONDUCT.md`)

## 📦 Dependencies

- **Minimal**: `requirements-mcp.txt` - Essential MCP server dependencies
- **Full**: `requirements.txt` - Complete original project dependencies

## 🔧 Configuration

- **Warp Integration**: `warp-mcp-config.json`
- **Server Configuration**: Embedded in `mcp_server_working.py`
- **Setup Scripts**: `setup.bat` and `start.bat` for Windows

---

This clean structure focuses purely on MCP server functionality while maintaining all the powerful automation capabilities of the original OpenManus project! 🎉
