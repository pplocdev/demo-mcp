# MCP Chatbot Project

This project includes a chatbot system with two main components: **MCP Server** and **MCP Client**. The client sends user queries to the server and receives responses.

## Project Structure

```
mcp-chatbot/
├── mcp-client/
│   ├── client.py
│   └── requirements.txt
├── mcp-server/
│   ├── server.py
│   └── requirements.txt
```

## Prerequisites

- Python 3.8 or higher
- [`uv`](https://github.com/astral-sh/uv) (used to run the client and manage dependencies)

Install `uv` globally if you haven't already:

```bash
pip install uv
```

## Installing Dependencies

Install dependencies separately for both the server and client:

### MCP Server

```bash
cd mcp-server
uv pip install -r requirements.txt
```

### MCP Client

```bash
cd ../mcp-client
uv pip install -r requirements.txt
```

## Running the MCP Client via Terminal

This guide explains how to run the MCP Client from the terminal to send queries to the chatbot.

### Steps

1. Navigate to the MCP Client directory:

   ```bash
   cd mcp-client
   ```

2. Run the client script with a reference to the server:

   ```bash
   python client.py ../mcp-server/server.py
   ```

   **Or**, if you're using `uv` to run the script:

   ```bash
   uv run client.py ../mcp-server/server.py
   ```

> **Note:** Ensure that the MCP Server is correctly set up and the path to the server file is valid.

## Features

- Accepts natural language queries from the user
- Sends queries to the MCP server
- Displays chatbot responses directly in the terminal

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
