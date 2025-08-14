@echo off
REM OpenManus MCP Server Startup Script
REM This script activates the UV virtual environment and starts the MCP server

echo Starting OpenManus MCP Server...
echo.

REM Check if .venv directory exists
if not exist ".venv" (
    echo ERROR: Virtual environment not found at .venv
    echo Please create the virtual environment first with: uv venv
    pause
    exit /b 1
)

REM Check if activation script exists
if not exist ".venv\Scripts\activate.bat" (
    echo ERROR: Activation script not found at .venv\Scripts\activate.bat
    echo Please ensure the virtual environment is properly created
    pause
    exit /b 1
)

REM Activate the virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Check if activation was successful
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Check if MCP server script exists
if not exist "mcp_server_working.py" (
    echo ERROR: MCP server script not found: mcp_server_working.py
    pause
    exit /b 1
)

REM Start the MCP server
echo Starting MCP server...
echo Press Ctrl+C to stop the server
echo.
python mcp_server_working.py %*

REM If we get here, the server has stopped
echo.
echo MCP server stopped.
pause
