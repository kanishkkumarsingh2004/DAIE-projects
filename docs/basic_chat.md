# Basic Chat

## Description
A fundamental chat application demonstrating the core features of the DAIE library. This example shows how to create a simple AI agent with RAG (Retrieval-Augmented Generation) capabilities and an interactive chat loop.

## Features
- **Interactive Chat Loop**: Real-time conversation with AI agent
- **RAG Integration**: Document-based knowledge retrieval
- **Streaming Responses**: Real-time streaming of AI responses
- **Customizable Agent**: Configurable personality and behavior
- **Error Handling**: Graceful handling of errors and interruptions

## Prerequisites
- Python 3.7+
- DAIE library installed
- Ollama running with `llama3.2:1b` model
- Knowledge base document at `./data/knowledge_base.txt` (optional)

## Configuration
The agent is configured with the following settings:
- **Name**: Luna
- **Role**: General Purpose
- **Personality**: Sassy, witty, and very direct
- **Behavior**: Always uses emojis and speaks enthusiastically
- **Temperature**: 0.9 (creative responses)
- **Max Tokens**: 1024
- **RAG**: Enabled with document path

## Usage
```bash
python basic_chat.py
```

### Commands
- Type your message and press Enter to chat
- Type `exit` or `quit` to end the session
- Press `Ctrl+C` to interrupt

## Code Structure
```python
# Main components:
1. LLM Configuration: set_llm() with Ollama model and streaming
2. Agent Configuration: AgentConfig with RAG settings
3. Agent Initialization: Agent creation and startup
4. Chat Loop: Interactive input/output with error handling
5. Cleanup: Graceful agent shutdown
```

## RAG Configuration
The agent uses Retrieval-Augmented Generation to answer questions based on documents:
```python
rag_document_path="./data/knowledge_base.txt"
enable_rag=True
```

### Setting Up RAG
1. Create a `data` directory in the same folder as the script
2. Add your knowledge base document (e.g., `knowledge_base.txt`)
3. The agent will automatically load and index the document

## Example Output
```
=== Basic Chat Loop ===
Type 'exit' or press Ctrl+C to quit.

You: What is DAIE?
Luna: DAIE stands for Decentralized AI Ecosystem! 🚀 It's an open-source Python library for building multi-agent AI systems. Pretty cool, right? 😎

You: exit
```

## Customization Options
You can modify the agent's behavior by adjusting the `AgentConfig`:
- `system_prompt`: Define the agent's core behavior
- `personality`: Adjust personality traits
- `behavior`: Set specific behavioral patterns
- `temperature`: Control response creativity (0.0-1.0)
- `max_tokens`: Limit response length
- `rag_document_path`: Path to knowledge base documents
- `enable_rag`: Enable/disable RAG functionality

## Error Handling
The application handles:
- Keyboard interrupts (Ctrl+C)
- EOF errors
- API errors (displayed to user)
- Empty input (ignored)

## Best Practices
1. Keep the knowledge base document focused and relevant
2. Use appropriate temperature settings for your use case
3. Monitor token usage to control costs
4. Implement proper error handling in production
