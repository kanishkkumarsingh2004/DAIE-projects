# DAIE Configuration Guide

This guide provides a comprehensive overview of how to configure the Decentralized AI Ecosystem (DAIE) for various environments and use cases.

## 1. LLM Configuration (`set_llm`)

The `set_llm` function is the primary way to define which AI model your agents will use.

```python
from daie.core import set_llm, LLMType

set_llm(
    ollama_llm="llama3.2:1b",  # Specify any model available in 'ollama list'
    temperature=0.3,           # 0.0 for factual, 1.0 for creative
    max_tokens=1024,           # Limit response length
    llm_type=LLMType.OLLAMA,   # Backend provider
    stream=True                # Enable real-time token streaming
)
```

### Parameters
- **ollama_llm**: The name of the model (e.g., `mistral`, `llama3`).
- **temperature**: Controls randomness. Use low values for tools and logic, high values for creative writing.
- **max_tokens**: Prevents runaway generation and manages resource usage.
- **stream**: If `True`, callbacks will be triggered for every token generated.

---

## 2. Agent Configuration (`AgentConfig`)

Every `Agent` in DAIE requires an `AgentConfig` to define its identity and capabilities.

### Core Identity
- **name**: A unique identifier for the agent.
- **role**: Uses `AgentRole` enum (e.g., `RESEARCHER`, `ORCHESTRATOR`).
- **system_prompt**: The "personality" and "instructions" for the model.

### Style & Behavior
- **personality**: Adjectives describing the tone (e.g., "professional", "sarcastic").
- **behavior**: Actionable constraints (e.g., "always cite sources", "use bullet points").

### Sample Configuration
```python
from daie import AgentConfig, AgentRole

config = AgentConfig(
    name="Researcher_01",
    role=AgentRole.RESEARCHER,
    system_prompt="You are an expert analyst. Focus on technical accuracy.",
    personality="analytical and cold",
    behavior="always double-check facts and output in JSON when asked",
    temperature=0.2
)
```

---

## 3. Tool Configuration

Agents can be granted tools to interact with the world.

```python
from daie.tools import FileManagerTool, APICallTool

agent.add_tool(FileManagerTool())
agent.add_tool(APICallTool())
```

> [!TIP]
> Use the `@tool` decorator to create custom functions that your agents can understand and call autonomously.

---

## 4. Environment-Based Configuration

For production systems, it is best practice to use environment variables.

### Using `.env` Files
1. Create a `.env` file in your root directory:
   ```env
   OLLAMA_MODEL=mistral
   DAIE_TEMPERATURE=0.5
   DAIE_MAX_TOKENS=2048
   ```

2. Load them in your script:
   ```python
   import os
   from dotenv import load_dotenv
   load_dotenv()

   set_llm(
       ollama_llm=os.getenv("OLLAMA_MODEL"),
       temperature=float(os.getenv("DAIE_TEMPERATURE"))
   )
   ```

---

## 5. RAG (Retrieval-Augmented Generation)

To give agents access to your private documents, configure the RAG settings.

```python
config = AgentConfig(
    enable_rag=True,
    rag_document_path="./my_documents/", # Directory containing .txt or .pdf files
)
```

### RAG Best Practices
- **Chunking**: DAIE automatically handles chunking, but ensures your source documents have clear headings for better retrieval results.
- **Storage**: Vector indices are created in memory or persisted depending on the implementation used in your agent.

---

## 6. Networking Configuration (P2P)

For distributed systems, configure the agent's P2P settings.

```python
config = AgentConfig(
    network_url="http://localhost:8000",
    auth_token="secure_token_abc_123",
    allow_file_transfers=True
)
```

> [!IMPORTANT]
> Ensure your firewall allows incoming connections on the port specified in `network_url`.
