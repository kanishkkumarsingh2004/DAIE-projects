# Custom Tool Integration

## Description
A practical demonstration of how to extend a DAIE agent's capabilities using custom tools. This example showcases the `@tool` decorator for defining new functions that the agent can autonomously select and execute during a ReAct loop.

## Features
- **Custom Tool Decorator**: Define tools using the simple `@tool` syntax.
- **Multi-Tool Support**: Combining custom tools with built-in tools like `FileManagerTool`.
- **Autonomous Tool Selection**: The agent uses a ReAct (Reasoning and Acting) loop to decide which tool to use based on the task description.
- **File System Interaction**: Demonstrate saving computational results to the local filesystem.

## Prerequisites
- Python 3.7+
- DAIE library installed
- Ollama running with `llama3.2:1b` model (or configure your preferred model)

## Configuration
The `MathBot` agent is configured with:
- **Name**: MathBot
- **Role**: General Purpose
- **System Prompt**: "You are a capable agent with access to math and file tools."
- **LLM**: `llama3.2:1b` (configured via `set_llm`)

## Usage
```bash
python Custom_tool.py
```

## Code Structure
```python
# Main components:
1. Tool Definition: `@tool` decorator applied to `calculate_math`.
2. Agent Setup: `Agent` initialized with `AgentConfig`.
3. Tool Addition: `agent.add_tool(calculate_math)` and `agent.add_tool(FileManagerTool())`.
4. Execution: `agent.execute_task()` with a complex multi-step request.
5. Lifecycle: `agent.start()` and `agent.stop()`.
```

## Step-by-Step Logic
1. **Tool Registration**: The `calculate_math` tool is registered with a name and description, which the LLM uses to understand its purpose.
2. **Task Processing**: The user asks a compound task: "Calculate 25 * 14 and save the result into a file called result.txt".
3. **Reasoning**: The agent identifies it needs the math tool first, then the file tool.
4. **Action**: 
   - Calls `calculate_math("25 * 14")`.
   - Calls `FileManagerTool` to write "350" to `result.txt`.
5. **Completion**: The agent returns the final confirmation.

## Example Output
```
Final Answer: I have calculated 25 * 14 to be 350 and saved it to result.txt.
```

## Use Cases
- **Mathematical Computation**: Complex math not inherently handled well by text generation.
- **External Integration**: Connecting agents to database queries, internal APIs, or legacy systems.
- **Autonomous Workflows**: Tasks involving multiple steps of computation and IO.

## Best Practices
- **Clear Descriptions**: Provide detailed tool descriptions so the LLM knows exactly when to use them.
- **Input Type Hinting**: Use clear parameter names and types in the function signature.
- **Error Handling**: Implement `try-except` blocks within your tool functions to return helpful error messages to the agent.
