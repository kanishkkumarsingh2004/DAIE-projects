# Orchestrator RAG

## Description
A research lab simulation using the DAIE library's Orchestrator pattern with RAG (Retrieval-Augmented Generation) capabilities. This example demonstrates how to create a multi-agent system where a professor coordinates with research assistants to answer questions based on documents.

## Features
- **Multi-Agent Coordination**: Professor orchestrates research assistants
- **RAG Integration**: Document-based knowledge retrieval
- **Role-Based Agents**: Each agent has specific expertise and goals
- **Streaming Support**: Real-time streaming of responses
- **Interactive Interface**: User presents research questions
- **JSON Response Parsing**: Automatic extraction of answers from structured responses

## Prerequisites
- Python 3.7+
- DAIE library installed
- Ollama running with `llama3.2:1b` model
- Documents in the `./data` directory

## Agent Roles
### Professor (Main Agent)
- **Name**: Professor_AI
- **Role**: Coordinator
- **Goal**: Coordinate students to solve complex problems professionally
- **Expertise**: Breaks down complex queries into logical sub-tasks

### Research Assistant (Sub-Agent)
- **Name**: NOVA
- **Role**: General Purpose
- **Goal**: Answer questions accurately using document context
- **Expertise**: Precise, helpful, and thorough analysis

## Configuration
### Professor Agent
```python
config2 = AgentConfig(
    name="Professor_AI",
    role=AgentRole.COORDINATOR,
    goal="Coordinate students to solve complex problems professionally",
    system_prompt="You are an expert professor. You break down complex queries into logical sub-tasks for your students.",
    rag_document_path=DOCUMENTS_PATH,
    enable_rag=True,
)
```

### Research Assistant Agent
```python
config1 = AgentConfig(
    name="NOVA",
    role=AgentRole.GENERAL_PURPOSE,
    system_prompt="You are a knowledgeable assistant. Use the provided document context to answer questions accurately.",
    personality="precise, helpful, and thorough",
    gender="female",
    behavior="always cites the source document chunk in your answer",
    temperature=0.3,
    max_tokens=1024,
    rag_document_path=DOCUMENTS_PATH,
    enable_rag=True,
)
```

## Usage
```bash
python Orchestrator_RAG.py
```

### Commands
- Present your research question
- Type `exit` or `quit` to end the session
- Press `Ctrl+C` to interrupt

## Code Structure
```python
# Main components:
1. LLM Configuration: set_llm() with streaming
2. Document Setup: Create data directory and sample document
3. Agent Creation: Professor and Research Assistant agents
4. Orchestrator Setup: Research lab orchestrator
5. Research Session Loop: Interactive Q&A
6. Cleanup: Graceful shutdown
```

## RAG Configuration
The system automatically creates a sample document if none exists:
```python
DOCUMENTS_PATH = os.path.join(os.path.dirname(__file__), "data")

sample_content = """
DAIE (Decentralized AI Ecosystem) is an open-source Python library 
for building multi-agent AI systems.
Key features:
- Unified Orchestrator model for agent coordination
- RAG support for document-based knowledge
"""
```

## Example Session
```
You (Court Clerk): What is DAIE?

Judge_Justice is presiding over the case...

Final Verdict/Guidance from Judge:
Based on the research conducted by my assistant NOVA, DAIE (Decentralized AI Ecosystem) is an open-source Python library designed for building multi-agent AI systems. The key features include a unified Orchestrator model for agent coordination and RAG support for document-based knowledge.

------------------------------
```

## How It Works
1. **User Input**: User presents a research question
2. **Orchestration**: Professor receives the input and coordinates with NOVA
3. **RAG Retrieval**: NOVA retrieves relevant document chunks
4. **Analysis**: NOVA analyzes the documents and provides answers
5. **Synthesis**: Professor synthesizes the information
6. **Display**: Final answer is displayed to the user

## Document Management
### Adding Documents
1. Place your documents (PDF, TXT) in the `./data` directory
2. The system will automatically load and index them
3. Agents can then answer questions based on the document content

### Supported Formats
- Plain text files (.txt)
- PDF files (.pdf) - requires PyPDF2
- Other formats can be added with custom loaders

## Customization
You can modify the agents' behavior by adjusting their configurations:
- Change the professor's coordination style
- Modify the research assistant's analysis approach
- Adjust temperature settings for different response styles
- Add more sub-agents for specialized tasks

## Use Cases
- Research assistance
- Document analysis
- Knowledge base querying
- Academic Q&A systems
- Multi-agent research collaboration

## Error Handling
The application handles:
- Keyboard interrupts (Ctrl+C)
- Empty input (ignored)
- JSON parsing errors (displays raw response)
- Agent communication errors
- Missing documents (creates sample)
