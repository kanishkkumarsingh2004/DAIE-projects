# RAG-Powered Chat Agent

## Description
An advanced chat application demonstrating Retrieval-Augmented Generation (RAG) capabilities in the DAIE library. This example shows how to create an AI agent that can answer questions based on your own documents (PDF, TXT).

## Features
- **RAG Integration**: Document-based knowledge retrieval
- **Document Support**: PDF and TXT file processing
- **Streaming Responses**: Real-time streaming of AI responses
- **Source Citation**: Agent cites document chunks in answers
- **Customizable Personality**: Configurable agent behavior
- **Interactive Chat**: Real-time conversation interface

## Prerequisites
- Python 3.7+
- DAIE library installed
- Ollama running with `llama3.2:1b` model
- RAG dependencies:
  ```bash
  pip install PyPDF2 sentence-transformers faiss-cpu
  ```
- Documents in the `./data` directory

## Configuration
The agent is configured with the following settings:
- **Name**: NOVA
- **Role**: General Purpose
- **Personality**: Precise, helpful, and thorough
- **Gender**: Female
- **Behavior**: Always cites the source document chunk in your answer
- **Temperature**: 0.3 (factual answers)
- **Max Tokens**: 1024
- **RAG**: Enabled with document path

## Usage
```bash
python rag_chat.py
```

### Commands
- Type your question and press Enter
- Type `exit` or `quit` to end the session
- Press `Ctrl+C` to interrupt

## Code Structure
```python
# Main components:
1. LLM Configuration: set_llm() with streaming
2. Document Path Setup: Configure documents directory
3. Agent Configuration: AgentConfig with RAG settings
4. Agent Initialization: Agent creation and startup
5. Chat Loop: Interactive Q&A with document retrieval
6. Cleanup: Graceful shutdown
```

## RAG Configuration
```python
DOCUMENTS_PATH = os.path.join(os.path.dirname(__file__), "data")

config = AgentConfig(
    name="NOVA",
    role=AgentRole.GENERAL_PURPOSE,
    system_prompt=(
        "You are a knowledgeable assistant. Use the provided document context "
        "to answer questions accurately. If the context doesn't contain the "
        "answer, say so honestly."
    ),
    personality="precise, helpful, and thorough",
    gender="female",
    behavior="always cites the source document chunk in your answer",
    temperature=0.3,
    max_tokens=1024,
    rag_document_path=DOCUMENTS_PATH,
    enable_rag=True,
)
```

## Setting Up Documents
### Directory Structure
```
project/
├── rag_chat.py
└── data/
    ├── knowledge_base.txt
    ├── documentation.pdf
    └── research_notes.txt
```

### Adding Documents
1. Create a `data` directory in the same folder as the script
2. Place your documents (PDF, TXT) in the `data` directory
3. The agent will automatically load and index them

### Supported Formats
- **Plain Text (.txt)**: Direct text processing
- **PDF (.pdf)**: Requires PyPDF2 library
- **Other formats**: Can be added with custom loaders

## Example Session
```
=== RAG Chat (Document-Powered) ===
📂 Documents loaded from: /path/to/data
Type 'exit' to quit.

You: What is DAIE?
NOVA: Based on the document context, DAIE (Decentralized AI Ecosystem) is an open-source Python library for building multi-agent AI systems. The key features include a unified Orchestrator model for agent coordination and RAG support for document-based knowledge.

[Source: knowledge_base.txt]

You: How does RAG work?
NOVA: According to the documentation, RAG (Retrieval-Augmented Generation) works by first retrieving relevant document chunks based on the user's query, then using those chunks as context for the AI to generate accurate answers. This approach ensures responses are grounded in your actual documents.

[Source: documentation.pdf]

You: exit
```

## How RAG Works
1. **Document Loading**: Documents are loaded from the specified path
2. **Chunking**: Documents are split into manageable chunks
3. **Embedding**: Chunks are converted to vector embeddings
4. **Indexing**: Embeddings are stored in a vector database
5. **Retrieval**: User query is matched against document chunks
6. **Generation**: AI generates answer using retrieved context
7. **Citation**: Source document chunk is cited in the response

## Customization
You can modify the agent's behavior by adjusting the `AgentConfig`:
- `system_prompt`: Define how the agent uses documents
- `personality`: Adjust response style
- `behavior`: Set citation preferences
- `temperature`: Control response creativity (0.0-1.0)
- `max_tokens`: Limit response length
- `rag_document_path`: Path to your documents
- `enable_rag`: Enable/disable RAG functionality

## Use Cases
- Knowledge base querying
- Document analysis
- Research assistance
- Customer support with documentation
- Educational Q&A systems
- Technical documentation search

## Performance Considerations
- **Document Size**: Larger documents require more processing time
- **Chunk Size**: Affects retrieval accuracy and speed
- **Embedding Model**: Impacts quality and performance
- **Vector Database**: Choice affects scalability

## Troubleshooting
### Common Issues
1. **No documents found**: Ensure documents are in the `./data` directory
2. **PDF errors**: Install PyPDF2 with `pip install PyPDF2`
3. **Slow responses**: Consider reducing document size or chunk size
4. **Poor answers**: Check document quality and relevance

### Dependencies
```bash
pip install PyPDF2 sentence-transformers faiss-cpu
```

## Error Handling
The application handles:
- Keyboard interrupts (Ctrl+C)
- Missing documents (creates sample)
- Document loading errors
- API errors (displayed to user)
- Empty input (ignored)
