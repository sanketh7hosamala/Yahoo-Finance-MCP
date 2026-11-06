from mcp.server.mcpserver import MCPServer
from tools.yahoo_finance_tool import YahooFinanceTool
import re
import os

# Suppress MCP INFO logs to reduce console output
import logging
logging.getLogger("mcp").setLevel(logging.WARNING)

mcp = MCPServer(
    name="Yahoo-Finance-Tools",
    dependencies=['yfinance'],
)

# Create prompt
@mcp.prompt()
def system_prompt() -> str:
    """Instructions for Yahoo Finance agent"""
    script_dir = os.path.dirname(__file__)
    prompt_path = os.path.join(script_dir, "prompts", "system_instructions.md")
    with open(prompt_path, "r") as file:
        return file.read()

# tools for Yahoo Finance
mcp.add_tool(
    fn=YahooFinanceTool.get_current_price,
    name='Finance-Get-Current-Stock-Price',
    description='Get the current stock price for a given ticker symbol.',
    )

mcp.add_tool(
    fn=YahooFinanceTool.get_company_info,
    name='Finance-Get-Company-Info',
    description='Get company information and overview for a given ticker symbol.',
    )

mcp.add_tool(
    fn=YahooFinanceTool.get_historical_stock_prices,
    name='Finance-Get-Historical-Stock-Prices',
    description='Get historical stock price data for a given ticker symbol over a specified period.',
    )

mcp.add_tool(
    fn=YahooFinanceTool.get_stock_fundamentals,
    name='Finance-Get-Stock-Fundamentals',
    description='Get fundamental financial data for a given ticker symbol.',
    )

mcp.add_tool(
    fn=YahooFinanceTool.get_income_statements,
    name='Finance-Get-Income-Statements',
    description='Get the income statement for a given ticker symbol.',
    )

mcp.add_tool(
    fn=YahooFinanceTool.get_key_financial_ratios,
    name='Finance-Get-Key-Financial-Ratios',
    description='Get key financial ratios for a given ticker symbol.',
    )

mcp.add_tool(
    fn=YahooFinanceTool.get_analyst_recommendations,
    name='Finance-Get-Analyst-Recommendations',
    description='Get analyst recommendations for a given ticker symbol.',
    )

mcp.add_tool(
    fn=YahooFinanceTool.get_company_news,
    name='Finance-Get-Company-News',
    description='Get the latest news articles related to a given ticker symbol.',
    )

mcp.add_tool(
    fn=YahooFinanceTool.get_technical_indicators,
    name='Finance-Get-Technical-Indicators',
    description='Get technical indicators for a given ticker symbol.',
    )

if __name__ == "__main__":
    mcp.run(transport='stdio')