# Claude Yahoo Finance MCP Agent

This project includes a console-based Claude agent that uses the Yahoo Finance
MCP server to answer questions about stock prices, company information,
historical data, fundamentals, financial statements, analyst recommendations,
company news, and historical market data.

## Setup

1. Install [uv](https://docs.astral.sh/uv/) and Python 3.13 or newer.
2. From this directory, install the project dependencies:

   ```powershell
   uv sync
   ```

3. Authenticate with Claude Code/Claude Agent SDK, or set `ANTHROPIC_API_KEY`
   in your environment or in a `.env` file in this directory:

   ```text
   ANTHROPIC_API_KEY=your-key
   ```

## Run

Start the agent from this directory:

```powershell
uv run agent.py
```

The Claude Agent SDK starts the Yahoo Finance MCP server as a subprocess and
uses the project's finance instructions as the agent's system prompt. The
conversation stays in one Claude session, and the agent can call the finance
MCP tools as needed. Enter `exit`, `quit`, or `bye` to stop.

Yahoo Finance data may be delayed or incomplete. The agent's instructions
require it to distinguish returned data from calculations and avoid
personalized investment advice.
