@echo off
REM OpenManus MCP Server Setup Script
REM This script sets up the UV environment and installs dependencies

echo OpenManus MCP Server Setup
echo ========================
echo.

REM Check if uv is installed
uv --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: UV is not installed or not in PATH
    echo Please install UV first: https://docs.astral.sh/uv/getting-started/installation/
    pause
    exit /b 1
)

echo UV is installed: 
uv --version
echo.

REM Create virtual environment if it doesn't exist
if not exist ".venv" (
    echo Creating virtual environment...
    uv venv --python 3.11
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo Virtual environment created successfully.
    echo.
) else (
    echo Virtual environment already exists.
    echo.
)

REM Activate the virtual environment and install dependencies
echo Activating virtual environment and installing dependencies...
call .venv\Scripts\activate.bat

if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Install dependencies
echo Installing dependencies from requirements-mcp.txt...
uv pip install -r requirements-mcp.txt

if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    echo Please check requirements.txt and try again
    pause
    exit /b 1
)

REM Test the MCP server
echo.
echo Testing MCP server...
python mcp_server_simple.py --help

if errorlevel 1 (
    echo ERROR: MCP server test failed
    echo Please check the error messages above
    pause
    exit /b 1
)

echo.
echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo Next steps:
echo 1. Use start.bat to run the MCP server
echo 2. Configure Warp with the JSON from warp-mcp-config.json
echo.
echo Available tools:
echo   - bash (shell commands)
echo   - browser (web automation)  
echo   - file_ops (file operations)
echo   - editor (text editing)
echo   - python (code execution)
echo   - web_search (web searching)
echo   - terminate (process control)
echo.
pause
