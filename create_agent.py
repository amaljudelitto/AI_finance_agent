import yfinance as yf
from langchain.agents import AgentType, Tool, initialize_agent
from langchain_openai import ChatOpenAI

# Initialize the language model
llm = ChatOpenAI(temperature=0)

# Define the function to get stock price
def get_stock_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return f"The current stock price of {symbol} is ${todays_data['Close'].iloc[-1]:.2f}"

# Create a tool for the agent to use
tools = [
    Tool(
        name="StockPrice",
        func=get_stock_price,
        description="Useful for getting the stock price of a company. The input should be the stock symbol of the company."
    )
]
