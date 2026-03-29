# Node-Based Multi-Agent Interactive Chat

## Description
An advanced interactive chat application demonstrating the Node class with real agents in the DAIE library. This example shows how to create and manage a production-ready node that hosts multiple specialized agents with an interactive command-line interface for real-time conversation, resource management, and peer-to-peer networking.

## Features
- **Node Architecture**: Centralized node management for multiple agents
- **Multi-Agent Hosting**: Host multiple specialized agents on a single node
- **Interactive Chat Loop**: Real-time conversation with AI agents
- **Resource Management**: Configure and monitor node resources (GPU, memory, cache)
- **P2P Networking**: Connect nodes via peer-to-peer communication layer
- **Agent Coordination**: Collaborative task execution across multiple agents
- **Intelligent Routing**: Automatic message routing based on content analysis
- **Status Monitoring**: Real-time node and agent status tracking
- **Streaming Support**: Optional real-time streaming of AI responses
- **Command Interface**: Rich set of commands for system control
- **Graceful Shutdown**: Proper cleanup of agents, nodes, and connections

## Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    Node (Production Server)                 │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │
│  │  Assistant  │  │   Coder     │  │  Researcher │          │
│  │   Agent     │  │   Agent     │  │   Agent     │          │
│  └─────────────┘  └─────────────┘  └─────────────┘          │
│         │                │                │                 │
│         └────────────────┼────────────────┘                 │
│                          │                                  │
│              CommunicationManager (P2P Layer)               │
│                          │                                  │
└──────────────────────────┼──────────────────────────────────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
      ┌────▼─────┐   ┌─────▼────┐   ┌──────▼───┐
      │  Node A  │◄─►│  Node B  │◄─►│  Node C  │
      └──────────┘   └──────────┘   └──────────┘
```

## Prerequisites
- Python 3.7+
- DAIE library installed
- Ollama running with `llama3.2:1b` model (or configure your preferred model)

## Agent Configuration

### Assistant Agent
- **Name**: Assistant
- **Role**: General Purpose
- **Purpose**: General-purpose assistance, explanations, and various tasks
- **Personality**: Friendly, patient, and thorough
- **Behavior**: Always provides clear explanations with examples

### Coder Agent
- **Name**: Coder
- **Role**: Specialized
- **Purpose**: Writing, debugging, and explaining code
- **Personality**: Precise, logical, and detail-oriented
- **Behavior**: Always includes code comments and best practices

### Researcher Agent
- **Name**: Researcher
- **Role**: Specialized
- **Purpose**: Gathering information, analyzing data, and providing well-researched answers
- **Personality**: Analytical, thorough, and objective
- **Behavior**: Always structures responses with clear sections and bullet points

## Node Resources
The node is configured with the following resources:
- **GPU Count**: 2
- **Memory**: 16 GB
- **Model Cache**: llama3.2 model cached
- **Max Concurrent Tasks**: 5

## LLM Configuration
```python
set_llm(
    ollama_llm="llama3.2:1b",
    stream=True  # or False based on user preference
)
```

## Usage
```bash
python node_agents_interactive.py
```

### Interactive Commands
The interactive mode provides a command-line chat interface with the following commands:

| Command | Description |
|---------|-------------|
| `<message>` | Chat with agents (auto-routed based on content) |
| `status` | Show node status |
| `info` | Show detailed node information (JSON) |
| `resources` | Show node resources |
| `agents` | List all registered agents |
| `collaborate <task>` | Execute collaborative task with all agents |
| `connect <node_id>` | Connect to a peer node |
| `exit` / `quit` | Exit the chat |

### Agent Routing
Messages are automatically routed based on keywords:
- **Code/Programming** → Coder Agent (keywords: code, program, function, debug, implement, script)
- **Research/Analysis** → Researcher Agent (keywords: research, analyze, study, data, information, explain)
- **Other** → Assistant Agent

## Code Structure

### NodeChatSystem Class
The main class that manages the node-based chat system:

```python
class NodeChatSystem:
    def __init__(self, node_id: str, node_name: str)
    async def initialize(self, use_streaming: bool = True)
    async def _create_agents(self)
    async def connect_to_peer(self, peer_node_id: str)
    async def route_message(self, message: str, agent_type: str = "auto") -> str
    async def execute_collaborative_task(self, task: str) -> str
    def get_node_info(self) -> dict
    async def shutdown(self)
```

### Key Methods
- **`initialize()`**: Sets up LLM, communication manager, node, resources, and agents
- **`route_message()`**: Routes messages to appropriate agents based on content
- **`execute_collaborative_task()`**: Coordinates multiple agents on a single task
- **`connect_to_peer()`**: Establishes P2P connections with other nodes
- **`shutdown()`**: Gracefully stops agents, node, and communication manager

### Interactive Chat Loop Function
```python
async def interactive_chat_loop(system: NodeChatSystem):
    """
    Run an interactive chat loop with the node-based system.
    
    Args:
        system: The NodeChatSystem instance
    """
    # Provides command-line interface for real-time interaction
```

## Interactive Features

### 1. Chat with Agents
Type any message to chat with agents. Messages are automatically routed:
```bash
You: Write a Python function to sort a list
Agent Response: [Coder Agent responds with code]

You: Explain quantum computing
Agent Response: [Researcher Agent responds with explanation]

You: What's the weather like?
Agent Response: [Assistant Agent responds]
```

### 2. Node Status
```bash
You: status
Node Status:
    Node ID: production-node-001
    Name: Production Server Node
    Status: active
    Agents: 3 active
      - Assistant (abc12345...)
      - Coder (def67890...)
      - Researcher (ghi11223...)
    Connections: 0 peers
    Resources: 4 configured
```

### 3. Detailed Information
```bash
You: info
Detailed Node Information:
{
  "node": {
    "node_id": "production-node-001",
    "name": "Production Server Node",
    "status": "active",
    "agent_count": 3,
    "agents": ["agent-id-1", "agent-id-2", "agent-id-3"],
    "connection_count": 0,
    "resources": {...}
  },
  "agents": {
    "assistant": {
      "id": "agent-id-1",
      "name": "Assistant",
      "role": "general_purpose",
      "is_running": true
    },
    ...
  },
  "resources": {...}
}
```

### 4. Resource Management
```bash
You: resources
Node Resources:
  gpu_count: 2
  memory_gb: 16
  model_cache: {'llama3.2': True}
  max_concurrent_tasks: 5
```

### 5. Agent Listing
```bash
You: agents
Registered Agents:
  - Assistant (assistant)
    ID: agent-id-1
    Role: general_purpose
    Status: Running
  - Coder (coder)
    ID: agent-id-2
    Role: specialized
    Status: Running
  - Researcher (researcher)
    ID: agent-id-3
    Role: specialized
    Status: Running
```

### 6. Collaborative Tasks
```bash
You: collaborate Design a REST API for a todo application
Starting collaborative task...
    → Consulting Assistant...
    → Consulting Coder...
    → Consulting Researcher...

Collaborative Result:
==================================================
COLLABORATIVE RESPONSE
==================================================

**Assistant:**
[Assistant's contribution]

---

**Coder:**
[Coder's contribution with code]

---

**Researcher:**
[Researcher's contribution with analysis]
```

### 7. Peer Node Connection
```bash
You: connect peer-node-002
[+] Connected to peer node: peer-node-002
```

## Demonstration Steps

### 1. System Initialization
```python
system = NodeChatSystem(
    node_id="production-node-001",
    name="Production Server Node"
)
await system.initialize(use_streaming=True)
```

### 2. Agent Creation
Three specialized agents are created and registered on the node:
- Assistant (General Purpose)
- Coder (Specialized)
- Researcher (Specialized)

### 3. Resource Configuration
```python
node.set_resource("gpu_count", 2)
node.set_resource("memory_gb", 16)
node.set_resource("model_cache", {"llama3.2": True})
node.set_resource("max_concurrent_tasks", 5)
```

### 4. Interactive Chat Loop
```python
await interactive_chat_loop(system)
```

### 5. Graceful Shutdown
```python
await system.shutdown()
```

## Logging
- **File Logging**: Detailed logs written to `node_agents.log`
- **Console Logging**: Warnings only displayed on console
- **Log Format**: Timestamp, logger name, level, and message

## Error Handling
- Comprehensive exception handling in chat loop
- Graceful degradation on agent failures
- Proper cleanup in finally blocks
- User-friendly error messages with color coding
- KeyboardInterrupt handling for clean exit

## Best Practices Demonstrated
1. **Separation of Concerns**: Node, agents, and communication are separate components
2. **Async/Await**: Proper asynchronous programming patterns
3. **Resource Management**: Configuring and monitoring node resources
4. **Error Handling**: Robust error handling and recovery
5. **Logging**: Comprehensive logging for debugging and monitoring
6. **Graceful Shutdown**: Proper cleanup of resources
7. **Configuration**: Flexible configuration options
8. **Documentation**: Well-documented code with docstrings
9. **User Experience**: Color-coded output and clear command interface

## Use Cases
- **Production AI Systems**: Deploy multiple specialized agents on a single node
- **Interactive Development**: Test and experiment with multi-agent systems
- **Distributed Computing**: Connect multiple nodes for scalable AI processing
- **Collaborative AI**: Coordinate multiple agents for complex tasks
- **Research & Development**: Experiment with multi-agent architectures
- **Educational**: Learn about node-based agent systems
- **Customer Support**: Deploy interactive AI support systems

## Troubleshooting

### Common Issues

#### LLM Not Responding
- Ensure Ollama is running: `ollama serve`
- Verify model is available: `ollama list`
- Check model name in configuration matches available models

#### Connection Errors
- Verify network connectivity
- Check firewall settings for P2P communication
- Ensure peer node IDs are correct

#### Agent Not Found
- Verify agent names: `assistant`, `coder`, `researcher`
- Check agent initialization completed successfully

#### Resource Issues
- Monitor system resources (GPU, memory)
- Adjust `max_concurrent_tasks` based on available resources
- Check Ollama resource usage

#### Command Not Recognized
- Check command spelling
- Use `help` or refer to command table
- Ensure proper spacing in commands like `collaborate <task>`

## Related Examples
- [Node-Based Multi-Agent Demo](node_agents_demo.md) - Automated demo version
- [Simple Ollama Chat Loop](simple_ollama_chat_loop.md) - Basic chat with single agent
- [P2P Networking](p2p_networking.md) - Peer-to-peer agent communication
- [Orchestrator RAG](Orchestrator_RAG.md) - RAG-based orchestration
- [Orchestrator Courtroom](Orchestrator_courtroom.md) - Multi-agent orchestration

## Additional Resources
- [DAIE Library Documentation](../README.md)
- [Agent Configuration Guide](../README.md#agent-configuration)
- [Communication Manager](../README.md#communication-manager)
- [Node Architecture](../README.md#node-architecture)
