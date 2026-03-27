# Simple Ollama Chat Loop

## Description
A comprehensive chat application demonstrating the DAIE library's core features with detailed logging and error handling. This example shows how to create a production-ready AI agent with proper logging, configuration, and graceful shutdown.

## Features
- **Interactive Chat Loop**: Real-time conversation with AI agent
- **Streaming Responses**: Real-time streaming of AI responses
- **Comprehensive Logging**: Detailed logging for debugging and monitoring
- **Error Handling**: Robust error handling and recovery
- **Configurable Agent**: Customizable agent personality and behavior
- **Graceful Shutdown**: Proper cleanup on exit or interruption

## Prerequisites
- Python 3.7+
- DAIE library installed
- Ollama running with `llama3.2:1b` model (or configure your preferred model)

## Configuration
The agent is configured with the following settings:
- **Name**: ALEX
- **Role**: General Purpose
- **Goal**: Help users with their questions and provide information
- **Backstory**: Created to assist with general questions and provide information
- **System Prompt**: Helpful AI assistant that provides accurate and friendly answers
- **Capabilities**: Text and communication

## LLM Configuration
```python
set_llm(
    ollama_llm="llama3.2:1b",
    temperature=0.3,
    max_tokens=1500,
    llm_type=LLMType.OLLAMA,
    stream=True
)
```

## Usage
```bash
python simple_ollama_chat_loop.py
```

### Commands
- Type your message and press Enter to chat
- Type `quit`, `exit`, or `q` to end the session
- Press `Ctrl+C` to interrupt

## Code Structure
```python
# Main components:
1. Logging Configuration: Set up comprehensive logging
2. LLM Configuration: Configure Ollama model with streaming
3. Agent Creation: create_chat_agent() function
4. Chat Loop: chat_with_agent() function with error handling
5. Main Entry Point: main() function with proper lifecycle management
```

## Logging Configuration
```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
```

### Log Levels
- **INFO**: General information about agent operations
- **ERROR**: Error messages and exceptions
- **DEBUG**: Detailed debugging information (if enabled)

## Agent Creation
```python
def create_chat_agent():
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
    
    agent = Agent(config=config)
    logger.info(f"Agent {agent.name} (ID: {agent.id}) created successfully")
    return agent
```

## Chat Loop
```python
async def chat_with_agent(agent: Agent):
    print(f"Connected to {agent.name}! Type 'quit' or 'exit' to end the chat.")
    print("=" * 50)
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ["quit", "exit", "q"]:
                print(f"\n{agent.name}: Goodbye!")
                break
            
            if not user_input:
                continue
            
            logger.info(f"Sending message to {agent.name}: {user_input}")
            response = await agent.send_message(user_input)
            
            # Handle streaming vs non-streaming
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
```

## Example Session
```
2024-01-15 10:30:45 - __main__ - INFO - Agent ALEX (ID: agent_1234567890) created successfully
2024-01-15 10:30:45 - __main__ - INFO - Starting agent ALEX...
Connected to ALEX! Type 'quit' or 'exit' to end the chat.
==================================================

You: Hello!
2024-01-15 10:30:50 - __main__ - INFO - Sending message to ALEX: Hello!
ALEX: Hi there! How can I help you today?

You: What is DAIE?
2024-01-15 10:30:55 - __main__ - INFO - Sending message to ALEX: What is DAIE?
ALEX: DAIE stands for Decentralized AI Ecosystem. It's an open-source Python library for building multi-agent AI systems. Pretty cool stuff!

You: quit
2024-01-15 10:31:00 - __main__ - INFO - Stopping agent ALEX...
ALEX: Goodbye!
```

## Error Handling
The application includes comprehensive error handling:

### Chat Loop Errors
```python
try:
    response = await agent.send_message(user_input)
except Exception as e:
    logger.error(f"Error in chat loop: {e}")
    print(f"\n{agent.name}: I'm sorry, I encountered an error. Please try again.")
```

### Main Function Errors
```python
try:
    await agent.start()
    await chat_with_agent(agent)
except KeyboardInterrupt:
    logger.info("Chat session interrupted by user")
except Exception as e:
    logger.error(f"Error during chat session: {e}")
finally:
    await agent.stop()
```

## Best Practices Demonstrated
1. **Logging**: Comprehensive logging for debugging and monitoring
2. **Error Handling**: Graceful error recovery and user feedback
3. **Resource Management**: Proper agent lifecycle management
4. **User Experience**: Clear prompts and feedback
5. **Configuration**: Centralized configuration management
6. **Documentation**: Well-documented code and functions

## Customization
You can modify the agent's behavior by adjusting the `AgentConfig`:
- `name`: Change the agent's name
- `goal`: Modify the agent's primary goal
- `backstory`: Adjust the agent's background
- `system_prompt`: Define the agent's core behavior
- `capabilities`: Add or remove agent capabilities

## Use Cases
- Customer support chatbots
- Educational assistants
- General-purpose AI assistants
- Development and testing
- Production chat applications

## Production Considerations
- **Logging**: Use appropriate log levels and handlers
- **Error Handling**: Implement proper error tracking
- **Monitoring**: Track agent performance and usage
- **Security**: Implement authentication and authorization
- **Scalability**: Consider multi-agent deployment

## Troubleshooting
### Common Issues
1. **Agent not responding**: Check Ollama is running and model is available
2. **Slow responses**: Consider using a smaller model or adjusting temperature
3. **Connection errors**: Verify network connectivity and API endpoints
4. **Memory issues**: Monitor agent memory usage and implement cleanup

### Debug Mode
Enable debug logging for more detailed information:
```python
logging.basicConfig(level=logging.DEBUG)
```
