# Simplified Chat Loop

## Description
A beginner-friendly example demonstrating how to use `ChatLoopConfig` to quickly set up a chat loop without writing the full boilerplate code. This is the simplest way to get a chat application running with the DAIE library.

## Features
- **Quick Setup**: One-liner chat loop initialization
- **Minimal Code**: Reduced boilerplate compared to manual implementation
- **Streaming Responses**: Real-time streaming of AI responses
- **Customizable Agent**: Configurable personality and behavior
- **Beginner Friendly**: Perfect starting point for new users

## Prerequisites
- Python 3.7+
- DAIE library installed
- Ollama running with `llama3.2:1b` model

## Configuration
The agent is configured with the following settings:
- **Name**: LUNA
- **Role**: General Purpose
- **Personality**: Friendly and helpful
- **Behavior**: Helpful and concise AI assistant
- **Streaming**: Enabled

## Usage
```bash
python simplified_chat_loop.py
```

### Commands
- Type your message and press Enter to chat
- Type `exit` or `quit` to end the session
- Press `Ctrl+C` to interrupt

## Code Structure
```python
# Main components:
1. LLM Configuration: set_llm() with Ollama model and streaming
2. Agent Configuration: AgentConfig with basic settings
3. Agent Initialization: Agent creation
4. Chat Loop: ChatLoopConfig.quick_start() for instant setup
```

## Key Concepts

### ChatLoopConfig
The `ChatLoopConfig` class provides a simplified interface for creating chat loops:
```python
from daie.chat import ChatLoopConfig

# One-liner to start chat!
ChatLoopConfig.quick_start(agent).run()
```

### Agent Configuration
Basic agent setup with minimal required parameters:
```python
config = AgentConfig(
    name="LUNA",
    role=AgentRole.GENERAL_PURPOSE,
    system_prompt="You are a helpful and concise AI assistant.",
    personality="friendly and helpful"
)
```

## Example Output
```
You: Hello!
LUNA: Hi there! How can I help you today?

You: What can you do?
LUNA: I'm a helpful AI assistant! I can answer questions, have conversations, and assist with various tasks. Just ask me anything!

You: exit
```

## Comparison with Manual Implementation

### Simplified Approach (This Example)
```python
ChatLoopConfig.quick_start(agent).run()
```

### Manual Approach (basic_chat.py)
```python
while True:
    try:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            break
        response = agent.chat(user_input)
        print(f"\n{agent.name}: {response}")
    except KeyboardInterrupt:
        break
```

## Customization Options
You can modify the agent's behavior by adjusting the `AgentConfig`:
- `name`: Set the agent's display name
- `role`: Choose from available agent roles
- `system_prompt`: Define the agent's core behavior
- `personality`: Adjust personality traits

## When to Use This Approach
- **Prototyping**: Quickly test agent configurations
- **Learning**: Understand DAIE basics without complexity
- **Simple Applications**: Basic chat interfaces
- **Demos**: Showcase agent capabilities

## When to Use Manual Implementation
- **Custom Logic**: Need custom input/output handling
- **Advanced Features**: Require RAG, tools, or complex workflows
- **Production**: Need fine-grained control over the chat loop
- **Error Handling**: Require specific error handling strategies

## Best Practices
1. Start with this simplified approach for new projects
2. Graduate to manual implementation when you need more control
3. Keep system prompts clear and concise
4. Test different personality settings to find the right fit
5. Use streaming for better user experience

## Related Examples
- [Basic Chat](basic_chat.md) - Manual chat loop implementation
- [Simple Ollama Chat Loop](simple_ollama_chat_loop.md) - Alternative simplified approach
- [AI Girlfriend Config Chat Loop](ai_gf_config_chat_loop.md) - Advanced configuration example
