"""
Example 04: RAG-Powered Chat Agent
===================================
This example shows how to create an agent that uses Retrieval-Augmented
Generation (RAG) to answer questions based on your own documents (PDF, TXT).

Prerequisites:
  1. Place your documents (PDF/TXT) in a folder, e.g. ./my_documents/
  2. Install the RAG dependencies:
       pip install PyPDF2 sentence-transformers faiss-cpu
  3. Have an Ollama model running (e.g. llama3.2:1b)

⚠️  NOTE: The RAG pipeline (document loading, chunking, embedding, retrieval)
    is NOT yet implemented in the library. This example shows the intended API
    once built. See the TODO comments below for what needs to be added.
"""

import asyncio
import os
from daie import Agent, AgentConfig, set_llm
from daie.agents import AgentRole

# 1. Configure the LLM
set_llm(ollama_llm="llama3.2:1b", stream=True)

# 2. Path to your documents folder
DOCUMENTS_PATH = os.path.join(os.path.dirname(__file__), "data")


async def main():
    os.makedirs(DOCUMENTS_PATH, exist_ok=True)

    config = AgentConfig(
        name="NOVA",
        role=AgentRole.GENERAL_PURPOSE,
        system_prompt=(
            "You are a knowledgeable assistant. Use the provided document context "
            "to answer questions accurately. If the context doesn't contain the "
            "answer, say so honestly."
        ),
        personality="precise, helpful, and thorough",
        gender="female",
        behavior="always cites the source document chunk in your answer",
        temperature=0.3,       # Lower temperature for factual answers
        max_tokens=1024,
        # --- RAG configuration ---
        rag_document_path=DOCUMENTS_PATH,
        enable_rag=True,
    )

    agent = Agent(config=config)
    await agent.start()

    print("=== RAG Chat (Document-Powered) ===")
    print(f"📂 Documents loaded from: {DOCUMENTS_PATH}")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ("exit", "quit"):
                break
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            break

        # relevant document chunks and include them in the prompt
        response = await agent.send_message(user_input)

        if response.startswith("Error:"):
            print(response)

        print("\n")

    await agent.stop()


if __name__ == "__main__":
    asyncio.run(main())
