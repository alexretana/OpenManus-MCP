# 🚀 OpenManus-MCP Tools Tutorial Guide

A comprehensive guide to using all the powerful automation tools available through the OpenManus Model Context Protocol (MCP) server.

---

## 🌐 **Browser Automation (`browser_use`)**

The crown jewel of OpenManus-MCP is its sophisticated browser automation system built on Playwright and browser-use.

### **What OpenManus Had Set Up:**

1. **🎯 Persistent Browser Sessions** - Maintains browser state across multiple commands
2. **📸 Screenshot Capture** - Automatically takes screenshots for visual context  
3. **🔍 DOM Element Detection** - Intelligent element indexing for precise interaction
4. **🤖 AI-Powered Content Extraction** - Uses LLM to extract structured data from web pages
5. **🔗 Integrated Web Search** - Combines search with navigation
6. **📱 Tab Management** - Full multi-tab browsing support

### **Available Browser Actions:**

#### **🔗 Navigation Actions**
```bash
# Navigate to a website
browser_use(action="go_to_url", url="https://example.com")

# Go back to previous page  
browser_use(action="go_back")

# Refresh current page
browser_use(action="refresh")

# Search the web and navigate to first result
browser_use(action="web_search", query="OpenAI GPT-4")
```

#### **🖱️ Element Interaction**
```bash
# Click on an element by index (from browser state)
browser_use(action="click_element", index=5)

# Type text into a form field
browser_use(action="input_text", index=3, text="your@email.com")

# Send keyboard commands
browser_use(action="send_keys", keys="Enter")
browser_use(action="send_keys", keys="Tab")
```

#### **📜 Scrolling & Navigation**
```bash
# Scroll down by pixels
browser_use(action="scroll_down", scroll_amount=500)

# Scroll up  
browser_use(action="scroll_up", scroll_amount=300)

# Scroll to specific text
browser_use(action="scroll_to_text", text="Contact Us")
```

#### **📋 Dropdown Management**
```bash
# Get all options from a dropdown
browser_use(action="get_dropdown_options", index=7)

# Select a specific option
browser_use(action="select_dropdown_option", index=7, text="United States")
```

#### **🤖 AI Content Extraction**
```bash
# Extract structured information using AI
browser_use(action="extract_content", goal="Find all product prices and names")

# Extract contact information
browser_use(action="extract_content", goal="Get email addresses and phone numbers")

# Summarize article content
browser_use(action="extract_content", goal="Summarize the main points of this article")
```

#### **🔄 Tab Management**
```bash
# Open new tab with URL
browser_use(action="open_tab", url="https://github.com")

# Switch to tab by ID
browser_use(action="switch_tab", tab_id=2)

# Close current tab
browser_use(action="close_tab")
```

#### **⏱️ Utility Actions**
```bash
# Wait for page to load
browser_use(action="wait", seconds=3)
```

### **🎯 Advanced Browser Workflows**

**Example: E-commerce Price Comparison**
```bash
1. browser_use(action="go_to_url", url="https://amazon.com")
2. browser_use(action="input_text", index=1, text="iPhone 15")
3. browser_use(action="send_keys", keys="Enter")
4. browser_use(action="wait", seconds=2)
5. browser_use(action="extract_content", goal="Extract product names, prices, and ratings")
```

**Example: Form Automation**
```bash
1. browser_use(action="go_to_url", url="https://forms.example.com")
2. browser_use(action="input_text", index=1, text="John Doe")
3. browser_use(action="input_text", index=2, text="john@example.com")
4. browser_use(action="select_dropdown_option", index=3, text="Software Engineer")
5. browser_use(action="click_element", index=10)  # Submit button
```

---

## 💻 **Shell Command Execution (`bash`)**

Execute shell commands with persistent session management.

### **Features:**
- **Persistent Session** - Commands remember previous state
- **Background Processes** - Support for long-running commands
- **Timeout Protection** - Prevents hanging commands
- **Interactive Support** - Handle interactive processes

### **Usage Examples:**
```bash
# Basic commands
bash(command="ls -la")
bash(command="pwd")

# Chain commands (session persists)
bash(command="cd /projects")
bash(command="ls")  # Will list contents of /projects

# Background processes
bash(command="python server.py > server.log 2>&1 &")

# Interactive processes
bash(command="python script.py")
# If returns exit code -1, send more input:
bash(command="y")  # Respond to prompt

# Interrupt hanging process
bash(command="ctrl+c")
```

---

## 📝 **Advanced Text Editing (`str_replace_editor`)**

Sophisticated file editing with precision string replacement and undo functionality.

### **Available Commands:**

#### **📖 View Files**
```bash
# View entire file
str_replace_editor(command="view", path="/path/to/file.py")

# View specific line range
str_replace_editor(command="view", path="/path/to/file.py", view_range=[10, 20])

# View from line to end
str_replace_editor(command="view", path="/path/to/file.py", view_range=[15, -1])

# View directory contents
str_replace_editor(command="view", path="/path/to/directory")
```

#### **✨ Create Files**
```bash
str_replace_editor(command="create", path="/path/to/new_file.py", 
                  file_text="print('Hello, World!')")
```

#### **🔄 Precise String Replacement**
```bash
# Replace exact text
str_replace_editor(command="str_replace", 
                  path="/path/to/file.py",
                  old_str="def old_function():",
                  new_str="def new_function():")

# Delete text (empty new_str)
str_replace_editor(command="str_replace", 
                  path="/path/to/file.py",
                  old_str="# TODO: Remove this",
                  new_str="")
```

#### **➕ Insert Text**
```bash
# Insert after specific line
str_replace_editor(command="insert", 
                  path="/path/to/file.py",
                  insert_line=10,
                  new_str="    # New comment here")
```

#### **↩️ Undo Changes**
```bash
str_replace_editor(command="undo_edit", path="/path/to/file.py")
```

---

## 🐍 **Python Code Execution (`python`)**

Execute Python code safely with timeout protection and output capture.

### **Features:**
- **Process Isolation** - Code runs in separate process
- **Timeout Protection** - 5-second default timeout
- **Output Capture** - See all print statements
- **Error Handling** - Detailed error messages

### **Usage Examples:**
```bash
# Basic computation
python(code="print(2 + 2)")

# Data analysis
python(code="""
import pandas as pd
data = {'name': ['Alice', 'Bob'], 'age': [25, 30]}
df = pd.DataFrame(data)
print(df)
""")

# File processing
python(code="""
with open('data.txt', 'r') as f:
    content = f.read()
    word_count = len(content.split())
    print(f'Word count: {word_count}')
""")

# Mathematical calculations
python(code="""
import math
result = math.sqrt(16) + math.pi
print(f'Result: {result:.2f}')
""")
```

---

## 📁 **Comprehensive File Operations (`file_ops`)**

Advanced file and directory management beyond basic editing.

### **Available Operations:**

#### **📂 Directory Operations**
```bash
# List directory contents
file_ops(operation="list_directory", path="/path/to/dir")

# List recursively with hidden files
file_ops(operation="list_directory", path="/path/to/dir", 
         recursive=true, show_hidden=true)

# Create directory
file_ops(operation="create_directory", path="/new/directory")

# Create directory with parents
file_ops(operation="create_directory", path="/deep/nested/dir", recursive=true)
```

#### **📄 File Operations**
```bash
# Copy file
file_ops(operation="copy_file", 
         path="/source/file.txt", 
         destination="/dest/file.txt")

# Move file
file_ops(operation="move_file", 
         path="/old/location.txt", 
         destination="/new/location.txt")

# Delete file
file_ops(operation="delete_file", path="/unwanted/file.txt")
```

#### **📊 Information & Analysis**
```bash
# Get detailed file info
file_ops(operation="get_file_info", path="/path/to/file.txt")

# Get file size
file_ops(operation="get_file_size", path="/large/file.zip")

# Get directory size
file_ops(operation="get_directory_size", path="/project/folder")
```

#### **🔍 Search Operations**
```bash
# Find Python files
file_ops(operation="find_files", path="/project", 
         pattern="*.py", recursive=true)

# Find configuration files
file_ops(operation="find_files", path="/app", pattern="*.config")
```

#### **🔐 Permissions**
```bash
# Change file permissions
file_ops(operation="change_permissions", path="/script.sh", permissions="755")
```

---

## 🔍 **Web Search (`web_search`)**

Multi-engine web searching with content fetching and structured results.

### **Features:**
- **Multi-Engine Support** - Google, Bing, DuckDuckGo, Baidu
- **Automatic Fallback** - Tries multiple engines if one fails
- **Content Fetching** - Can retrieve full page content
- **Structured Results** - Organized search results with metadata

### **Usage Examples:**
```bash
# Basic search
web_search(query="Python asyncio tutorial")

# Search with more results
web_search(query="machine learning algorithms", num_results=10)

# Search with content fetching
web_search(query="latest AI news", fetch_content=true, num_results=3)

# Targeted search
web_search(query="OpenAI GPT-4 API documentation", 
          lang="en", country="us")
```

---

## 🛑 **Process Control (`terminate`)**

Clean process termination and resource management.

### **Usage:**
```bash
# Terminate current processes and cleanup
terminate()
```

---

## 🎯 **Real-World Workflow Examples**

### **📊 Web Data Collection Workflow**
```bash
1. web_search(query="top tech companies 2024", num_results=5)
2. browser_use(action="go_to_url", url="https://first-result-url.com")
3. browser_use(action="extract_content", goal="Extract company names and valuations")
4. str_replace_editor(command="create", path="/data/companies.json", file_text="extracted_data")
5. python(code="import json; data = json.load(open('/data/companies.json')); print(len(data))")
```

### **🔧 Code Analysis Workflow**
```bash
1. file_ops(operation="find_files", path="/project", pattern="*.py", recursive=true)
2. str_replace_editor(command="view", path="/project/main.py")
3. python(code="import ast; # Analyze code structure")
4. str_replace_editor(command="str_replace", path="/project/main.py", 
                     old_str="old_pattern", new_str="new_pattern")
```

### **📋 Form Automation Workflow**
```bash
1. browser_use(action="go_to_url", url="https://application-form.com")
2. browser_use(action="input_text", index=1, text="Application Data")
3. file_ops(operation="get_file_info", path="/uploads/resume.pdf")
4. browser_use(action="click_element", index=5)  # Upload button
5. browser_use(action="extract_content", goal="Confirm form submission")
```

---

## ⚡ **Pro Tips**

1. **🔄 Chain Commands** - Use bash's persistent session for complex operations
2. **📸 Visual Context** - Browser screenshots help understand current state  
3. **🎯 Specific Goals** - Be precise with extract_content goals for better results
4. **⚡ Error Handling** - All tools return structured error messages
5. **🧹 Resource Management** - Use terminate() to clean up when done
6. **📝 Undo Support** - str_replace_editor supports undo for safety
7. **🔍 Smart Search** - Combine web_search with browser automation for comprehensive data gathering

---

## 🚨 **Safety Features**

- **⏱️ Timeout Protection** - All long-running operations have timeouts
- **🔒 Process Isolation** - Python code runs in separate processes
- **💾 Undo Support** - File operations can be reversed
- **🧹 Automatic Cleanup** - Browser resources are automatically managed
- **📊 Error Reporting** - Comprehensive error messages and logging

---

## 🎮 **Getting Started**

1. **Start the MCP Server** - Run `start.bat` or configure in Warp
2. **Explore with Simple Commands** - Try `bash(command="pwd")` to test
3. **Navigate the Web** - Use `browser_use(action="go_to_url", url="...")` 
4. **Extract Data** - Combine browser automation with content extraction
5. **Automate Workflows** - Chain multiple tools for complex tasks

The OpenManus-MCP tools provide a comprehensive automation platform that rivals commercial RPA solutions, all through a simple AI-accessible interface! 🚀
