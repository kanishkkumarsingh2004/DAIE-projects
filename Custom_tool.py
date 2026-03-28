import asyncio
from daie import Agent, AgentConfig, set_llm
from daie.agents import AgentRole
from daie.tools import FileManagerTool, APICallTool, tool

set_llm(ollama_llm="llama3.2:1b", stream=True)


# Custom tool via decorator
@tool(name="calculate_math", description="Evaluate a basic math expression.")
async def calculate_math(expression: str) -> str:
    return str(eval(expression))

async def main():
    agent = Agent(config=AgentConfig(
        name="MathBot",
        role=AgentRole.GENERAL_PURPOSE,
        system_prompt="You are a capable agent with access to math and file tools.",
    ))

    agent.add_tool(calculate_math)
    agent.add_tool(FileManagerTool())

    await agent.start()

    # LLM autonomously picks the right tools via the ReAct loop
    result = await agent.execute_task(
        "Calculate 25 * 14 and save the result into a file called result.txt"
    )
    print("Final Answer:", result)

    await agent.stop()

asyncio.run(main())