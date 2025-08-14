# 🚀 OpenManus-MCP

**Powerful AI Agent Automation Tools via Model Context Protocol (MCP)**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

OpenManus-MCP is a comprehensive MCP server that brings advanced automation capabilities to AI assistants through a rich collection of tools including browser automation, shell execution, file operations, Python code execution, web search, and more.

> 🌟 **Built on the foundation of the original [OpenManus](https://github.com/FoundationAgents/OpenManus) project** - a groundbreaking open-source AI agent framework that revolutionized autonomous task execution.

## ✨ Key Features

- 🌐 **Advanced Browser Automation** - Full Playwright-powered web browser control with AI-powered content extraction
- 💻 **Shell Command Execution** - Persistent bash sessions with background process support
- 📝 **Intelligent File Operations** - Comprehensive file and directory management
- 🐍 **Safe Python Execution** - Isolated Python code execution with timeout protection
- 🔍 **Multi-Engine Web Search** - Search across Google, Bing, DuckDuckGo with content fetching
- 🧹 **Resource Management** - Automatic cleanup and process termination
- ⚡ **High Performance** - Optimized for speed and reliability
- 🔒 **Security First** - Process isolation and timeout protection

## 🎯 Perfect For

- **AI-Powered Web Automation** - Scraping, form filling, data extraction
- **Development Workflows** - Code analysis, testing, deployment automation  
- **Data Collection** - Research, monitoring, competitive analysis
- **System Administration** - File management, process control, maintenance
- **Research & Analysis** - Information gathering, report generation

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) package manager (recommended)

### Installation

#### Option 1: Using our setup script (Windows)

```bash
git clone https://github.com/your-username/OpenManus-MCP.git
cd OpenManus-MCP
.\setup.bat
```

#### Option 2: Manual installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/OpenManus-MCP.git
cd OpenManus-MCP
```

2. **Create virtual environment:**

```bash
uv venv --python 3.12
source .venv/bin/activate  # Unix/macOS
# .venv\Scripts\activate  # Windows
```

3. **Install dependencies:**

```bash
uv pip install -r requirements-mcp.txt
```

4. **Install browser dependencies (optional but recommended):**

```bash
playwright install
```

### Running the MCP Server

#### Quick Start (Windows)

```bash
.\start.bat
```

#### Manual Start

```bash
python mcp_server_working.py
```

### Integration with Warp Terminal

1. **Add to Warp MCP configuration:**

Add this to your Warp MCP settings:

```json
{
  "mcpServers": {
    "openmanus": {
      "command": "path/to/your/OpenManus-MCP/start.bat",
      "description": "OpenManus automation tools with browser, shell, file ops, Python execution, and web search"
    }
  }
}
```

2. **Restart Warp** to load the new MCP server

3. **Start using tools** - The AI assistant will now have access to all OpenManus tools!

## 🛠️ Available Tools

OpenManus-MCP provides a comprehensive suite of automation tools:

| Tool | Description | Key Features |
|------|-------------|-------------|
| 🌐 **browser_use** | Advanced browser automation | Playwright-powered, AI content extraction, tab management |
| 💻 **bash** | Shell command execution | Persistent sessions, background processes, interactive support |
| 📝 **str_replace_editor** | File editing and management | Precise string replacement, undo support, directory viewing |
| 🐍 **python** | Python code execution | Process isolation, timeout protection, output capture |
| 📁 **file_ops** | File system operations | Directory management, file operations, permissions |
| 🔍 **web_search** | Multi-engine web search | Google, Bing, DuckDuckGo with content fetching |
| 🛑 **terminate** | Process control | Clean resource management and termination |

## 📚 Documentation

- **[Comprehensive Tutorial](TUTORIAL.md)** - Detailed guide for all tools with examples
- **[MCP Integration Guide](README-MCP.md)** - Technical setup and integration details

## 📁 Project Structure

```
OpenManus-MCP/
├── mcp_server_working.py          # Main MCP server
├── start.bat                      # Windows startup script
├── setup.bat                      # Windows setup script 
├── requirements-mcp.txt           # Simplified dependencies
├── warp-mcp-config.json          # Warp integration config
├── TUTORIAL.md                   # Complete usage tutorial
├── README-MCP.md                 # Technical documentation
└── app/
    └── tool/
        ├── bash.py                   # Shell command tool
        ├── browser_use_tool.py       # Browser automation  
        ├── file_operations.py        # File system operations
        ├── python_execute.py         # Python execution
        ├── str_replace_editor.py     # File editing
        ├── web_search.py             # Web search
        └── terminate.py              # Process termination
```

## 🤝 Contributing

We welcome contributions! Please feel free to:

- 🐛 Report bugs via [GitHub Issues](../../issues)
- 💡 Suggest new features or improvements
- 🔧 Submit pull requests
- 📚 Improve documentation

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Acknowledgement

Thanks to [anthropic-computer-use](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)
and [browser-use](https://github.com/browser-use/browser-use) for providing basic support for this project!

Additionally, we are grateful to [AAAJ](https://github.com/metauto-ai/agent-as-a-judge), [MetaGPT](https://github.com/geekan/MetaGPT), [OpenHands](https://github.com/All-Hands-AI/OpenHands) and [SWE-agent](https://github.com/SWE-agent/SWE-agent).

We also thank stepfun(阶跃星辰) for supporting our Hugging Face demo space.

OpenManus is built by contributors from MetaGPT. Huge thanks to this agent community!

## Cite
```bibtex
@misc{openmanus2025,
  author = {Xinbin Liang and Jinyu Xiang and Zhaoyang Yu and Jiayi Zhang and Sirui Hong and Sheng Fan and Xiao Tang},
  title = {OpenManus: An open-source framework for building general AI agents},
  year = {2025},
  publisher = {Zenodo},
  doi = {10.5281/zenodo.15186407},
  url = {https://doi.org/10.5281/zenodo.15186407},
}
```
