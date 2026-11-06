import json
from typing import Any, cast
try:
    import yfinance as yf  # type: ignore[reportMissingTypeStubs]
except ImportError:
    raise ImportError("Please install yfinance using 'pip install yfinance'.")

class YahooFinanceTool:
    @staticmethod
    def get_current_price(symbol: str) -> str:
        """
        Use this function to get the current stock price for a given ticker symbol.

        Args:
            symbol (str): The ticker symbol of the stock (e.g., 'AAPL' for Apple).
        
        Returns:
            str: The current stock price as a string or error message.
        """
        try:
            stock = yf.Ticker(symbol)
            current_price = stock.info.get("regularMarketPrice", stock.info.get("currentPrice"), stock.info.get('currency', 'USD'))
            #current_price = stock.info.get("currentPrice")
            return f"{current_price:.4f} {stock.info.get('currency', 'USD')}" if current_price is not None else "Price not available"
        except Exception as e:
            return f"Error fetching stock price for {symbol}: {e}"

    @staticmethod
    def get_company_info(symbol: str) -> str:
        """
        Use this function to get company information and overviewfor a given ticker symbol.

        Args:
            symbol (str): The ticker symbol of the stock (e.g., 'AAPL' for Apple).
        Returns:
            str: A JSON string containing company information or an error message.
        """
        try:
            company_info_full = yf.Ticker(symbol).info
            if company_info_full is None:
                return f"Error: No company information available for {symbol}"

            company_info_cleaned = {
                "Name": company_info_full.get("shortName"),
                "Symbol": company_info_full.get("symbol"),
                "Current Price": f"{company_info_full.get('regularMarketPrice', company_info_full.get('currentPrice'))}{company_info_full.get('currency', 'USD')}",
                "Market Cap": f"{company_info_full.get('marketCap', company_info_full.get('enterpriseValue'))}{company_info_full.get('currency', 'USD')}",
                "Sector": company_info_full.get("sector"),
                "Industry": company_info_full.get("industry"),
                "Address": company_info_full.get("address1"),
                "City": company_info_full.get("city"),
                "State": company_info_full.get("state"),
                "Country": company_info_full.get("country"),
                "Zip": company_info_full.get("zip"),
                "EPS": company_info_full.get("trailingEps"),
                "P/E Ratio": company_info_full.get("trailingPE"),
                "52-Week Low": f"{company_info_full.get('fiftyTwoWeekLow')}{company_info_full.get('currency', 'USD')}",
                "52-Week High": f"{company_info_full.get('fiftyTwoWeekHigh')}{company_info_full.get('currency', 'USD')}",
                "50 Day Average": f"{company_info_full.get('fiftyDayAverage')}{company_info_full.get('currency', 'USD')}",
                "200 Day Average": f"{company_info_full.get('twoHundredDayAverage')}{company_info_full.get('currency', 'USD')}",
                "Website": company_info_full.get("website"),
                "Summary": company_info_full.get("longBusinessSummary"),
                "Analysts Recommendation": company_info_full.get("recommendationKey"),
                "Number of Analysts Opinions": company_info_full.get("numberOfAnalystOpinions"),
                "Employees": company_info_full.get("fullTimeEmployees"),
                "Total Cash": f"{company_info_full.get('totalCash', company_info_full.get('totalCashPerShare'))}{company_info_full.get('currency', 'USD')}",
                "Free Cash Flow": f"{company_info_full.get('freeCashflow')}{company_info_full.get('currency', 'USD')}",
                "Operating Cash Flow": f"{company_info_full.get('operatingCashflow')}{company_info_full.get('currency', 'USD')}",
                "EBITDA": f"{company_info_full.get('ebitda')}{company_info_full.get('currency', 'USD')}",
                "Revenue": f"{company_info_full.get('totalRevenue')}{company_info_full.get  ('currency', 'USD')}",
                "Revenue Growth": f"{company_info_full.get('revenueGrowth') * 100:.2f}%" if company_info_full.get('revenueGrowth') is not None else None,
                "Gross Margins": f"{company_info_full.get('grossMargins') * 100:.2f}%" if company_info_full.get('grossMargins') is not None else None,
                "Ebita Margins": f"{company_info_full.get('ebitdaMargins') * 100:.2f}%" if company_info_full.get('ebitdaMargins') is not None else None,
            }
            return json.dumps(company_info_cleaned, indent=4)
        except Exception as e:
            return f"Error fetching company info for {symbol}: {e}"

    @staticmethod
    def get_historical_stock_prices(symbol: str, period: str = "1mo", interval: str = "1d") -> str:
        """
        Use this function to get historical stock price for a given ticker symbol.

        Args:
            symbol (str): The ticker symbol of the stock (e.g., 'AAPL' for Apple).
            period (str): The period for historical data 
                        Valid periods: '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max').
            interval (str): The interval between data points. Defaults to "1d"
                        Valid intervals: '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'.
        
        Returns:
            str: The current stock price or an error message.
        """
        try:
            stock = yf.Ticker(symbol)
            historical_price = stock.history(period=period, interval=interval)
            return historical_price.to_json(orient="index", date_format="iso")
        except Exception as e:
            return f"Error fetching historical stock prices for {symbol}: {e}"

    @staticmethod
    def get_stock_fundamentals(symbol: str) -> str:
        """
        Use this function to get fundamental data for a given ticker symbol.

        Args:
            symbol (str): The ticker symbol of the stock (e.g., 'AAPL' for Apple).

        Returns:
            str: A JSON string containing fundamental data or an error message.
                Keys:
                    - "symbol": The ticker symbol of the stock.
                    - "company_name": The long name of the company.
                    - "sector": The sector of the company.
                    - "industry": The industry of the company.
                    - "market_cap": The market capitalization of the company.
                    - "enterprise_value": The enterprise value of the company.
                    - "trailing_pe": The trailing P/E ratio of the company.
                    - "pe_ratio": The forward P/E ratio of the company.
                    - "pb_ratio": The Price/Book ratio of the company.
                    - "dividend_yield": The dividend yield of the company.
                    - "eps": The earnings per share of the company.
                    - "beta": The beta of the company.
                    - "52_week_high": The 52-week high price of the company.
                    - "52_week_low": The 52-week low price of the company.
                    - "peg_ratio": The PEG ratio of the company.
                    - "price_sales": The Price/Sales ratio of the company.
                    - "price_book": The Price/Book ratio of the company.
                    - "enterprise_value_revenue": The Enterprise Value/Revenue ratio of the company.
                    - "enterprise_value_ebitda": The Enterprise Value/EBITDA ratio of the company.
                    - "buffett_indicator": The Buffett Indicator of the company.
        """
        try:
            stock = yf.Ticker(symbol)
            info = stock.info
            if info is None:
                return f"Error: No fundamental data available for {symbol}"

            fundamentals = {
                "symbol": symbol,
                "company_name": info.get("longName", ""),
                "sector": info.get("sector", ""),
                "industry": info.get("industry", ""),
                "market_cap": info.get("marketCap", "N/A"),
                "enterprise_value": info.get("enterpriseValue", "N/A"),
                "trailing_pe": info.get("trailingPE", "N/A"),
                "pe_ratio": info.get("forwardPE", "N/A"),
                "pb_ratio": info.get("priceToBook", "N/A"),
                "dividend_yield": info.get("dividendYield", "N/A"),
                "eps": info.get("trailingEps", "N/A"),
                "beta": info.get("beta", "N/A"),
                "52_week_high": info.get("fiftyTwoWeekHigh", "N/A"),
                "52_week_low": info.get("fiftyTwoWeekLow", "N/A"),
                "peg_ratio": info.get("pegRatio", "N/A"),
                "price_sales": info.get("priceToSalesTrailing12Months", "N/A"),
                "price_book": info.get("priceToBook", "N/A"),
                "enterprise_value_revenue": info.get("enterpriseToRevenue", "N/A"),
                "enterprise_value_ebitda": info.get("enterpriseToEbitda", "N/A"),
                "buffett_indicator": info.get("buffettIndicator", "N/A")
            }
            return json.dumps(fundamentals, indent=4)
        except Exception as e:
            return f"Error fetching stock fundamentals for {symbol}: {e}"

    @staticmethod
    def get_income_statements(symbol: str) -> str:
        """
        Use this function to get income statement data for a given ticker symbol.

        Args:
            symbol (str): The ticker symbol of the stock (e.g., 'AAPL' for Apple).
            
        Returns:
            str: A JSON string containing income statement data or an error message.
        """
        try:
            stock = yf.Ticker(symbol)
            financials = stock.financials
            if financials.empty:
                return f"No income statement data available for {symbol}"

            return financials.to_json(orient="index", date_format="iso")
        except Exception as e:
            return f"Error fetching income statement data for {symbol}: {e}"

    @staticmethod
    def get_key_financial_ratios(symbol: str) -> str:
        """
        Use this function to get key financial ratios for a given ticker symbol.

        Args:
            symbol (str): The ticker symbol of the stock (e.g., 'AAPL' for Apple).
            
        Returns:
            str: A JSON string containing key financial ratios or an error message.
        """
        try:
            stock = yf.Ticker(symbol)
            key_ratios = stock.info
            if key_ratios is None:
                return f"Error: No fundamental data available for {symbol}"
            return json.dumps(key_ratios, indent=4)
        except Exception as e:
            return f"Error fetching key financial ratios for {symbol}: {e}"

    @staticmethod
    def get_analyst_recommendations(symbol: str) -> str:
        """
        Use this function to get analyst recommendations for a given ticker symbol.

        Args:
            symbol (str): The ticker symbol of the stock (e.g., 'AAPL' for Apple).
        Returns:
            str: A JSON string containing analyst recommendations or an error message.
        """
        try:
            stock = yf.Ticker(symbol)
            recommendations = stock.recommendations
            if recommendations is None or recommendations.empty:
                return f"No analyst recommendations available for {symbol}"

            return recommendations.to_json(orient="index", date_format="iso")
        except Exception as e:
            return f"Error fetching analyst recommendations for {symbol}: {e}"

    @staticmethod
    def get_company_news(symbol: str, num_stories: int = 5) -> str:
        """
        Use this function to get recent news articles for a given ticker symbol.

        Args:
            symbol (str): The ticker symbol of the stock (e.g., 'AAPL' for Apple).
            num_stories (int): The number of news stories to retrieve. Defaults to 5.
        Returns:
            str: A JSON string containing recent news articles or an error message.
        """
        try:
            stock = yf.Ticker(symbol)
            news = stock.news
            if news is None or len(news) == 0:
                return f"No news articles available for {symbol}"

            # Limit the number of stories to the specified num_stories
            limited_news = news[:num_stories]
            return json.dumps(limited_news, indent=4)
        except Exception as e:
            return f"Error fetching company news for {symbol}: {e}"

    @staticmethod
    def get_technical_indicators(symbol: str, period: str = "3mo") -> str:
        """
        Use this function to get technical indicators for a given ticker symbol.

        Args:
            symbol (str): The ticker symbol of the stock (e.g., 'AAPL' for Apple).
            period (str): The period for historical data 
                        Valid periods: '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max').        
        Returns:
            str: A JSON string containing technical indicators or an error message.
        """
        try:
            stock = yf.Ticker(symbol)
            indicators = stock.history(period=period)
            if indicators.empty:
                return f"No indicator available for {symbol}"
            return indicators.to_json(orient="index", date_format="iso")
        except Exception as e:
            return f"Error fetching technical indicators for {symbol}: {e}"