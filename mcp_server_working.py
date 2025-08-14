#!/usr/bin/env python3
"""
OpenManus MCP Server - Working version based on original pattern
"""

import argparse
import asyncio
import atexit
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict

# Add the current directory to Python path for imports
sys.path.insert(0, str(Path(__file__).parent))

try:
    from mcp.server.fastmcp import FastMCP
    MCP_AVAILABLE = True
except ImportError:
    print("MCP package not found. Please install with: uv pip install mcp", file=sys.stderr)
    MCP_AVAILABLE = False

# Core tools
from app.tool.bash import Bash
from app.tool.str_replace_editor import StrReplaceEditor
from app.tool.terminate import Terminate
from app.tool.python_execute import PythonExecute
from app.tool.file_operations import FileOperations

# Set up logging
logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stderr)])
logger = logging.getLogger(__name__)


class OpenManusMCPServer:
    """Simple MCP Server using FastMCP."""
    
    def __init__(self, name: str = "openmanus"):
        if not MCP_AVAILABLE:
            raise RuntimeError("MCP package not available")
        
        self.server = FastMCP(name)
        self.tools = {}
        
        # Initialize tools
        self._initialize_tools()
        self._register_tools()
    
    def _initialize_tools(self):
        """Initialize all available tools."""
        try:
            # Core tools that should always work
            self.tools["bash"] = Bash()
            self.tools["editor"] = StrReplaceEditor()
            self.tools["terminate"] = Terminate()
            self.tools["python"] = PythonExecute()
            self.tools["file_ops"] = FileOperations()
            
            # Optional tools that might fail
            try:
                from app.tool.web_search import WebSearch
                self.tools["web_search"] = WebSearch()
                logger.info("Web search tool loaded")
            except Exception as e:
                logger.warning(f"Web search tool not available: {e}")
            
            # Browser tool (requires heavy dependencies)
            try:
                from app.tool.browser_use_tool import BrowserUseTool
                self.tools["browser"] = BrowserUseTool()
                logger.info("Browser tool loaded")
            except Exception as e:
                logger.warning(f"Browser tool not available: {e}")
            
            logger.info(f"Initialized tools: {', '.join(self.tools.keys())}")
        except Exception as e:
            logger.error(f"Failed to initialize tools: {e}")
    
    def _register_tools(self):
        """Register all tools with the server."""
        for tool_name, tool_instance in self.tools.items():
            self._register_single_tool(tool_name, tool_instance)
    
    def _register_single_tool(self, tool_name: str, tool_instance):
        """Register a single tool with the server."""
        try:
            tool_param = tool_instance.to_param()
            function_def = tool_param["function"]
            
            # Create async wrapper function
            async def tool_wrapper(**kwargs):
                try:
                    logger.info(f"Executing {tool_name} with args: {kwargs}")
                    result = await tool_instance.execute(**kwargs)
                    
                    # Handle different result types
                    if hasattr(result, 'model_dump'):
                        output = json.dumps(result.model_dump(), indent=2)
                    elif isinstance(result, dict):
                        output = json.dumps(result, indent=2)
                    else:
                        output = str(result)
                    
                    logger.info(f"Tool {tool_name} completed successfully")
                    return output
                except Exception as e:
                    error_msg = f"Tool {tool_name} failed: {str(e)}"
                    logger.error(error_msg)
                    return error_msg
            
            # Register with FastMCP - only name and description
            tool_wrapper.__name__ = function_def["name"]
            tool_wrapper.__doc__ = function_def["description"]
            
            self.server.tool(
                name=function_def["name"],
                description=function_def["description"]
            )(tool_wrapper)
            
            logger.info(f"Registered tool: {tool_name}")
        except Exception as e:
            logger.error(f"Failed to register tool {tool_name}: {e}")
    
    async def cleanup(self):
        """Clean up server resources."""
        logger.info("Cleaning up server resources")
        if "browser" in self.tools and hasattr(self.tools["browser"], "cleanup"):
            try:
                await self.tools["browser"].cleanup()
            except Exception as e:
                logger.warning(f"Browser cleanup failed: {e}")
    
    def run(self, transport: str = "stdio"):
        """Run the MCP server."""
        logger.info(f"Starting OpenManus MCP Server with {transport} transport")
        logger.info(f"Available tools: {', '.join(self.tools.keys())}")
        
        # Register cleanup
        atexit.register(lambda: asyncio.run(self.cleanup()))
        
        # Run the server
        self.server.run(transport=transport)


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="OpenManus MCP Server")
    parser.add_argument(
        "--transport",
        choices=["stdio"],
        default="stdio",
        help="Communication method (default: stdio)",
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Set the logging level (default: INFO)",
    )
    return parser.parse_args()


def main():
    """Main entry point."""
    args = parse_args()
    
    # Set logging level
    logging.getLogger().setLevel(getattr(logging, args.log_level))
    
    if not MCP_AVAILABLE:
        print("Error: MCP package not installed.", file=sys.stderr)
        print("Install with: uv pip install mcp", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Create and run server
        server = OpenManusMCPServer()
        server.run(transport=args.transport)
    except KeyboardInterrupt:
        logger.info("Server interrupted by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
