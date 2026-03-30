# 🟢 Beginner - Chat Loop Config Example
# Difficulty: Beginner
# This example demonstrates how to use ChatLoopConfig to quickly set up
# a chat loop without writing the full boilerplate code.

from daie import Agent, AgentConfig, set_llm
from daie.agents import AgentRole
from daie.chat import ChatLoopConfig

# Configure LLM globally
set_llm(ollama_llm="llama3.2:1b", stream=True)

"""
Simplest way to create a chat loop.
Just create an agent and pass it to ChatLoopConfig!
"""
config = AgentConfig(
    name="LUNA",
    role=AgentRole.GENERAL_PURPOSE,
    system_prompt="You are a helpful and concise AI assistant.",
    personality="friendly and helpful"
)
agent = Agent(config=config)

# One-liner to start chat!
ChatLoopConfig.quick_start(agent).run()

