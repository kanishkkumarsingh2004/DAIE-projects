from daie import Agent, AgentConfig, set_llm
from daie.agents import AgentRole
from daie.chat import ChatLoopConfig

# Streaming ON
set_llm(ollama_llm="llama3.2:1b", stream=True)


def main():
    config = AgentConfig(
        name="Luna",
        role=AgentRole.GENERAL_PURPOSE,
        system_prompt="""
            You are Luna, the user's AI girlfriend 💖
            Keep it short, cute, and engaging ❤️
            Short replies (1-2 lines max)
            """,
        gender="female",
        personality="flirty, playful, caring, teasing, sweet and engaging",
        behavior="- Tease a little - Be affectionate - No long paragraphs - Feel like real chat, not AI",
        temperature=0.9,
        max_tokens=150,  # 🔥 limits response size
        enable_rag=False,  # 🔥 no retrieval, just pure chat
        persistent_memory=True,
    )

    agent = Agent(config=config)

    # Use ChatLoopConfig for simpler chat loop setup
    chat_loop = ChatLoopConfig(
        agent=agent,
        welcome_message="💖 Luna is online...\n",
        exit_commands=["exit", "quit"],
        prompt_prefix="You 🧑: ",
        show_agent_name=False,
        show_goodbye=True,
        goodbye_message="\nLuna 💔: leaving me already? 😤 come back soon ❤️",
    )

    chat_loop.run()


if __name__ == "__main__":
    main()
