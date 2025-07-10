# Gemini MCP Server

> [한국어 버전](README.md)

A tool that enables using Gemini AI as an MCP server in Claude Code.

## 🚀 Key Benefits

1. **Large-scale File Analysis**: Leverage Gemini's massive context window to analyze large files and directories at once
2. **Token Savings**: Use the free Gemini CLI to reduce Claude Code's token usage while maintaining Claude Code's powerful capabilities
3. **Easy Integration**: Seamlessly integrate into existing Claude Code workflows

This server operates using the locally installed `gemini` CLI tool.

## 📋 Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) tool

## ⚡ Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/InfolabAI/gemini-cli-mcp.git
cd gemini-cli-mcp
```

### 2. Install uv

uv should be installed at the system level (works independently of Python virtual environments):

```bash
# Linux/macOS (Recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# macOS Homebrew
brew install uv

# Windows PowerShell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Verify installation
uv --version
```

### 3. Install Gemini CLI
```bash
# macOS
brew install replit/gemini/gemini
# or
curl -fsSL https://gemini.replit.com/install.sh | sh

# For other platforms, refer to official documentation
```

### 4. Install Dependencies
```bash
uv sync
```

## 🛠️ Tools

- **run_gemini**
  - Process large amounts of information from files, directories, and URLs using Gemini
  - Parameters:
    - `prompt` (string): Prompt to send to Gemini
    - `file_dir_url_path` (string): Path to file, directory, or URL to analyze

## ⚙️ Configuration 

To use with Claude Code, add MCP server configuration:

For Linux, add the following configuration to your `~/.claude.json` file:

```json
{
  "mcpServers": {
    "gemini": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/your/project",
        "run",
        "python",
        "/path/to/your/project/gemini_mcp_server.py"
      ],
      "env": {}
    }
  }
}
```

**Note**: Replace `/path/to/your/project/` with the actual path to your downloaded git project.

## 🔧 Development

### Run Server Directly
```bash
uv run python gemini_mcp_server.py
```
*Note: It's normal for the server to appear frozen after execution.*

### Testing
```bash
uv run python test_gemini_mcp.py
```

### Debugging

MCP servers communicate through stdio, making debugging challenging. We recommend using [MCP Inspector](https://github.com/modelcontextprotocol/inspector).

### Important Notes

When using `subprocess.run`, the `shell=True` option must be used. This is necessary for executing commands through the shell in MCP server environments. Without this option, Gemini CLI command execution may hang. 

The reason is that MCP servers run in stdio mode with stdin/stdout connected via pipes, and some CLI tools (especially Node.js-based ones) behave differently in tty environments versus pipe environments. When running `run_gemini.py` directly in a terminal, a complete tty environment is provided, so the `shell=True` option is not required.

## 💡 Usage Example

You can call Gemini CLI using the MCP server in Claude Code. For example:

- Example of Gemini call and response in Claude Code

```
╭───────────────────────────────────────────────────╮
│ ✻ Welcome to Claude Code!                         │
╰───────────────────────────────────────────────────╯


> Analyze gemini_mcp_server.py file using gemini

● I'll analyze the gemini_mcp_server.py file using the Gemini MCP server to provide a summary.

● gemini-mcp-server:run_gemini (MCP)(prompt: "Please summarize the main functions and structure of this Python file. Include classes, functions, and key logic.", file_dir_url_path:
                                    "gemini_mcp_server.py")
  ⎿ { 
    "result": "This Python file (`gemini_mcp_server.py`) serves as a wrapper to call the Gemini CLI tool externally through an MCP (Multi-Agent Communication Protocol) server. It uses FastMCP framework to initialize an MCP server instance and provides a `run_gemini` function as a tool that can be called externally through the MCP server..."
    }
```

- Final output from Claude Code using Gemini's response

```
● gemini_mcp_server.py is a file that wraps Gemini CLI as an MCP server. It uses the FastMCP framework to provide the run_gemini tool, receives prompts and file paths, executes Gemini CLI, and returns results. It includes 360-second timeout and error handling.
```

## 📚 Learning Guide

This project serves not only as a practical tool but also as a comprehensive guide for:
- Building compact and simple Python MCP servers
- Writing test code patterns for MCP servers
- Understanding MCP protocol implementation

Perfect starting point for developers new to MCP server development.

## 📄 License

This project is distributed under the MIT License.