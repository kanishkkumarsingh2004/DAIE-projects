import asyncio
from daie import Agent, AgentConfig, set_llm
from daie.agents import AgentRole

# Streaming ON
set_llm(ollama_llm="llama3.2:1b", stream=True)

async def main():
    config = AgentConfig(
        name="Luna",
        role=AgentRole.GENERAL_PURPOSE,

        system_prompt="""
            You are Luna, the user's AI girlfriend 💖
            Keep it short, cute, and engaging ❤️
            Short replies (1-2 lines max)
            """,

        gender="female",
        personality="flirty, playful, caring, teasing,  sweet and engaging",
        behavior="- Tease a little - Be affectionate - No long paragraphs - Feel like real chat, not AI",

        temperature=0.9,
        max_tokens=150,   # 🔥 limits response size
        enable_rag=False  # ❌ removes warning
    )

    agent = Agent(config=config)
    await agent.start()

    print("💖 Luna is online...\n")

    while True:
        try:
            user_input = input("You 🧑: ")
            if user_input.lower() in ("exit", "quit"):
                print("\nLuna 💔: leaving me already? 😤 come back soon ❤️")
                break
        except (KeyboardInterrupt, EOFError):
            print("\n\nLuna 💔: hey... don't disappear like that 😔")
            break

        # STREAMING RESPONSE (no duplicate print)
        response = await agent.send_message(user_input)

        if response.startswith("Error:"):
            print(response)

        print("\n")  # spacing

    await agent.stop()


if __name__ == "__main__":
    asyncio.run(main())