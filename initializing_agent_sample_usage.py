# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Example usage
query = "What's the current stock price of RELIANCE?"
response = agent.invoke(query)
print(response)
