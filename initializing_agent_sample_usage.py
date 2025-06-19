# Initialize the agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True)

# Example usage
query = "What's the current stock price of Apple?"
response = agent.invoke(query)
print(response)
