# P2P Multi-Agent Networking & File Transfer

## Description
A comprehensive demonstration of peer-to-peer (P2P) networking capabilities in the DAIE library. This example shows how to create multiple agents that can communicate directly with each other, transfer files, and implement authorization controls.

## Features
- **P2P Communication**: Direct agent-to-agent messaging
- **File Transfer**: A2A (Agent-to-Agent) file transfer protocol
- **Authorization Whitelisting**: Control which agents can send messages
- **Registry-Based Discovery**: Automatic agent discovery and registration
- **Communication Statistics**: Track message delivery and network stats
- **Security Controls**: Token-based authentication and sender restrictions

## Prerequisites
- Python 3.7+
- DAIE library installed
- Ollama running with `wizard-vicuna-uncensored:7b` model (or configure your preferred model)

## Agent Configuration
### NodeAlfa (Sender)
- **Name**: NodeAlfa
- **Role**: General Purpose
- **Network URL**: http://localhost:8000
- **Purpose**: Networking relay agent

### NodeBravo (Receiver)
- **Name**: NodeBravo
- **Role**: General Purpose
- **Network URL**: http://localhost:8001
- **Auth Token**: secure_token_123
- **File Transfers**: Enabled
- **Purpose**: Secure receiver agent

### Intruder (Test Agent)
- **Name**: Intruder
- **Role**: General Purpose
- **Purpose**: Test authorization blocking

## Usage
```bash
python p2p_networking.py
```

## Code Structure
```python
# Main components:
1. Communication Manager: Shared communication hub
2. Agent Creation: Three agents with different configurations
3. Direct Messaging: Agent-to-agent message sending
4. Registry Discovery: Query agent registry
5. File Transfer: A2A file transfer demonstration
6. Authorization Test: Blocked sender demonstration
7. Statistics: Communication stats display
8. Cleanup: Graceful shutdown
```

## Demonstration Steps
### 1. Direct Messaging
```python
msg = AgentMessage(
    sender_id=agent1.id,
    receiver_id=agent2.id,
    content="Hello from NodeAlfa! Are you online?",
    message_type="text",
)
result = await comm.send_message(msg)
```

### 2. Registry Discovery
```python
node_info = comm.registry.get_node(agent2.id)
print(f"Found NodeBravo in registry: {node_info}")
```

### 3. File Transfer
```python
file_tool = agent1.get_tool("a2a_send_file")
result = await file_tool._execute({
    "receiver_id": agent2.id,
    "file_path": payload_path,
    "message": "Secure payload inbound!",
})
```

### 4. Authorization Test
```python
# Restrict NodeBravo to only accept messages from NodeAlfa
agent2.config.allowed_senders = [agent1.id]

# Intruder's message will be blocked
blocked_msg = AgentMessage(
    sender_id=agent3.id,
    receiver_id=agent2.id,
    content="I'm trying to sneak in!",
    message_type="text",
)
await comm.send_message(blocked_msg)
```

## Example Output
```
==================================================
  P2P Multi-Agent Networking Demo
==================================================

  NodeAlfa  ID: agent_1234567890
  NodeBravo ID: agent_0987654321

[1] Sending a direct message from NodeAlfa → NodeBravo...
    Message delivered: True

[2] Querying the Node Registry for discovered agents...
    Found NodeBravo in registry: {'id': 'agent_0987654321', 'name': 'NodeBravo', ...}

[3] Demonstrating A2A File Transfer...
    Sending 'demo_payload.txt' from NodeAlfa → NodeBravo...
    File transfer result: {'success': True, 'message': 'File transferred successfully'}

[4] Testing authorization (blocked sender)...
    Intruder message was blocked by authorization whitelist ✓

[5] Communication Manager Stats:
    messages_sent: 3
    messages_received: 2
    files_transferred: 1
    active_connections: 3

==================================================
  Demo complete! Cleaning up...
==================================================
```

## Communication Manager
The `CommunicationManager` is the central hub for all agent communications:
- Manages agent registration
- Routes messages between agents
- Handles file transfers
- Tracks communication statistics
- Enforces authorization rules

## Security Features
### Authentication
- Token-based authentication for secure agents
- Configurable auth tokens per agent

### Authorization
- Whitelist-based sender restrictions
- Empty whitelist allows all senders
- Specific sender IDs can be blocked or allowed

### File Transfer Security
- Only agents with `allow_file_transfers=True` can send/receive files
- File transfers are logged and tracked

## Use Cases
- Distributed AI systems
- Multi-agent collaboration
- Secure file sharing
- Network simulation
- Agent discovery protocols
- Authorization system testing

## Production Considerations
In a production environment:
- Each agent would run on a separate host
- Use public-facing network URLs (e.g., DevTunnels)
- Implement proper SSL/TLS encryption
- Use secure authentication tokens
- Monitor network traffic and stats

## Error Handling
The application handles:
- Network connection errors
- Message delivery failures
- File transfer errors
- Authorization violations
- Agent registration issues
