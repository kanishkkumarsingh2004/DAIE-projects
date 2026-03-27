# AI Girlfriend Config Chat Loop

## Description
An interactive chat application featuring an AI girlfriend persona named "Luna" with streaming responses. This example demonstrates how to create a personalized AI agent with custom personality traits and behavior patterns.

## Features
- **Streaming Responses**: Real-time streaming of AI responses for a more natural conversation flow
- **Customizable Personality**: Configurable agent personality with traits like flirty, playful, caring, and teasing
- **Gender-Specific Behavior**: Female agent with gender-appropriate responses
- **Short Response Mode**: Limited to 1-2 line responses for quick, engaging conversations
- **Graceful Exit Handling**: Handles exit commands and keyboard interrupts gracefully

## Prerequisites
- Python 3.7+
- DAIE library installed
- Ollama running with `llama3.2:1b` model (or configure your preferred model)

## Configuration
The agent is configured with the following settings:
- **Name**: Luna
- **Role**: General Purpose
- **Personality**: Flirty, playful, caring, teasing, sweet, and engaging
- **Temperature**: 0.9 (more creative responses)
- **Max Tokens**: 150 (keeps responses short)
- **RAG**: Disabled

## Usage
```bash
python ai_gf_config_chat_loop.py
```

### Commands
- Type your message and press Enter to chat
- Type `exit` or `quit` to end the session
- Press `Ctrl+C` to interrupt

## Code Structure
```python
# Main components:
1. LLM Configuration: set_llm() with Ollama model and streaming enabled
2. Agent Configuration: AgentConfig with personality and behavior settings
3. Agent Initialization: Agent creation and startup
4. Chat Loop: Interactive input/output loop with error handling
5. Cleanup: Graceful agent shutdown
```

## Example Output
```
💖 Luna is online...

You 🧑: Hello!
Luna: Hey there! 😊 How's your day going?

You 🧑: What's your favorite color?
Luna: Hmm, I love pink! 💖 It's so pretty and romantic~

Luna 💔: leaving me already? 😤 come back soon ❤️
```

## Customization
You can modify the agent's personality by changing the `AgentConfig` parameters:
- `system_prompt`: Define the agent's core behavior
- `personality`: Adjust personality traits
- `behavior`: Set specific behavioral patterns
- `temperature`: Control response creativity (0.0-1.0)
- `max_tokens`: Limit response length
