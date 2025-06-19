import yfinance as yf
from langchain.agents import Tool, initialize_agent, AgentType
from langchain_openai import ChatOpenAI

# Initialize the language model
llm = ChatOpenAI(temperature=0)

# Define the function to get stock price
def get_stock_price(symbol: str) -> str:
    # Append .NS for Indian stocks (NSE)
    symbol = symbol.upper().strip()
    full_symbol = f"{symbol}.NS"

    try:
        ticker = yf.Ticker(full_symbol)
        data = ticker.history(period="1d")
        if data.empty:
            return f"Could not fetch stock data for {symbol}. Please check the symbol."
        price = data['Close'].iloc[-1]
        return f"The current stock price of {symbol} is ₹{price:.2f}"
    except Exception as e:
        return f"Error retrieving stock data: {e}"

# Create a tool for the agent to use
tools = [
    Tool(
        name="StockPrice",
        func=get_stock_price,
        description="Useful for getting the stock price of an Indian company. Input should be the stock symbol (e.g., RELIANCE)."
    )
]

