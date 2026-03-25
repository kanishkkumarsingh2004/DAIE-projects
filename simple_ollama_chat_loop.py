
#!/usr/bin/env python3
"""
DAIE Library Ollama Chat Loop Example

This script demonstrates a simple chat loop using the DAIE (Decentralized AI Ecosystem) library.
It creates an agent and provides an interactive chat interface for users to communicate with the agent.
"""

import asyncio
import logging
from daie.agents.agent import Agent
from daie.agents.config import AgentConfig, AgentRole
from daie import set_llm, LLMType

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

ollama_model_name = "llama3.2:1b" # Replace with your actual Ollama model name 

set_llm(ollama_llm=ollama_model_name, temperature=0.3, max_tokens=1500, llm_type=LLMType.OLLAMA, stream=True)

async def chat_with_agent(agent: Agent):
    """
    Main chat loop function that handles user input and displays agent responses.
    """
    print(f"Connected to {agent.name}! Type 'quit' or 'exit' to end the chat.")
    print("=" * 50)
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check if user wants to quit
            if user_input.lower() in ["quit", "exit", "q"]:
                print(f"\n{agent.name}: Goodbye!")
                break
            
            if not user_input:
                continue
            
            # Send message to agent and get response
            logger.info(f"Sending message to {agent.name}: {user_input}")
            
            response = await agent.send_message(user_input)
            
            # Streaming prints inline (agent.send_message handles the prefix)
            from daie.core.llm_manager import get_llm_config
            if not get_llm_config().stream and response:
                print(f"\n{agent.name}: {response}")
            
            print()
            
        except KeyboardInterrupt:
            print(f"\n\n{agent.name}: Goodbye!")
            break
        except Exception as e:
            logger.error(f"Error in chat loop: {e}")
            print(f"\n{agent.name}: I'm sorry, I encountered an error. Please try again.")


def create_chat_agent():
    """
    Create and configure a chat agent with appropriate settings.
    """
    config = AgentConfig(
        name="ALEX",
        role=AgentRole.GENERAL_PURPOSE,
        goal="Help users with their questions and provide information",
        backstory="Created to assist with general questions and provide information",
        system_prompt=(
            "You are ALEX a helpful AI assistant that provides accurate and friendly answers. "
            "Keep your responses concise and helpful. Be conversational and approachable."
        ),
        capabilities=["text", "communication"],
    )
    
    # Create agent instance
    agent = Agent(config=config)
    
    
    logger.info(f"Agent {agent.name} (ID: {agent.id}) created successfully")
    
    return agent


async def main():
    """
    Main entry point of the application.
    """
    # Create and start the agent
    agent = create_chat_agent()
    
    try:
        # Start the agent
        logger.info(f"Starting agent {agent.name}...")
        await agent.start()
        
        # Start chat loop
        await chat_with_agent(agent)
        
    except KeyboardInterrupt:
        logger.info("Chat session interrupted by user")
    except Exception as e:
        logger.error(f"Error during chat session: {e}")
    finally:
        # Stop the agent
        logger.info(f"Stopping agent {agent.name}...")
        await agent.stop()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nChat session terminated.")
