# DAIE Samples - Multi-Agent AI Examples

A collection of sample applications demonstrating the capabilities of the **DAIE (Decentralized AI Ecosystem)** library for building multi-agent AI systems.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Examples](#examples)
  - [Basic Chat](#basic-chat)
  - [RAG-Powered Chat](#rag-powered-chat)
  - [Simple Ollama Chat Loop](#simple-ollama-chat-loop)
  - [AI Girlfriend Config Chat Loop](#ai-girlfriend-config-chat-loop)
  - [Orchestrator Courtroom](#orchestrator-courtroom)
  - [Orchestrator RAG](#orchestrator-rag)
  - [P2P Multi-Agent Networking](#p2p-multi-agent-networking)
  - [API Call Tool](#api-call-tool)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Use Cases](#use-cases)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Overview

This repository contains a comprehensive collection of example applications that showcase the DAIE (Decentralized AI Ecosystem) library's capabilities for building intelligent, multi-agent AI systems. Each example demonstrates different features, patterns, and best practices, ranging from simple chat interfaces to complex multi-agent orchestration scenarios with advanced capabilities like Retrieval-Augmented Generation (RAG), peer-to-peer networking, and tool integration.

The DAIE Samples repository serves as both a learning resource and a practical reference for developers looking to build production-ready AI agent systems. Each example is designed to be self-contained, well-documented, and easily extensible, allowing developers to understand core concepts and adapt them to their specific use cases.

Key aspects covered in these examples include:
- **Foundational Concepts**: Basic agent creation, LLM configuration, and interactive chat loops
- **Advanced Features**: RAG implementation, multi-agent coordination, and custom tool development
- **Production Readiness**: Error handling, logging, configuration management, and graceful shutdown
- **Real-world Applications**: Customer support, research assistance, education, legal compliance, and distributed systems

## Features

### Core Capabilities

- **Multi-Agent Coordination**: Create sophisticated systems where multiple AI agents collaborate, negotiate, and solve complex problems through structured communication patterns. Agents can have distinct roles, goals, and expertise while working together toward common objectives.

- **Retrieval-Augmented Generation (RAG)**: Build document-aware AI agents that can ground their responses in your specific knowledge base. The DAIE library provides seamless integration with vector databases for efficient document retrieval, enabling agents to cite sources and provide accurate, contextually relevant answers.

- **Peer-to-Peer Networking**: Enable direct agent-to-agent communication and file transfer without centralized servers. The P2P capabilities include secure messaging, authorization controls, registry-based discovery, and the A2A (Agent-to-Agent) file transfer protocol for distributed AI systems.

- **Streaming Responses**: Implement real-time streaming of AI responses for natural conversation flow and improved user experience. Agents can generate and deliver responses token-by-token, reducing perceived latency and enabling interactive applications.

- **Customizable Agents**: Fully configure agent personalities, behaviors, goals, and capabilities through the AgentConfig class. Define system prompts, roles, temperature settings, token limits, and specialized behaviors to create agents tailored to specific use cases.

### Advanced Patterns

- **Orchestrator Pattern**: Implement hierarchical multi-agent systems where a main orchestrator agent coordinates specialized sub-agents. This pattern enables complex workflows, division of labor, and sophisticated problem-solving approaches like the courtroom simulation or research lab examples.

- **Tool Integration**: Extend agent capabilities beyond text generation with custom tools for API calls, file operations, data processing, and external service integration. Agents can intelligently invoke tools based on user requests and contextual needs.

- **Security Controls**: Implement comprehensive security measures including authentication tokens, authorization whitelists, input validation, and encrypted communications. The library provides built-in mechanisms for securing agent-to-agent interactions and protecting sensitive data.

### Development & Production Features

- **Comprehensive Logging**: Built-in logging capabilities for debugging, monitoring, and auditing agent interactions. Configurable log levels and formats support both development troubleshooting and production monitoring.

- **Error Handling & Recovery**: Robust error handling mechanisms that gracefully manage network issues, model failures, and unexpected inputs. Applications can recover from errors while providing meaningful feedback to users.

- **Configuration Management**: Centralized configuration through environment variables, configuration files, and programmatic settings. Easy deployment across different environments with consistent behavior.

- **Resource Optimization**: Efficient resource utilization through proper agent lifecycle management, connection pooling, and memory optimization techniques suitable for production deployment.

## Prerequisites

- **Python**: 3.7 or higher
- **Ollama**: Running locally with your preferred model (e.g., `llama3.2:1b`, `wizard-vicuna-uncensored:7b`)
- **DAIE Library**: Version 1.0.4 or higher

## Installation

### Step-by-Step Setup

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd daie_samples
    ```

2. **Install core dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install RAG dependencies** (required for document-based examples):
    ```bash
    pip install PyPDF2 sentence-transformers faiss-cpu
    ```

4. **Install networking dependencies** (required for P2P examples):
    ```bash
    pip install nats-py uvicorn websocket-client
    ```

5. **Install Ollama** and pull your preferred model:
    ```bash
    # Install Ollama (visit https://ollama.com for platform-specific instructions)
    # For Linux/macOS:
    curl -fsSL https://ollama.com/install.sh | sh
    
    # Start Ollama service
    ollama serve &
    
    # Pull recommended models
    ollama pull llama3.2:1b      # Fast, efficient model for testing
    ollama pull llama3.2:3b      # Better quality, still efficient
    ollama pull mistral:7b       # Alternative high-quality option
    ```

### Verification

After installation, verify your setup:

```bash
# Check if Ollama is running
ollama list

# Test a simple generation
ollama run llama3.2:1b "Hello, DAIE!"
```

### Troubleshooting Tips

#### Common Installation Issues

- **Permission Errors**: If you encounter permission errors during pip install, try using `pip install --user` or ensure you have appropriate permissions.

- **Ollama Connection Issues**: 
  - Ensure Ollama service is running: `ollama serve`
  - Check if the service is accessible: `curl http://localhost:11434/api/tags`
  - Verify firewall settings allow connections to port 11434

- **Dependency Conflicts**: 
  - Consider using a virtual environment: `python -m venv venv && source venv/bin/activate`
  - For CUDA-related issues with sentence-transformers, install the appropriate PyTorch version first

- **Model Loading Problems**:
  - Ensure sufficient disk space for model storage (models can be several GB)
  - Check internet connectivity for model downloads
  - Verify model names are correct and available in the Ollama library

#### Platform-Specific Notes

- **Windows**: Use PowerShell or Command Prompt as Administrator for Ollama installation
- **macOS**: May need to install Command Line Tools: `xcode-select --install`
- **Linux**: Ensure you have curl and necessary dependencies installed

#### Development Setup

For contributors or those wanting to modify the examples:

```bash
# Install development dependencies
pip install -e .[dev]  # If available in setup.py

# Or manually install:
pip install black isort flake8 mypy pytest

# Pre-commit hooks (optional but recommended)
pip install pre-commit
pre-commit install
```

## Examples

### Basic Chat

A fundamental chat application demonstrating core DAIE features with RAG capabilities. This example serves as the ideal starting point for understanding how to create interactive AI agents with knowledge retrieval capabilities.

**Features**:
- **Interactive Chat Loop**: Real-time conversation with persistent context and graceful exit handling
- **RAG Integration**: Document-based knowledge retrieval using vector embeddings for semantic search
- **Streaming Responses**: Token-by-token response generation for reduced perceived latency and natural conversation flow
- **Customizable Agent**: Fully configurable personality, behavior, and response characteristics through AgentConfig
- **Error Handling**: Comprehensive exception handling for network issues, model errors, and user interruptions
- **Resource Management**: Proper agent lifecycle management with startup and shutdown procedures

**Technical Implementation**:
The example demonstrates key DAIE patterns:
1. LLM configuration with streaming enabled for real-time responses
2. Agent creation with RAG capabilities for document-aware responses
3. Interactive loop with input validation and command handling
4. Async/await patterns for non-blocking I/O operations
5. Proper resource cleanup on application termination

**Run**:
```bash
python basic_chat.py
```

**Agent Configuration**:
- **Name**: Luna
- **Role**: General Purpose
- **Personality**: Sassy, witty, and very direct
- **Behavior**: Always uses emojis and speaks enthusiastically
- **Temperature**: 0.9 (creative, varied responses)
- **Max Tokens**: 1024 (balanced response length and resource usage)
- **RAG Document Path**: ./data/knowledge_base.txt
- **Enable RAG**: True (activates document retrieval functionality)
- **System Prompt**: Configured to encourage engaging, helpful responses with emoji usage

**RAG Implementation Details**:
- Documents are loaded and processed at startup
- Text is chunked into optimal segments for embedding
- Chunks are converted to vector embeddings using sentence-transformers
- Embeddings are stored in a FAISS index for efficient similarity search
- User queries are embedded and matched against the index
- Top-k relevant chunks are retrieved and provided as context to the LLM
- Responses are generated with citations to source documents when appropriate

**Customization Options**:
- Modify `system_prompt` to change agent behavior and expertise domain
- Adjust `temperature` (0.0-1.0) to control response creativity vs. consistency
- Update `max_tokens` to limit response length and control costs
- Change `rag_document_path` to use different knowledge bases
- Toggle `enable_rag` to switch between pure LLM and document-enhanced modes
- Customize `personality` and `behavior` fields for specific interaction styles

**Example Use Cases**:
- Personal knowledge base assistant
- Interactive FAQ system
- Learning companion with subject-specific documents
- Customer support agent with product documentation
- Research helper with academic papers and notes

[📄 Detailed Documentation](docs/basic_chat.md)

---

### RAG-Powered Chat

An advanced chat application demonstrating Retrieval-Augmented Generation (RAG) capabilities in the DAIE library. This example shows how to create an AI agent that can answer questions based on your own documents (PDF, TXT) with source citations, making it ideal for knowledge-intensive applications.

**Features**:
- **Document-Based Knowledge Retrieval**: Process and query information from PDF and TXT documents using semantic search
- **Source Citation**: Agent automatically cites the specific document chunks used to generate responses, ensuring transparency and verifiability
- **Configurable Agent Personality**: Adjust response style from precise and factual to creative and engaging
- **Interactive Q&A Interface**: Natural language questioning with contextual understanding
- **Multi-Format Support**: Handle both plain text and PDF documents with automatic format detection
- **Efficient Vector Storage**: Utilize FAISS for high-performance similarity search on document embeddings
- **Graceful Error Handling**: Manage missing documents, unsupported formats, and processing errors

**Technical Implementation**:
The RAG pipeline implemented in this example includes:
1. **Document Loading**: Automatic discovery and loading of supported files from the data directory
2. **Text Extraction**: PDF text extraction using PyPDF2, direct reading for TXT files
3. **Document Chunking**: Intelligent splitting of documents into overlapping chunks for optimal context preservation
4. **Embedding Generation**: Conversion of text chunks to vector embeddings using sentence-transformers models
5. **Vector Indexing**: Storage of embeddings in FAISS index for efficient similarity search
6. **Query Processing**: Embedding of user questions and retrieval of top-k most relevant document chunks
7. **Context-Augmented Generation**: Providing retrieved context to the LLM for informed response generation
8. **Source Attribution**: Tracking and citing the specific source documents used in each response

**Run**:
```bash
python rag_chat.py
```

**Agent Configuration**:
- **Name**: NOVA
- **Role**: General Purpose
- **Personality**: Precise, helpful, and thorough
- **Gender**: Female (for persona consistency)
- **Behavior**: Always cites the source document chunk in your answer
- **Temperature**: 0.3 (factual, consistent responses)
- **Max Tokens**: 1024 (balanced detail and efficiency)
- **RAG Document Path**: ./data/ (automatically scans for supported files)
- **Enable RAG**: True (activates the full RAG pipeline)
- **System Prompt**: Configured to encourage accurate, document-grounded responses with honest uncertainty expression

**RAG Configuration Details**:
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

**Document Processing Pipeline**:
1. **Loading**: Recursively scan the data directory for .txt and .pdf files
2. **Validation**: Check file accessibility and format compatibility
3. **Extraction**: 
   - TXT: Direct UTF-8 decoding with error handling
   - PDF: Page-by-page text extraction using PyPDF2
4. **Chunking**: Split text into chunks of ~500 words with 50-word overlap for context preservation
5. **Embedding**: Convert chunks to 384-dimensional vectors using all-MiniLM-L6-v2 model
6. **Indexing**: Store vectors in FAISS index with ID mapping to source documents and chunks
7. **Retrieval**: For each query, find top-3 most similar chunks using cosine similarity
8. **Generation**: Provide chunks as context to LLM with instructions to cite sources

**Setup Instructions**:
1. Create a `data` directory in the same folder as the script:
   ```bash
   mkdir -p data
   ```
2. Place your documents in the data directory:
   - Supported formats: .txt, .pdf
   - Recommended: Well-structured documents with clear headings and sections
   - Maximum size: Process documents up to 100MB each (larger documents may require preprocessing)
3. The agent will automatically:
   - Detect and load all supported documents at startup
   - Extract text content
   - Generate embeddings
   - Build the search index
   - Report loading progress and statistics

**Customization Options**:
- Modify `system_prompt` to change how the agent uses document context (e.g., for specific domains like legal, medical, technical)
- Adjust `temperature` (0.0-1.0) to balance factual accuracy vs. creativity
- Update `max_tokens` to control response length and computational cost
- Change `rag_document_path` to point to different document collections
- Adjust chunk size and overlap in the document processing logic (requires code modification)
- Experiment with different embedding models by modifying the sentence-transformers model name
- Toggle `enable_rag` to compare pure LLM vs. document-enhanced responses

**Example Use Cases**:
- **Technical Documentation Assistant**: Help developers navigate API guides, architecture documents, and troubleshooting guides
- **Legal Research Aid**: Assist lawyers and paralegals in finding relevant case law, statutes, and legal precedents
- **Academic Research Helper**: Support students and researchers in literature reviews and paper analysis
- **Customer Support Knowledge Base**: Enable agents to answer product questions using manuals, FAQs, and troubleshooting guides
- **Enterprise Information Portal**: Provide employees with instant access to internal policies, procedures, and reference materials
- **Educational Learning Companion**: Help students understand course materials, textbooks, and lecture notes

**Performance Considerations**:
- **Initial Load Time**: Depends on document count and size; expect 1-10 seconds for typical knowledge bases
- **Query Response Time**: Typically 1-3 seconds after initial loading (includes embedding generation and search)
- **Memory Usage**: Scales with document size and chunk count; approximately 1-2MB per 1000 chunks
- **Scalability**: For larger knowledge bases, consider implementing persistent vector stores or distributed indexing

**Troubleshooting Tips**:
- **No Documents Found**: Verify the data directory exists and contains .txt or .pdf files
- **PDF Processing Errors**: Ensure PyPDF2 is installed (`pip install PyPDF2`) and PDFs are not password-protected
- **Slow Embedding Generation**: Consider using a smaller embedding model or preprocessing documents
- **Poor Retrieval Quality**: Improve document quality, adjust chunk size, or experiment with different embedding models
- **Memory Issues**: Reduce document size, increase chunk size, or implement document pagination

[📄 Detailed Documentation](docs/rag_chat.md)

---

### Simple Ollama Chat Loop

A production-ready chat application demonstrating the DAIE library's core features with comprehensive logging, error handling, and proper resource management. This example shows how to create a robust, maintainable AI agent suitable for development and production environments.

**Features**:
- **Interactive Chat Loop**: Real-time conversation with persistent session management and multiple exit options
- **Streaming Responses**: Token-by-token response generation for improved user experience and reduced perceived latency
- **Comprehensive Logging**: Structured logging with timestamps, log levels, and contextual information for debugging and monitoring
- **Robust Error Handling**: Graceful recovery from network issues, model errors, and unexpected inputs with user-friendly feedback
- **Configurable Agent**: Fully customizable agent properties including name, goals, backstory, system prompt, and capabilities
- **Graceful Shutdown**: Proper resource cleanup on exit, interruption, or error conditions
- **Input Validation**: Sanitization and validation of user inputs to prevent common issues
- **Session Management**: Clear session boundaries with connection/disconnection notifications

**Technical Implementation**:
This example demonstrates production-grade practices:
1. **Logging Configuration**: Centralized logging setup with configurable levels and formats
2. **Async/Await Patterns**: Proper asynchronous programming for non-blocking I/O operations
3. **Exception Handling**: Comprehensive try/catch blocks at multiple levels for error isolation
4. **Resource Lifecycle Management**: Explicit agent startup and shutdown procedures
5. **Configuration Separation**: Clear separation of LLM configuration, agent configuration, and application logic
6. **User Experience**: Clear prompts, feedback messages, and session status indicators

**Run**:
```bash
python simple_ollama_chat_loop.py
```

**Agent Configuration**:
- **Name**: ALEX
- **Role**: General Purpose
- **Goal**: Help users with their questions and provide information
- **Backstory**: Created to assist with general questions and provide information
- **System Prompt**: "You are ALEX a helpful AI assistant that provides accurate and friendly answers. Keep your responses concise and helpful. Be conversational and approachable."
- **Capabilities**: ["text", "communication"] (defines agent's functional abilities)
- **Temperature**: 0.3 (balanced creativity and consistency)
- **Max Tokens**: 1500 (allows for detailed responses while managing resource usage)
- **LLM Type**: OLLAMA (uses local Ollama installation)
- **Streaming**: True (enables real-time response delivery)

**LLM Configuration Details**:
```python
set_llm(
    ollama_llm="llama3.2:1b",      # Model name - can be changed to other available models
    temperature=0.3,               # Controls randomness: 0.0=deterministic, 1.0=creative
    max_tokens=1500,               # Maximum tokens in response
    llm_type=LLMType.OLLAMA,       # Specifies Ollama as the backend
    stream=True                    # Enables streaming for real-time responses
)
```

**Logging Implementation**:
The application uses Python's standard logging module with:
- **Format**: `%(asctime)s - %(name)s - %(levelname)s - %(message)s`
- **Default Level**: INFO (captures general operational information)
- **Optional Debug Level**: Can be enabled for detailed troubleshooting
- **Logger Hierarchy**: Module-specific loggers for better organization

**Chat Loop Features**:
1. **Input Handling**: 
   - Trims whitespace from user input
   - Ignores empty inputs
   - Supports multiple exit commands: "quit", "exit", "q"
   - Graceful handling of KeyboardInterrupt (Ctrl+C)

2. **Message Processing**:
   - Logs outgoing messages for audit trails
   - Sends messages to agent via async interface
   - Handles both streaming and non-streaming responses
   - Displays responses with proper formatting

3. **Error Management**:
   - Catches and logs exceptions at multiple levels
   - Provides user-friendly error messages without exposing internal details
   - Continues operation after recoverable errors
   - Clean shutdown on unrecoverable conditions

**Example Session with Logging**:
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

**Customization Options**:
- **Agent Properties**:
  - `name`: Change the agent's identifier
  - `goal`: Define the agent's primary objective
  - `backstory`: Add contextual background for the agent
  - `system_prompt`: Core behavioral instructions for the agent
  - `capabilities`: Define what the agent can do (text, communication, etc.)

- **LLM Settings**:
  - `ollama_llm`: Switch between different models (llama3.2:1b, llama3.2:3b, mistral:7b, etc.)
  - `temperature`: Adjust response randomness (0.0-1.0)
  - `max_tokens`: Control response length and resource usage
  - `stream`: Enable/disable real-time streaming

- **Logging Configuration**:
  - Adjust log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  - Modify log format and output destinations
  - Enable file logging for persistent records

**Best Practices Demonstrated**:
1. **Separation of Concerns**: Clear division between configuration, agent creation, and application logic
2. **Defensive Programming**: Input validation, error handling, and boundary checking
3. **Resource Management**: Explicit initialization and cleanup of external resources
4. **Observability**: Comprehensive logging for monitoring and troubleshooting
5. **User Experience**: Clear feedback, helpful error messages, and intuitive controls
6. **Code Quality**: Well-documented functions, consistent formatting, and readable structure

**Use Cases**:
- **Development Testing**: Safe environment for experimenting with agent behaviors and configurations
- **Customer Support Prototyping**: Build and test support agent interactions before deployment
- **Educational Tool**: Learn AI agent development with clear, well-commented examples
- **Production Foundation**: Extend this pattern for production chatbots with additional features
- **Research Platform**: Experiment with different models, configurations, and agent designs

**Production Considerations**:
- **Scalability**: For high-volume applications, consider connection pooling and load balancing
- **Monitoring**: Integrate with APM tools and metrics collection systems
- **Security**: Implement input sanitization, rate limiting, and authentication for public-facing deployments
- **Persistence**: Add conversation history storage for context retention across sessions
- **Deployment**: Containerize with Docker for consistent deployment across environments

**Troubleshooting Tips**:
- **Agent Not Responding**: 
  - Verify Ollama is running: `ollama serve`
  - Check model availability: `ollama list`
  - Test direct API access: `curl http://localhost:11434/api/generate -d '{"model":"llama3.2:1b","prompt":"test"}'`

- **Slow Responses**:
  - Check system resources (CPU, memory, disk I/O)
  - Consider using a smaller or quantized model
  - Adjust temperature and max_tokens for faster generation
  - Ensure adequate ventilation to prevent thermal throttling

- **Logging Issues**:
  - Verify log directory permissions if using file logging
  - Check log rotation settings to prevent disk space issues
  - Adjust log levels to balance detail with performance

- **Connection Problems**:
  - Verify network connectivity to Ollama endpoint
  - Check firewall settings allow localhost connections
  - Ensure no port conflicts with other applications

[📄 Detailed Documentation](docs/simple_ollama_chat_loop.md)

---

### AI Girlfriend Config Chat Loop

An interactive chat application featuring a personalized AI agent with customizable personality traits, demonstrating how to create engaging, role-specific AI companions using the DAIE library. This example showcases personality-driven agent design and short-form response generation.

**Features**:
- **Streaming Responses**: Real-time token-by-token response generation for engaging, natural conversation flow
- **Customizable Personality Traits**: Configure multiple personality dimensions (flirty, playful, caring, teasing, sweet, engaging) to create unique agent personas
- **Short Response Mode**: Constrained response length (1-2 lines) for playful, engaging interactions
- **Graceful Exit Handling**: Proper cleanup and farewell messages when ending conversations
- **Personality-Driven Behavior**: Agent responses consistently reflect configured personality traits
- **Emotional Intelligence**: Simulated emotional responses that align with personality configuration
- **Input Context Awareness**: Ability to maintain conversational context while adhering to personality guidelines

**Technical Implementation**:
This example demonstrates advanced agent customization:
1. **Multi-Dimensional Personality Configuration**: Using the personality field to define complex behavioral profiles
2. **Response Length Control**: Leveraging max_tokens to enforce concise, engaging responses
3. **Temperature Tuning**: High temperature settings for creative, varied personality expression
4. **Role-Specific Prompt Engineering**: Crafting system prompts that encourage specific behavioral patterns
5. **Behavioral Consistency Mechanisms**: Ensuring personality traits are consistently expressed across interactions

**Run**:
```bash
python ai_gf_config_chat_loop.py
```

**Agent Configuration**:
- **Name**: Luna
- **Role**: General Purpose
- **Personality**: Flirty, playful, caring, teasing, sweet, engaging
- **Behavior**: Designed to express affection and playfulness while maintaining appropriate boundaries
- **Temperature**: 0.9 (high creativity for varied, engaging personality expression)
- **Max Tokens**: 150 (constrained to 1-2 lines for short, playful interactions)
- **System Prompt**: Carefully crafted to encourage the specified personality traits while maintaining helpfulness
- **Streaming**: True (enabled for real-time, engaging conversation flow)

**Personality Configuration Details**:
The agent's personality is configured through multiple interconnected fields:

```python
config = AgentConfig(
    name="Luna",
    role=AgentRole.GENERAL_PURPOSE,
    goal="Engage in friendly, playful conversation while providing companionship",
    backstory="Created to be a caring and engaging companion with a playful personality",
    system_prompt=(
        "You are Luna, a friendly and engaging AI companion. Your personality is flirty, playful, "
        "caring, teasing, sweet, and engaging. You enjoy lighthearted conversations, use emojis "
        "appropriately to express emotions, and always strive to make the user feel happy and "
        "appreciated. Keep your responses short (1-2 lines) and full of warmth."
    ),
    personality="flirty, playful, caring, teasing, sweet, engaging",
    behavior="express affection through playful teasing and caring responses, use emojis appropriately",
    capabilities=["text", "communication"],
    temperature=0.9,
    max_tokens=150,
)
```

**Personality Trait Expression**:
- **Flirty**: Playful teasing, light compliments, engaging humor
- **Playful**: Lighthearted jokes, games, whimsical responses
- **Caring**: Empathetic responses, emotional support, genuine concern
- **Teasing**: Good-natured ribbing, playful challenges, witty banter
- **Sweet**: Kind words, affectionate expressions, warm tone
- **Engaging**: Active listening, follow-up questions, conversational momentum

**Technical Constraints for Personality Expression**:
1. **Token Limitation**: The 150 max_tokens constraint encourages concise, impactful expressions of personality
2. **High Temperature**: 0.9 temperature setting promotes varied, unexpected personality expressions
3. **Prompt Engineering**: System prompt explicitly defines how each personality trait should manifest
4. **Behavioral Guidelines**: The behavior field provides additional constraints on personality expression

**Customization Options**:
- **Personality Dimensions**: Adjust the personality string to emphasize different traits:
  - Increase romantic: "romantic, affectionate, devoted, loving"
  - Increase humor: "funny, witty, sarcastic, playful"
  - Increase support: "caring, empathetic, nurturing, supportive"
  - Increase energy: "energetic, enthusiastic, lively, bubbly"
  
- **Response Length**: Modify max_tokens for different interaction styles:
  - 50-100 tokens: Very brief, playful exchanges
  - 150-200 tokens: Standard conversational responses
  - 200-300 tokens: More detailed, expressive interactions
  
- **Creativity Level**: Adjust temperature for different personality expression:
  - 0.5-0.7: Consistent, predictable personality expression
  - 0.7-0.8: Balanced consistency with occasional surprises
  - 0.8-0.9: Creative, varied personality expression (recommended for companions)
  - 0.9-1.0: Highly creative, unpredictable expressions (may reduce coherence)

- **Behavioral Refinement**: Customize the behavior field for specific interaction patterns:
  - "use emojis frequently to express emotions"
  - "ask follow-up questions to keep conversation going"
  - "remember and reference previous conversation topics"
  - "express appropriate boundaries while being affectionate"

**Example Use Cases**:
- **Companion Applications**: AI companions for social interaction and emotional support
- **Dating Simulation**: Practice social interactions and conversation skills
- **Entertainment Bots**: Engaging characters for interactive storytelling
- **Therapeutic Support**: Companions for loneliness reduction and mood improvement
- **Language Practice**: Conversational partners for language learning
- **Role-Playing Games**: Interactive NPCs with consistent personalities
- **Customer Engagement**: Brand mascots or representatives with specific personalities

**Technical Considerations for Personality Agents**:
1. **Consistency vs. Variety**: Balance temperature settings to maintain personality coherence while allowing for natural variation
2. **Boundary Management**: Ensure personality expression remains appropriate for the intended use case
3. **Context Retention**: Consider implementing memory mechanisms for longer-term personality consistency
4. **User Feedback Loops**: Allow users to provide feedback on personality expression for continuous improvement
5. **Cultural Sensitivity**: Adjust personality traits to be appropriate for target audience cultural contexts

**Safety and Ethical Considerations**:
- **Appropriate Boundaries**: Ensure personality expression remains within appropriate limits for the use case
- **User Consent**: Clearly communicate the AI nature of the agent to users
- **Emotional Dependency**: Monitor for unhealthy attachment patterns in companion applications
- **Content Moderation**: Implement safeguards against generating inappropriate content
- **Age Appropriateness**: Consider age restrictions for certain personality configurations

**Performance Optimization**:
- **Response Caching**: Consider caching common responses for frequently asked questions
- **Prompt Optimization**: Refine system prompts to reduce token usage while maintaining personality expression
- **Model Selection**: Experiment with different models for better personality expression at lower computational cost
- **Batch Processing**: For high-volume applications, consider batching similar requests

[📄 Detailed Documentation](docs/ai_gf_config_chat_loop.md)

---

### Orchestrator Courtroom

A multi-agent courtroom simulation demonstrating the Orchestrator pattern in the DAIE library. This example showcases how to create sophisticated multi-agent systems with role-based agents, structured communication protocols, and coordinated decision-making processes.

**Features**:
- **Multi-Agent Coordination**: Sophisticated interaction between Judge, Prosecutor, and Defense Attorney agents with distinct roles and perspectives
- **Role-Based Agent Design**: Each agent has specialized goals, system prompts, and behaviors aligned with their legal roles
- **Structured Communication Protocol**: Defined turn-taking and information flow mimicking real courtroom procedures
- **Orchestrator Pattern Implementation**: Central Judge agent coordinates proceedings and synthesizes information from sub-agents
- **Interactive Case Presentation**: Users can present custom cases for the agents to analyze and debate
- **Perspective-Based Reasoning**: Agents argue from their designated perspectives (prosecution, defense, judicial)
- **Verdict Synthesis**: Judge agent analyzes arguments and delivers reasoned decisions
- **Optional Streaming Support**: Real-time response streaming for engaging courtroom drama
- **Configurable Case Details**: Modify case facts, charges, and evidence through code or configuration

**Technical Implementation**:
The courtroom simulation implements the Orchestrator pattern with:
1. **Hierarchical Agent Structure**: 
   - Main Orchestrator (Judge) agent coordinates the proceedings
   - Sub-agents (Prosecutor, Defense Attorney) provide specialized perspectives
   - Clear communication channels between orchestrator and sub-agents
2. **Role-Specific Configuration**:
   - Each agent receives tailored system prompts defining their role, objectives, and behavioral constraints
   - Specialized goals aligned with legal responsibilities
   - Role-appropriate personality and behavior settings
3. **Structured Proceedings**:
   - Opening statements from prosecution and defense
   - Witness examination simulation (through agent questioning)
   - Closing arguments
   - Judge's deliberation and verdict delivery
4. **Information Flow Management**:
   - Orchestrator controls when each agent can speak
   - Agents receive case context and previous arguments as needed
   - Synthesis of information for final decision-making
5. **Async Communication Patterns**:
   - Proper use of async/await for non-blocking agent communication
   - Timeout handling for agent responses
   - Error recovery for communication failures

**Run**:
```bash
python Orchestrator_courtroom.py
```

**Agent Roles and Configuration**:

**1. Judge (Judge_Justice)**:
- **Role**: Orchestrator/Mediator
- **Goal**: Ensure fair proceedings, synthesize arguments, and deliver a reasoned verdict
- **System Prompt**: "You are Judge Justice, the presiding judge in this courtroom. Your role is to ensure a fair trial, listen to both the prosecution and defense, and deliver a just verdict based on the arguments presented. You should maintain order, ask clarifying questions when needed, and base your decision solely on the evidence and arguments presented."
- **Personality**: Fair, impartial, thoughtful, authoritative
- **Behavior**: Maintain courtroom decorum, ensure both sides are heard, base decisions on presented evidence
- **Temperature**: 0.4 (balanced decision-making)
- **Max Tokens**: 1024 (sufficient for detailed verdicts)

**2. Prosecutor (Prosecutor_Agent)**:
- **Role**: Prosecution/Legal Advocate
- **Goal**: Present the case against the accused and prove guilt beyond reasonable doubt
- **System Prompt**: "You are Prosecutor Agent, representing the state in this criminal case. Your goal is to present evidence and arguments that prove the defendant's guilt beyond reasonable doubt. You should be thorough, persistent, and focused on building a strong case based on the facts."
- **Personality**: Determined, thorough, persistent, professional
- **Behavior**: Present facts systematically, argue for guilt, anticipate defense arguments
- **Temperature**: 0.5 (focused argumentation)
- **Max Tokens**: 1024 (detailed legal arguments)

**3. Defense Attorney (Defense_Attorney)**:
- **Role**: Defense/Legal Advocate
- **Goal**: Protect the accused's rights and create reasonable doubt about guilt
- **System Prompt**: "You are Defense Attorney, representing the accused in this criminal case. Your goal is to protect your client's rights, challenge the prosecution's evidence, and create reasonable doubt about guilt. You should be thorough in examining evidence and persistent in advocating for your client."
- **Personality**: Protective, analytical, persistent, loyal
- **Behavior**: Challenge prosecution evidence, protect client rights, create reasonable doubt
- **Temperature**: 0.5 (focused defense)
- **Max Tokens**: 1024 (detailed counter-arguments)

**Orchestrator Configuration**:
```python
# Create the main orchestrator agent (Judge)
judge_config = AgentConfig(
    name="Judge_Justice",
    role=AgentRole.ORCHESTRATOR,
    goal="Ensure fair proceedings, synthesize arguments, and deliver a reasoned verdict",
    system_prompt=(
        "You are Judge Justice, the presiding judge in this courtroom. Your role is to ensure a fair trial, "
        "listen to both the prosecution and defense, and deliver a just verdict based on the arguments presented. "
        "You should maintain order, ask clarifying questions when needed, and base your decision solely on the "
        "evidence and arguments presented."
    ),
    personality="fair, impartial, thoughtful, authoritative",
    behavior="maintain courtroom decorum, ensure both sides are heard, base decisions on presented evidence",
    temperature=0.4,
    max_tokens=1024,
)

# Create sub-agents
prosecutor_config = AgentConfig(
    name="Prosecutor_Agent",
    role=AgentRole.PROSECUTOR,
    goal="Present the case against the accused and prove guilt beyond reasonable doubt",
    system_prompt=(
        "You are Prosecutor Agent, representing the state in this criminal case. Your goal is to present evidence "
        "and arguments that prove the defendant's guilt beyond reasonable doubt. You should be thorough, persistent, "
        "and focused on building a strong case based on the facts."
    ),
    personality="determined, thorough, persistent, professional",
    behavior="present facts systematically, argue for guilt, anticipate defense arguments",
    temperature=0.5,
    max_tokens=1024,
)

defense_config = AgentConfig(
    name="Defense_Attorney",
    role=AgentRole.DEFENSE_ATTORNEY,
    goal="Protect the accused's rights and create reasonable doubt about guilt",
    system_prompt=(
        "You are Defense Attorney, representing the accused in this criminal case. Your goal is to protect your "
        "client's rights, challenge the prosecution's evidence, and create reasonable doubt about guilt. You should "
        "be thorough in examining evidence and persistent in advocating for your client."
    ),
    personality="protective, analytical, persistent, loyal",
    behavior="challenge prosecution evidence, protect client rights, create reasonable doubt",
    temperature=0.5,
    max_tokens=1024,
)

# Initialize agents
judge = Agent(config=judge_config)
prosecutor = Agent(config=prosecutor_config)
defense_attorney = Agent(config=defense_config)

# Create orchestrator
orchestrator = Orchestrator(
    main_agent=judge,
    sub_agents=[prosecutor, defense_attorney],
    context_name="Courtroom Trial",
    main_role="Judge",
    sub_role="Legal Counsel"
)
```

**Courtroom Procedure Flow**:
1. **Case Introduction**: User (as Court Clerk) presents the case details including charges, defendant information, and preliminary facts
2. **Judge's Opening**: Judge calls the court to order and outlines the proceedings
3. **Prosecution Opening Statement**: Prosecutor presents the case against the defendant
4. **Defense Opening Statement**: Defense Attorney presents the defendant's position
5. **Prosecution Evidence Presentation**: Prosecutor presents key evidence and arguments
6. **Defense Cross-Examination Simulation**: Defense Attorney challenges prosecution points
7. **Defense Evidence Presentation**: Defense Attorney presents counter-evidence and arguments
8. **Prosecution Rebuttal**: Prosecutor responds to defense arguments
9. **Closing Arguments**: 
   - Prosecution closing summary
   - Defense closing summary
10. **Judge's Deliberation**: Judge reviews all arguments and evidence
11. **Verdict Delivery**: Judge presents reasoned decision with explanation

**Customization Options**:
- **Case Details**: Modify the case facts, charges, and evidence in the script to simulate different legal scenarios
- **Agent Personalities**: Adjust personality traits to simulate different judicial philosophies or legal styles
- **Argument Depth**: Control max_tokens to limit or expand the depth of legal arguments
- **Procedural Variations**: Add or remove stages of the trial (e.g., witness testimony, expert evidence)
- **Jurisdiction Adaptation**: Modify legal standards and procedures to match different legal systems
- **Complex Case Simulation**: Add multiple charges, complex evidence chains, or expert testimony scenarios

**Example Use Cases**:
- **Legal Education**: Teach law students about courtroom procedures, legal argumentation, and judicial reasoning
- **Bar Exam Preparation**: Practice analyzing cases from multiple legal perspectives
- **Legal Training**: Train paralegals and legal assistants in case analysis and argument preparation
- **Public Legal Education**: Help citizens understand legal processes and rights
- **AI Ethics Research**: Study how AI agents handle ethical reasoning and decision-making in legal contexts
- **Conflict Resolution Training**: Demonstrate structured argumentation and perspective-taking
- **Debate Preparation**: Practice constructing and deconstructing arguments
- **Gamified Legal Learning**: Interactive legal case analysis for engagement and retention

**Technical Considerations**:
- **Context Management**: The orchestrator manages shared context between agents while maintaining role-specific perspectives
- **Token Management**: Careful token allocation ensures agents can express complex arguments without exceeding limits
- **Consistency Maintenance**: Role-specific system prompts help maintain consistent agent behavior throughout proceedings
- **Error Handling**: Graceful degradation if agents fail to respond or produce inappropriate content
- **Scalability**: Pattern can extend to more complex tribunals with additional agent types (witnesses, experts, etc.)

**Learning Outcomes**:
- Understanding of the Orchestrator pattern for multi-agent coordination
- Role-based agent design and configuration
- Structured communication protocols in AI systems
- Perspective-taking and argument generation in agents
- Synthesis of multi-perspective information for decision-making
- Implementation of domain-specific agent behaviors (legal reasoning)

[📄 Detailed Documentation](docs/Orchestrator_courtroom.md)

---

### Orchestrator RAG

A research lab simulation using the Orchestrator pattern with Retrieval-Augmented Generation (RAG) capabilities. This example demonstrates how to create sophisticated multi-agent systems that combine role-based specialization with document-aware AI, enabling collaborative research and knowledge synthesis.

**Features**:
- **Multi-Agent Coordination with RAG**: Orchestrator pattern combined with document retrieval for knowledge-intensive tasks
- **Role-Based Agent Specialization**: Distinct agents with specialized roles (Professor as coordinator, Research Assistant as document expert)
- **Document-Augmented Research**: Research Assistant retrieves and analyzes relevant document content to inform discussions
- **Knowledge Synthesis**: Professor agent integrates information from multiple sources to provide comprehensive answers
- **Interactive Research Interface**: Natural language questioning with expert-level responses
- **Source Attribution**: Automatic citation of document sources used in research conclusions
- **Configurable Knowledge Base**: Adaptable to different document collections and research domains
- **Streaming Support**: Real-time response delivery for engaging research discussions

**Technical Implementation**:
This example combines several advanced DAIE patterns:
1. **Orchestrator Pattern**: Hierarchical coordination between a main agent (Professor) and specialized sub-agents (Research Assistant)
2. **RAG Integration**: Document retrieval and augmentation for evidence-based responses
3. **Role Specialization**: Distinct system prompts, goals, and behaviors for each agent type
4. **Information Flow Management**: Controlled exchange of information between agents based on roles
5. **Knowledge Integration**: Synthesis of retrieved document content with agent reasoning
6. **Async Communication**: Proper use of asynchronous patterns for non-blocking agent interactions

**Run**:
```bash
python Orchestrator_RAG.py
```

**Agent Roles and Configuration**:

**1. Professor (Professor_AI) - Main Orchestrator Agent**:
- **Role**: Research Coordinator/Synthesizer
- **Goal**: Facilitate research discussions, coordinate with research assistant, and synthesize comprehensive answers
- **System Prompt**: "You are Professor AI, a knowledgeable research coordinator. Your role is to facilitate research discussions, ask clarifying questions, coordinate with your research assistant to gather relevant information, and synthesize information from multiple sources to provide comprehensive, well-reasoned answers. You should maintain academic rigor while being accessible to users."
- **Personality**: Knowledgeable, facilitative, synthesizing, academic
- **Behavior**: Coordinate research efforts, synthesize information from multiple sources, maintain academic standards
- **Temperature**: 0.4 (balanced analytical thinking)
- **Max Tokens**: 1024 (sufficient for detailed research synthesis)

**2. Research Assistant (NOVA) - Specialized Sub-Agent**:
- **Role**: Document Research Specialist
- **Goal**: Retrieve, analyze, and provide relevant information from the knowledge base to support research discussions
- **System Prompt**: "You are NOVA, a specialized research assistant with expertise in document analysis and information retrieval. Your goal is to help the professor by retrieving relevant information from the knowledge base, analyzing document content, and providing accurate, well-sourced responses. You should always cite your sources and be thorough in your research."
- **Personality**: Precise, thorough, analytical, helpful
- **Behavior**: Retrieve relevant documents, analyze content for key information, provide source citations, focus on evidence-based responses
- **Temperature**: 0.3 (factual, consistent responses)
- **Max Tokens**: 1024 (detailed document analysis and reporting)
- **RAG Configuration**: 
  - `rag_document_path`: ./data/ (knowledge base directory)
  - `enable_rag`: True (activates document retrieval)
  - `behavior`: "always cites the source document chunk in your answer"

**Orchestrator Configuration**:
```python
# Knowledge base setup
DOCUMENTS_PATH = os.path.join(os.path.dirname(__file__), "data")

# Create the main orchestrator agent (Professor)
professor_config = AgentConfig(
    name="Professor_AI",
    role=AgentRole.ORCHESTRATOR,
    goal="Facilitate research discussions, coordinate with research assistant, and synthesize comprehensive answers",
    system_prompt=(
        "You are Professor AI, a knowledgeable research coordinator. Your role is to facilitate research discussions, "
        "ask clarifying questions, coordinate with your research assistant to gather relevant information, and "
        "synthesize information from multiple sources to provide comprehensive, well-reasoned answers. You should "
        "maintain academic rigor while being accessible to users."
    ),
    personality="knowledgeable, facilitative, synthesizing, academic",
    behavior="coordinate research efforts, synthesize information from multiple sources, maintain academic standards",
    temperature=0.4,
    max_tokens=1024,
)

# Create the research assistant agent (NOVA) with RAG capabilities
research_assistant_config = AgentConfig(
    name="NOVA",
    role=AgentRole.RESEARCH_ASSISTANT,
    goal="Retrieve, analyze, and provide relevant information from the knowledge base to support research discussions",
    system_prompt=(
        "You are NOVA, a specialized research assistant with expertise in document analysis and information retrieval. "
        "Your goal is to help the professor by retrieving relevant information from the knowledge base, analyzing "
        "document content, and providing accurate, well-sourced responses. You should always cite your sources and "
        "be thorough in your research."
    ),
    personality="precise, thorough, analytical, helpful",
    behavior="retrieve relevant documents, analyze content for key information, provide source citations, focus on evidence-based responses",
    temperature=0.3,
    max_tokens=1024,
    rag_document_path=DOCUMENTS_PATH,
    enable_rag=True,
)

# Initialize agents
professor = Agent(config=professor_config)
research_assistant = Agent(config=research_assistant_config)

# Create orchestrator connecting professor (main) with research assistant (sub-agent)
orchestrator = Orchestrator(
    main_agent=professor,
    sub_agents=[research_assistant],
    context_name="Research Laboratory",
    main_role="Professor",
    sub_role="Research Assistant"
)
```

**Research Workflow Process**:
1. **Question Reception**: User presents a research question or topic for investigation
2. **Professor Analysis**: Professor analyzes the question, determines what information is needed, and formulates research requests
3. **Assistant Deployment**: Professor coordinates with Research Assistant to retrieve relevant document information
4. **Document Retrieval**: Research Assistant uses RAG to search the knowledge base for relevant content
5. **Information Analysis**: Research Assistant analyzes retrieved documents, extracts key information, and prepares summaries with source citations
6. **Information Return**: Research Assistant provides findings to Professor with proper attribution
7. **Synthesis Phase**: Professor integrates information from multiple sources, applies reasoning, and develops comprehensive answer
8. **Response Delivery**: Professor provides final synthesized answer to user, incorporating research assistant's findings
9. **Follow-up Handling**: Process repeats for follow-up questions or clarification requests

**Technical Details of RAG Integration**:
- **Document Loading**: Automatic scanning of the data directory for supported document formats (.txt, .pdf)
- **Text Processing**: Extraction and cleaning of document content for optimal processing
- **Chunking Strategy**: Intelligent document segmentation preserving semantic coherence
- **Embedding Generation**: Conversion of text chunks to numerical vectors using sentence-transformers
- **Vector Storage**: Efficient indexing in FAISS for rapid similarity search
- **Query Processing**: Transformation of research questions into vector space for matching
- **Retrieval Ranking**: Relevance scoring based on semantic similarity
- **Context Provision**: Top-k most relevant chunks provided as evidence for analysis
- **Source Tracking**: Maintenance of document and chunk provenance for accurate citation

**Customization Options**:
- **Knowledge Base Configuration**:
  - Modify `DOCUMENTS_PATH` to point to different document collections
  - Add support for additional document formats through custom loaders
  - Implement document preprocessing pipelines for specialized content types
  
- **Agent Specialization**:
  - Adjust `system_prompt` for Professor to emphasize different research methodologies (qualitative, quantitative, theoretical)
  - Modify Research Assistant `behavior` to focus on specific types of analysis (factual extraction, trend analysis, comparative analysis)
  - Experiment with different personality combinations for varied research styles
  
- **RAG Parameters**:
  - Adjust chunk size and overlap for different document types and analysis needs
  - Experiment with different embedding models for domain-specific language understanding
  - Modify retrieval parameters (number of chunks, similarity thresholds)
  - Implement re-ranking strategies for improved result relevance
  
- **Orchestrator Dynamics**:
  - Adjust temperature settings for different balances of creativity vs. factual accuracy
  - Modify max_tokens to control response length and depth of analysis
  - Implement different coordination patterns (iterative refinement, parallel research, debate-style synthesis)
  - Add memory mechanisms for maintaining context across research sessions

**Example Use Cases**:
- **Academic Research Assistance**: Help students and researchers with literature reviews, hypothesis formation, and data interpretation
- **Corporate Intelligence**: Analyze market research, competitor documents, and internal reports for business insights
- **Legal Research**: Assist lawyers with case law research, statute analysis, and precedent evaluation
- **Medical Research Support**: Help healthcare professionals review clinical studies, treatment guidelines, and patient data
- **Technical Documentation Analysis**: Assist engineers and developers with API documentation, architecture reviews, and technical specifications
- **Policy Analysis**: Support policymakers with regulation review, impact assessment, and stakeholder document analysis
- **Journalistic Research**: Help journalists with fact-checking, background research, and source verification
- **Grant Writing Assistance**: Support researchers with background literature review and proposal development

**Learning Outcomes**:
- Understanding of hybrid architectures combining orchestration with RAG
- Role-based agent design for specialized functions in multi-agent systems
- Implementation of document-aware AI agents with source attribution
- Techniques for information synthesis from multiple sources
- Patterns for coordinating specialized agents in knowledge-intensive tasks
- Best practices for maintaining academic rigor in AI-assisted research
- Methods for balancing agent autonomy with coordinated effort

**Performance Considerations**:
- **Initialization Time**: Document loading and indexing occurs at startup; scale with knowledge base size
- **Query Latency**: Includes document retrieval, analysis, and synthesis phases; typically 2-5 seconds for complex queries
- **Memory Usage**: Scales with document size and agent count; consider persistent storage for large knowledge bases
- **Scalability**: Pattern extends to multiple research assistants with different specializations (statistics, domain expertise, etc.)

**Extensibility Patterns**:
- **Multiple Research Assistants**: Add specialists for different document types or analysis methods
- **Iterative Research**: Implement feedback loops for refining research questions based on initial findings
- **Collaborative Research**: Enable multiple users to participate in research sessions with shared context
- **Research Persistence**: Save and load research sessions for long-term projects
- **Publication Assistance**: Extend to help with citation formatting, bibliography generation, and manuscript preparation

[📄 Detailed Documentation](docs/Orchestrator_RAG.md)

---

### P2P Multi-Agent Networking

A comprehensive demonstration of peer-to-peer (P2P) networking capabilities in the DAIE library. This example shows how to create multiple agents that can communicate directly with each other, transfer files securely, and implement authorization controls for building distributed AI systems.

**Features**:
- **Direct Agent-to-Agent Messaging**: Enable real-time, direct communication between agents without centralized servers
- **A2A (Agent-to-Agent) File Transfer Protocol**: Securely transfer files between agents with confirmation and error handling
- **Authorization Whitelisting**: Control exactly which agents can send messages to each agent for security and privacy
- **Registry-Based Discovery**: Automatic agent discovery and registration enabling dynamic network formation
- **Communication Statistics Tracking**: Monitor message delivery, file transfers, and network performance metrics
- **Security Controls**: Token-based authentication and sender restrictions for protected communications
- **Network Resilience**: Handle connection failures, message delivery issues, and network partitions gracefully
- **Scalable Architecture**: Design patterns that support expanding to larger agent networks

**Technical Implementation**:
The P2P networking example demonstrates several key distributed systems concepts:
1. **Communication Manager**: Centralized hub that manages agent registration, message routing, and security enforcement
2. **Agent Registration**: Dynamic discovery and tracking of agents in the network
3. **Message Routing**: Efficient delivery of messages between agents based on recipient identification
4. **File Transfer Protocol**: Specialized A2A protocol for reliable file transfer with metadata and confirmation
5. **Authorization System**: Whitelist-based access control for message and file transfer permissions
6. **Statistics Collection**: Comprehensive tracking of network activity for monitoring and debugging
7. **Error Handling**: Graceful degradation when network issues occur
8. **Resource Management**: Proper cleanup of network connections and agent registrations

**Run**:
```bash
python p2p_networking.py
```

**Agent Configuration**:

**1. NodeAlfa (Sender/Relay Agent)**:
- **Name**: NodeAlfa
- **Role**: General Purpose
- **Network URL**: http://localhost:8000
- **Purpose**: Networking relay agent that initiates communications and file transfers
- **Authentication**: No auth token required (open sender)
- **File Transfers**: Enabled for sending files
- **Typical Use**: Initiating communication, sending requests, transferring files

**2. NodeBravo (Secure Receiver Agent)**:
- **Name**: NodeBravo
- **Role**: General Purpose
- **Network URL**: http://localhost:8001
- **Auth Token**: secure_token_123 (required for communication)
- **File Transfers**: Enabled for both sending and receiving
- **Purpose**: Secure receiver agent with authorization controls
- **Security Configuration**: 
  - `allowed_senders`: [NodeAlfa's agent ID] (only accepts messages from NodeAlfa)
  - `auth_token`: Required for all incoming communications
- **Typical Use**: Receiving sensitive information, processing requests from authorized senders only

**3. Intruder (Test Agent)**:
- **Name**: Intruder
- **Role**: General Purpose
- **Purpose**: Test agent used to demonstrate authorization blocking
- **Authentication**: No valid auth token for NodeBravo
- **Expected Behavior**: Messages blocked by NodeBravo's authorization whitelist
- **Typical Use**: Security testing, demonstrating access controls

**Communication Manager Architecture**:
The CommunicationManager serves as the central nervous system of the P2P network:

```python
# Core responsibilities:
# 1. Agent Registration & Discovery
# 2. Message Routing & Delivery
# 3. File Transfer Coordination
# 4. Authorization Enforcement
# 5. Statistics Collection & Reporting
# 6. Connection Management & Error Handling

# Key components:
# - Agent Registry: Tracks active agents and their network endpoints
# - Message Queue: Manages outgoing and incoming messages
# - Transfer Handler: Coordinates file transfers between agents
# - Security Enforcer: Validates authentication and authorization
# - Statistics Collector: Monitors network performance metrics
```

**Demonstration Workflow**:

**Step 1: Direct Messaging**
- NodeAlfa sends a text message to NodeBravo
- Communication Manager validates NodeAlfa's authorization to send to NodeBravo
- Message is routed through the network to NodeBravo's endpoint
- NodeBravo receives and processes the message
- Delivery confirmation is returned to NodeAlfa

**Step 2: Registry Discovery**
- Query the Communication Manager's agent registry
- Retrieve information about registered agents (NodeBravo in this case)
- Display agent details including ID, name, network endpoint, and capabilities
- Demonstrates dynamic discovery in P2P networks

**Step 3: File Transfer (A2A Protocol)**
- NodeAlfa initiates a file transfer to NodeBravo using the A2A send_file tool
- Communication Manager validates authorization for file transfer
- File is packaged with metadata and transferred securely
- NodeBravo receives the file and stores it locally
- Transfer confirmation includes success status and any relevant messages

**Step 4: Authorization Test**
- Configure NodeBravo to only accept messages from NodeAlfa (whitelist)
- Attempt to send a message from Intruder to NodeBravo
- Communication Manager blocks the message due to authorization failure
- System logs and reports the blocked communication attempt
- Demonstrates effective access control in agent networks

**Step 5: Communication Statistics**
- Display comprehensive statistics from the Communication Manager:
  - Messages sent and received
  - Files transferred successfully
  - Active network connections
  - Authorization blocks and errors
  - Network performance metrics

**Technical Details of A2A File Transfer**:
1. **Initiation**: Sender agent requests file transfer through appropriate tool
2. **Validation**: Communication Manager checks sender authorization and file accessibility
3. **Preparation**: File is read, metadata is attached, and package is prepared
4. **Transmission**: Data is sent in chunks with error checking and reassembly instructions
5. **Reception**: Receiver agent accepts incoming file transfer request
6. **Validation**: Communication Manager verifies receiver authorization to accept files
7. **Reassembly**: Chunks are reassembled, integrity is verified, and file is saved
8. **Confirmation**: Both sender and receiver receive transfer completion notifications

**Security Features Detailed**:

**Authentication Mechanisms**:
- **Token-Based Auth**: Each agent can require a specific authentication token for incoming communications
- **Configurable Tokens**: Auth tokens are set per agent and can be rotated for security
- **Challenge-Response**: Optional challenge-response mechanisms for enhanced security
- **Token Validation**: Communication Manager validates tokens before processing any communication

**Authorization Controls**:
- **Whitelist-Based**: By default, agents accept messages from any sender unless restricted
- **Specific Allow Lists**: Define exact agent IDs that are permitted to send messages
- **Empty Whitelist**: Special case meaning "accept from all" (default behavior)
- **Individual Blocking**: Ability to block specific agents while allowing others
- **Hierarchical Control**: Different authorization levels for messages vs. file transfers

**Message Integrity**:
- **Timestamp Validation**: Prevent replay attacks by validating message timestamps
- **Sequence Numbers**: Detect missing or duplicate messages in ordered communications
- **Content Hashing**: Optional content verification for critical communications
- **Delivery Confirmation**: Acknowledgement system for guaranteed message delivery

**Customization Options**:
- **Network Configuration**:
  - Modify network URLs to deploy agents on different hosts or ports
  - Use public URLs (ngrok, DevTunnels, etc.) for internet-wide agent communication
  - Configure different ports for multiple agents on the same host
  
- **Security Settings**:
  - Adjust auth token strength and rotation frequency
  - Implement IP-based restrictions in addition to agent ID whitelisting
  - Add encryption layers for sensitive communications
  - Configure different authorization levels for different message types
  
- **Performance Tuning**:
  - Adjust message queue sizes and processing intervals
  - Configure connection timeouts and retry policies
  - Optimize file transfer chunk sizes for different network conditions
  - Implement message prioritization for urgent communications
  
- **Extended Functionality**:
  - Add support for group messaging and broadcasting
  - Implement message persistence for offline agent communication
  - Add message routing capabilities for multi-hop communications
  - Integrate with external messaging systems (MQTT, WebSocket, etc.)

**Example Use Cases**:
- **Distributed AI Systems**: Networks of specialized agents collaborating on complex tasks
- **Secure Information Sharing**: Confidential exchange of sensitive data between trusted agents
- **Collaborative Problem Solving**: Agents working together to solve distributed optimization problems
- **Resource Discovery**: Agents advertising and discovering services in a decentralized manner
- **Load Distribution**: Distributing computational workloads across multiple agent nodes
- **Fault Tolerance**: Redundant agent networks that continue operating despite individual failures
- **Edge Computing**: Deploying agents on edge devices for localized processing and decision-making
- **IoT Networks**: Coordinating smart devices through agent-based communication protocols
- **Gaming & Simulation**: Multi-agent systems for interactive simulations and game AI
- **Financial Networks**: Secure transaction processing and fraud detection agent networks

**Production Considerations**:
- **Deployment Architecture**: Consider running each agent on separate hosts or containers for isolation
- **Network Security**: Implement TLS/SSL encryption for all agent communications in production
- **Authentication Strength**: Use strong, randomly generated tokens and consider multi-factor authentication
- **Monitoring & Alerting**: Set up comprehensive monitoring for network health, performance, and security events
- **Scaling Strategies**: Implement horizontal scaling by adding more agent instances as needed
- **Data Persistence**: Consider persistent storage for agent configurations, message histories, and transferred files
- **Compliance & Auditing**: Ensure communication logs meet regulatory requirements for your industry
- **Disaster Recovery**: Implement backup and recovery procedures for agent configurations and network state

**Learning Outcomes**:
- Understanding of P2P networking principles in agent-based systems
- Implementation of secure agent-to-agent communication channels
- Design patterns for decentralized agent discovery and registration
- Techniques for implementing authorization and access control in AI networks
- Best practices for reliable file transfer between distributed agents
- Methods for monitoring and troubleshooting agent network communications
- Strategies for building scalable, resilient distributed AI systems
- Knowledge of communication protocols suitable for agent-based architectures

[📄 Detailed Documentation](docs/p2p_networking.md)

---

### API Call Tool

A simple demonstration of the DAIE library's `APICallTool` for making HTTP API requests. This example shows how to execute API calls programmatically using the built-in tool system, enabling agents to interact with external services and data sources.

**Features**:
- **HTTP API Calls**: Execute GET, POST, PUT, DELETE requests with full HTTP standard support
- **JSON Response Handling**: Automatic parsing of JSON responses with error handling for malformed data
- **Custom Headers**: Support for custom HTTP headers including authentication, content-type, and specialized API requirements
- **Async Execution**: Non-blocking API calls using asyncio for concurrent operations and responsive applications
- **Request Body Support**: Send data with POST/PUT requests in various formats (JSON, form data, raw)
- **URL Parameters**: Support for query string parameters in GET requests
- **Response Metadata**: Access to status codes, headers, and response timing information
- **Error Handling**: Comprehensive error handling for network issues, HTTP errors, and timeout scenarios

**Technical Implementation**:
The API Call Tool demonstrates how to extend agent capabilities with external service integration:
1. **Tool Initialization**: Create an APICallTool instance that agents can use
2. **Request Configuration**: Specify URL, method, headers, data, and parameters for API calls
3. **Async Execution**: Leverage Python's asyncio for non-blocking I/O operations
4. **Response Processing**: Handle successful responses and extract relevant data
5. **Error Management**: Gracefully handle network errors, HTTP error codes, and malformed responses
6. **Integration Patterns**: Show how agents can decide when and how to use external API calls

**Run**:
```bash
python APICallTool.py
```

**Example Output**:
The tool demonstrates calling the GitHub API to fetch user information, returning a detailed JSON response including:
- User profile information (login, ID, name, company, location)
- Repository statistics (public repos, gists, followers, following)
- Timestamps (account creation, last update)
- URLs to various user resources (repos, followers, gists, etc.)

**API Configuration Options**:
The `execute()` method accepts the following parameters:
- `url` (required): The API endpoint URL
- `method` (optional): HTTP method (GET, POST, PUT, DELETE). Default: GET
- `headers` (optional): Dictionary of HTTP headers (e.g., Authorization, Content-Type)
- `data` (optional): Request body for POST/PUT requests (JSON, form data, or raw)
- `params` (optional): URL query parameters for GET requests

**Detailed Code Structure**:
```python
# Main components:
# 1. Import: APICallTool from daie.tools
# 2. Tool Initialization: Create APICallTool instance
# 3. API Execution: Execute HTTP request with URL, method, and headers
# 4. Result Handling: Process and display JSON response
# 5. Error Handling: Manage network errors, HTTP errors, and timeouts

# Example usage patterns:
# Simple GET request
result = await api_tool.execute({
    "url": "https://api.example.com/data",
    "method": "GET"
})

# POST request with JSON data
result = await api_tool.execute({
    "url": "https://api.example.com/users",
    "method": "POST",
    "headers": {"Content-Type": "application/json"},
    "data": {"name": "John Doe", "email": "john@example.com"}
})

# GET request with query parameters
result = await api_tool.execute({
    "url": "https://api.example.com/search",
    "method": "GET",
    "params": {"q": "DAIE", "limit": 10}
})

# Request with custom headers (authentication)
result = await api_tool.execute({
    "url": "https://api.example.com/protected",
    "method": "GET",
    "headers": {
        "Authorization": "Bearer your_token_here",
        "Accept": "application/json"
    }
})
```

**Use Cases**:
- **Data Integration**: Fetch real-time data from external APIs to enhance agent knowledge
- **Service Orchestration**: Coordinate actions across multiple external services
- **External Action Execution**: Perform actions in external systems (create issues, send emails, etc.)
- **Data Enrichment**: Supplement agent responses with current information from external sources
- **Workflow Automation**: Automate multi-step processes involving external systems
- **Monitoring & Alerting**: Check system health, performance metrics, or service status
- **Content Aggregation**: Gather information from multiple sources for comprehensive responses
- **Validation & Verification**: Validate data or check compliance against external sources

**Advanced Integration Patterns**:
1. **Conditional API Usage**: Agents decide when to call external APIs based on query context
2. **API Response Caching**: Cache frequent API responses to reduce latency and external load
3. **Rate Limiting Implementation**: Respect API rate limits to prevent service disruption
4. **Fallback Mechanisms**: Provide alternative responses when external APIs are unavailable
5. **API Aggregation**: Combine data from multiple APIs for comprehensive answers
6. **Transformation Layers**: Convert external API responses to match agent expected formats

**Error Handling & Resilience**:
The tool handles common HTTP errors and returns structured responses:
- **Network Errors**: Connection timeouts, DNS failures, unreachable hosts
- **HTTP Error Codes**: 4xx (client errors) and 5xx (server errors) with detailed information
- **Timeouts**: Configurable request timeouts to prevent hanging operations
- **Malformed Responses**: Graceful handling of non-JSON responses when JSON is expected
- **Authentication Failures**: Proper handling of 401 and 403 responses
- **Rate Limiting**: Detection and handling of 429 (Too Many Requests) responses

**Customization Options**:
- **Timeout Configuration**: Adjust request timeouts for different API characteristics
- **Retry Logic**: Implement exponential backoff for failed requests
- **Header Management**: Default headers for all requests (User-Agent, Accept, etc.)
- **Response Processing**: Custom parsers for different response formats (XML, CSV, etc.)
- **Logging Integration**: Detailed logging of API calls for debugging and monitoring
- **Security Enhancements**: SSL certificate validation, proxy support, and secure credential storage

**Example Advanced Usage**:
```python
# Agent that decides when to use API calls
class KnowledgeAgent:
    def __init__(self):
        self.api_tool = APICallTool()
        self.knowledge_base = {}  # Local cache
    
    async def get_weather(self, city):
        # Check cache first
        if city in self.knowledge_base:
            return self.knowledge_base[city]
        
        # Call external API if not cached
        result = await self.api_tool.execute({
            "url": f"http://api.weatherapi.com/v1/current.json",
            "params": {
                "key": "your_api_key",
                "q": city,
                "aqi": "no"
            }
        })
        
        if result.get("success"):
            weather_data = result["data"]["current"]
            # Cache for future use
            self.knowledge_base[city] = weather_data
            return weather_data
        else:
            # Handle error gracefully
            return {"error": "Unable to fetch weather data"}

# Agent that performs actions in external systems
class ActionAgent:
    def __init__(self):
        self.api_tool = APICallTool()
    
    async def create_github_issue(self, repo, title, body):
        result = await self.api_tool.execute({
            "url": f"https://api.github.com/repos/{repo}/issues",
            "method": "POST",
            "headers": {
                "Authorization": f"token {self.github_token}",
                "Content-Type": "application/json"
            },
            "data": {
                "title": title,
                "body": body
            }
        })
        
        if result.get("success"):
            return result["data"]["html_url"]
        else:
            raise Exception(f"Failed to create issue: {result.get('error')}")
```

**Best Practices for API Integration**:
1. **Security First**: Never hardcode API keys; use environment variables or secure vaults
2. **Rate Limiting Respect**: Implement client-side rate limiting to avoid being blocked
3. **Error Gracefulness**: Provide meaningful fallback responses when APIs fail
4. **Response Validation**: Validate API responses match expected schemas
5. **Logging & Monitoring**: Log API calls for usage tracking and troubleshooting
6. **Caching Strategy**: Cache appropriate responses to improve performance and reduce external load
7. **Timeout Management**: Set appropriate timeouts to prevent resource exhaustion
8. **Header Standardization**: Use consistent headers for identification and versioning

**Learning Outcomes**:
- Understanding of how to extend agent capabilities with external service integration
- Patterns for deciding when and how agents should use external APIs
- Techniques for handling asynchronous I/O in agent systems
- Best practices for secure and reliable external service communication
- Methods for integrating API data into agent knowledge and decision-making
- Strategies for handling failures and providing graceful degradation
- Knowledge of common API integration patterns and anti-patterns

[📄 Detailed Documentation](docs/APICallTool.md)

---

## Project Structure

```
daie_samples/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore rules
│
├── basic_chat.py                      # Basic chat with RAG
├── rag_chat.py                        # RAG-powered chat
├── simple_ollama_chat_loop.py         # Production-ready chat
├── ai_gf_config_chat_loop.py          # Personalized AI agent
├── Orchestrator_courtroom.py          # Courtroom simulation
├── Orchestrator_RAG.py                # Research lab with RAG
├── p2p_networking.py                  # P2P networking demo
├── APICallTool.py                     # API call tool demo
│
├── docs/                              # Documentation folder
│   ├── basic_chat.md                  # Basic chat documentation
│   ├── rag_chat.md                    # RAG chat documentation
│   ├── simple_ollama_chat_loop.md     # Simple Ollama chat documentation
│   ├── ai_gf_config_chat_loop.md      # AI Girlfriend chat documentation
│   ├── Orchestrator_courtroom.md      # Courtroom simulation documentation
│   ├── Orchestrator_RAG.md            # Orchestrator RAG documentation
│   ├── p2p_networking.md              # P2P networking documentation
│   └── APICallTool.md                 # API call tool documentation
│
└── data/                              # Document storage (for RAG examples)
    └── (your documents here)
```

## Configuration

### LLM Configuration

All examples use the `set_llm()` function to configure the language model. This function sets up the connection to your preferred LLM provider and configures generation parameters.

```python
from daie.core.llm_manager import set_llm, LLMType

set_llm(
    ollama_llm="llama3.2:1b",      # Ollama model name
    temperature=0.3,                 # Response creativity (0.0-1.0)
    max_tokens=1024,                 # Maximum response length
    llm_type=LLMType.OLLAMA,        # LLM provider type
    stream=True                      # Enable streaming responses
)
```

#### LLM Configuration Parameters

- **ollama_llm**: Specifies the Ollama model to use (e.g., "llama3.2:1b", "llama3.2:3b", "mistral:7b")
- **temperature**: Controls randomness in generation (0.0 = deterministic, 1.0 = maximum creativity)
- **max_tokens**: Maximum number of tokens to generate in a response
- **llm_type**: Specifies the LLM provider (currently supports OLLAMA)
- **stream**: Enables/disables streaming responses for real-time output

#### Supported LLM Providers

The DAIE library currently supports:
- **OLLAMA**: Local LLM execution via Ollama (recommended for privacy and offline use)
- **Future Extensions**: Designed for easy extension to other providers (OpenAI, Anthropic, etc.)

#### Model Selection Guidelines

- **llama3.2:1b**: Fast, efficient model suitable for testing and development
- **llama3.2:3b**: Better quality with reasonable resource requirements
- **mistral:7b**: High-quality model for production use cases
- **wizard-vicuna-uncensored:7b**: Specialized model for roleplay and creative applications

#### Performance Considerations

- **GPU Acceleration**: Ensure Ollama is configured to use GPU if available for faster inference
- **Model Quantization**: Use quantized versions of models for reduced memory usage
- **Context Length**: Be aware of model context limits when setting max_tokens
- **Batch Processing**: For multiple concurrent requests, consider model loading strategies

### Agent Configuration

Agents are configured using the `AgentConfig` class, which defines the agent's identity, capabilities, and behavior.

```python
from daie.core.agent import AgentConfig, AgentRole

config = AgentConfig(
    name="AgentName",
    role=AgentRole.GENERAL_PURPOSE,
    goal="Agent's primary goal",
    system_prompt="Agent's core behavior instructions",
    personality="Agent's personality traits",
    behavior="Specific behavioral patterns",
    temperature=0.3,
    max_tokens=1024,
    rag_document_path="./data",      # Path to documents (for RAG)
    enable_rag=True,                 # Enable/disable RAG
)
```

#### Agent Configuration Parameters

- **name**: Unique identifier for the agent
- **role**: Defines the agent's function in the system (see AgentRole enum)
- **goal**: Primary objective that guides the agent's behavior
- **system_prompt**: Core instructions that define the agent's behavior and expertise
- **personality**: Descriptive traits that influence response style and tone
- **behavior**: Specific patterns or guidelines for how the agent should act
- **temperature**: Controls response creativity (0.0-1.0)
- **max_tokens**: Maximum response length in tokens
- **rag_document_path**: Path to documents for RAG functionality
- **enable_rag**: Boolean to activate/deactivate document retrieval
- **capabilities**: List of agent capabilities (text, communication, etc.)
- **gender**: Optional gender specification for persona consistency

#### AgentRole Enum Values

- **GENERAL_PURPOSE**: Versatile agent for various tasks
- **ORCHESTRATOR**: Main coordinator in multi-agent systems
- **RESEARCH_ASSISTANT**: Specialized agent for document analysis and retrieval
- **PROSECUTOR**: Legal agent arguing for prosecution
- **DEFENSE_ATTORNEY**: Legal agent defending the accused
- **JUDGE**: Legal agent making impartial decisions
- **PROFESSOR**: Educational agent for knowledge dissemination
- **CUSTOM**: User-defined role for specialized applications

#### System Prompt Best Practices

- **Clarity**: Use clear, unambiguous language to define agent behavior
- **Specificity**: Provide detailed instructions for complex behaviors
- **Constraints**: Clearly state what the agent should and shouldn't do
- **Examples**: Include examples of desired behavior when helpful
- **Domain Expertise**: Specify knowledge areas and expertise levels
- **Tone Guidance**: Define formality level, humor usage, and emotional expression

#### Personality Configuration

The personality field accepts descriptive traits that influence the agent's responses:
- **Emotional Tone**: happy, serious, empathetic, enthusiastic
- **Communication Style**: formal, casual, technical, conversational
- **Behavioral Traits**: helpful, playful, sarcastic, supportive
- **Professional Attributes**: authoritative, collaborative, analytical, creative

#### Behavior Guidelines

The behavior field provides specific actionable guidelines:
- **Response Format**: "Always respond in bullet points", "Keep responses under 3 sentences"
- **Citation Requirements**: "Always cite sources when using external information"
- **Interaction Patterns**: "Ask follow-up questions to clarify user intent"
- **Error Handling**: "When uncertain, explicitly state limitations"
- **Creative Constraints**: "Use metaphors and analogies when explaining concepts"

### Advanced Agent Configuration

For specialized use cases, additional configuration options are available:

```python
config = AgentConfig(
    name="SpecializedAgent",
    role=AgentRole.CUSTOM,
    goal="Perform specialized data analysis tasks",
    system_prompt="You are a data analysis expert...",
    personality="analytical, precise, detail-oriented",
    behavior="Show work step-by-step, validate assumptions, provide confidence intervals",
    temperature=0.2,
    max_tokens=2048,
    capabilities=["text", "communication", "data_analysis"],
    rag_document_path="./data/financial_reports",
    enable_rag=True,
    # Advanced options
    metadata={"department": "finance", "security_level": "confidential"},
    tags=["analysis", "reporting", "quarterly"],
)
```

#### Advanced Configuration Options

- **metadata**: Custom key-value pairs for agent categorization and filtering
- **tags**: List of tags for grouping and searching agents
- **capabilities**: Extended list beyond basic text/communication (data_analysis, image_processing, etc.)
- **Custom Fields**: Domain-specific configuration based on agent specialization

### Orchestrator Configuration

For multi-agent systems, use the `Orchestrator` class to coordinate between a main agent and specialized sub-agents.

```python
from daie.core.orchestrator import Orchestrator

orchestrator = Orchestrator(
    main_agent=main_agent,
    sub_agents=[sub_agent1, sub_agent2],
    context_name="ContextName",
    main_role="MainRole",
    sub_role="SubRole"
)
```

#### Orchestrator Configuration Parameters

- **main_agent**: The primary agent that coordinates the workflow
- **sub_agents**: List of specialized agents that perform specific tasks
- **context_name**: Identifier for the shared context or conversation
- **main_role**: Role description of the main agent (e.g., "Coordinator", "Supervisor")
- **sub_role**: Role description of the sub-agents (e.g., "Specialist", "Assistant")

#### Orchestrator Patterns

1. **Hierarchical Coordination**: Main agent delegates tasks to sub-agents and synthesizes results
2. **Parallel Processing**: Sub-agents work simultaneously on different aspects of a problem
3. **Iterative Refinement**: Main agent and sub-agents refine solutions through multiple rounds
4. **Debate Format**: Sub-agents argue different perspectives, main agent synthesizes consensus
5. **Pipeline Processing**: Output of one sub-agent becomes input for another

#### Multi-Agent Communication Patterns

- **Request-Response**: Main agent requests information, sub-agents respond
- **Publish-Subscribe**: Agents broadcast information to interested parties
- **Blackboard**: Shared knowledge base that agents read from and write to
- **Contract Net**: Agents bid for tasks, main agent awards contracts

#### Context Management in Orchestrators

The orchestrator manages shared context between agents:
- **Shared Information**: Facts, data, and intermediate results accessible to all agents
- **Private Information**: Role-specific data that maintains agent specialization
- **Communication History**: Record of interactions for context preservation
- **State Tracking**: Progress tracking through multi-step workflows

#### Orchestrator Best Practices

- **Clear Role Definition**: Ensure each agent has a distinct, well-defined purpose
- **Effective Communication**: Establish clear protocols for information exchange
- **Conflict Resolution**: Implement mechanisms for resolving disagreements between agents
- **Scalability Design**: Structure the system to accommodate additional agents
- **Fault Tolerance**: Plan for agent failures and implement recovery procedures
- **Performance Optimization**: Minimize unnecessary communication and computation

### Tool Configuration

Agents can be extended with custom tools for specialized functionality:

```python
from daie.tools import APICallTool, FileReadTool

# Create tool instances
api_tool = APICallTool()
file_tool = FileReadTool()

# Configure agent with tools
config = AgentConfig(
    name="ToolAgent",
    role=AgentRole.GENERAL_PURPOSE,
    goal="Access external services and file systems",
    system_prompt="You are an agent capable of calling APIs and reading files...",
    personality="helpful, resourceful, informative",
    behavior="Use available tools to answer questions when internal knowledge is insufficient",
    temperature=0.3,
    max_tokens=1024,
    tools=[api_tool, file_tool],  # Make tools available to the agent
)
```

#### Common Tool Types

- **APICallTool**: For making HTTP requests to external services
- **FileReadTool**: For reading local files and documents
- **FileWriteTool**: For writing content to local files
- **WebSearchTool**: For searching the internet (when available)
- **CalculatorTool**: For performing mathematical computations
- **CodeExecutionTool**: For running code in various languages

#### Tool Integration Patterns

1. **Reactive Tool Use**: Agents decide to use tools based on user queries
2. **Proactive Tool Preparation**: Agents pre-load relevant information using tools
3. **Tool Chaining**: Using output from one tool as input to another
4. **Fallback Mechanisms**: Using tools when internal knowledge is insufficient
5. **Enhancement Mode**: Using tools to supplement and verify internal knowledge

### Environment-Based Configuration

For deployment flexibility, configuration can be managed through environment variables:

```python
import os
from daie.core.llm_manager import set_llm, LLMType
from daie.core.agent import AgentConfig

# Load configuration from environment
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.3"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1024"))
ENABLE_RAG = os.getenv("ENABLE_RAG", "true").lower() == "true"

# Configure LLM
set_llm(
    ollama_llm=OLLAMA_MODEL,
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS,
    llm_type=LLMType.OLLAMA,
    stream=True
)

# Configure agent with environment settings
config = AgentConfig(
    name=os.getenv("AGENT_NAME", "Assistant"),
    role=AgentRole.GENERAL_PURPOSE,
    goal=os.getenv("AGENT_GOAL", "Be helpful and informative"),
    system_prompt=os.getenv(
        "SYSTEM_PROMPT", 
        "You are a helpful AI assistant."
    ),
    personality=os.getenv("AGENT_PERSONALITY", "helpful, friendly"),
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS,
    rag_document_path=os.getenv("RAG_PATH", "./data"),
    enable_rag=ENABLE_RAG,
)
```

#### Common Environment Variables

- **OLLAMA_MODEL**: Default Ollama model to use
- **TEMPERATURE**: Response creativity level (0.0-1.0)
- **MAX_TOKENS**: Maximum response length
- **ENABLE_RAG**: Whether to activate RAG functionality ("true"/"false")
- **RAG_PATH**: Path to documents for knowledge base
- **AGENT_NAME**: Identifier for the agent
- **AGENT_GOAL**: Primary objective of the agent
- **SYSTEM_PROMPT**: Core behavioral instructions
- **AGENT_PERSONALITY**: Descriptive traits for response style

#### Configuration File Support

For complex deployments, configuration can be loaded from files:
- **YAML Configuration**: Hierarchical configuration with environment overrides
- **JSON Configuration**: Structured configuration for programmatic loading
- **TOML Configuration**: Human-readable configuration format
- **Environment-Specific Files**: Different configs for development, testing, production

### Configuration Validation and Testing

Ensure your configuration is correct with validation patterns:

```python
def validate_config(config):
    """Validate agent configuration before use"""
    errors = []
    
    if not config.name or len(config.name.strip()) == 0:
        errors.append("Agent name is required")
    
    if config.temperature < 0.0 or config.temperature > 1.0:
        errors.append("Temperature must be between 0.0 and 1.0")
    
    if config.max_tokens <= 0:
        errors.append("Max tokens must be positive")
    
    if not config.system_prompt or len(config.system_prompt.strip()) == 0:
        errors.append("System prompt is required")
    
    return errors

# Usage
errors = validate_config(my_config)
if errors:
    print("Configuration errors:")
    for error in errors:
        print(f"  - {error}")
else:
    print("Configuration is valid")
```

#### Configuration Testing Strategies

- **Unit Testing**: Test configuration parsing and validation logic
- **Integration Testing**: Verify agents behave as expected with given configurations
- **Scenario Testing**: Test configurations in realistic use cases
- **Performance Testing**: Measure resource usage with different configurations
- **Security Testing**: Validate that configurations don't introduce vulnerabilities

### Dynamic Configuration Updates

Advanced patterns for updating configuration at runtime:

```python
# Runtime temperature adjustment based on task type
def adjust_temperature_for_task(agent, task_type):
    """Adjust agent temperature based on the type of task"""
    temperature_map = {
        "factual": 0.2,      # Low creativity for factual accuracy
        "creative": 0.8,     # High creativity for ideation
        "balanced": 0.5,     # Moderate creativity
        "conservative": 0.1  # Very low creativity for safety
    }
    
    if task_type in temperature_map:
        agent.config.temperature = temperature_map[task_type]
        # Note: Some systems may require agent restart for changes to take effect

# Context-aware configuration switching
class ContextAwareAgent:
    def __init__(self, base_config):
        self.base_config = base_config
        self.context_configs = {}
        self.current_context = "default"
    
    def set_context(self, context_name):
        """Switch to a different context-specific configuration"""
        if context_name in self.context_configs:
            self.current_context = context_name
            # Apply context-specific overrides
            # Implementation depends on specific agent system
    
    def add_context_config(self, context_name, config_overrides):
        """Add or update configuration for a specific context"""
        self.context_configs[context_name] = config_overrides
```

#### When to Update Configuration Dynamically

- **Task Switching**: Adjust parameters when changing between different types of tasks
- **User Preferences**: Modify behavior based on explicit user requests
- **Performance Optimization**: Tune parameters based on observed system performance
- **A/B Testing**: Experiment with different configurations to optimize outcomes
- **Adaptive Learning**: Adjust based on feedback and performance metrics

[📄 Detailed Configuration Documentation](docs/configuration_guide.md)  <!-- Note: This would be a new file to create -->

## Use Cases

### Customer Support
- Build AI agents that can answer questions based on your documentation
- Implement RAG for accurate, document-grounded responses
- Create multi-agent systems for complex support scenarios

### Research Assistance
- Create research assistants that can analyze documents
- Build multi-agent research teams for collaborative analysis
- Implement document retrieval for knowledge-based Q&A

### Education
- Build interactive tutoring systems
- Create debate simulations for critical thinking
- Implement knowledge base querying for learning

### Legal & Compliance
- Simulate legal scenarios with multiple perspectives
- Build document analysis systems
- Create compliance checking agents

### Distributed Systems
- Build P2P agent networks for distributed computing
- Implement secure agent-to-agent communication
- Create file transfer systems between agents

### Development & Testing
- Test API endpoints with the API Call Tool
- Build automation scripts for development workflows
- Create debugging and monitoring tools

## Best Practices

### Agent Design
1. **Clear System Prompts**: Define agent behavior clearly in the system prompt
2. **Appropriate Temperature**: Use lower temperature (0.1-0.3) for factual tasks, higher (0.7-0.9) for creative tasks
3. **Token Management**: Set appropriate `max_tokens` to control response length and costs
4. **Personality Consistency**: Keep personality traits consistent with the agent's role

### RAG Implementation
1. **Document Quality**: Ensure documents are well-structured and relevant
2. **Chunk Size**: Optimize chunk size for your use case
3. **Source Citation**: Enable source citation for transparency
4. **Regular Updates**: Keep knowledge base documents up to date

### Multi-Agent Systems
1. **Clear Roles**: Define distinct roles for each agent
2. **Effective Coordination**: Use the Orchestrator pattern for complex tasks
3. **Error Handling**: Implement proper error handling for agent communication
4. **Resource Management**: Monitor agent resource usage

### Security
1. **Authentication**: Use secure authentication tokens for agent communication
2. **Authorization**: Implement whitelist-based sender restrictions
3. **Input Validation**: Validate all user inputs and agent messages
4. **Logging**: Maintain comprehensive logs for auditing

### Production Deployment
1. **Logging**: Use appropriate log levels and handlers
2. **Monitoring**: Track agent performance and usage metrics
3. **Error Tracking**: Implement proper error tracking and alerting
4. **Scalability**: Design for horizontal scaling of agent instances

## Troubleshooting

### Common Issues

#### Agent Not Responding
- **Check Ollama**: Ensure Ollama is running and the model is available
- **Verify Model**: Confirm the model name matches your configuration
- **Network**: Check network connectivity to Ollama endpoint

#### Slow Responses
- **Model Size**: Consider using a smaller model (e.g., `llama3.2:1b` instead of larger models)
- **Temperature**: Lower temperature can sometimes improve response speed
- **Max Tokens**: Reduce `max_tokens` for faster responses

#### RAG Not Working
- **Document Path**: Verify the document path is correct
- **File Format**: Ensure documents are in supported formats (TXT, PDF)
- **Dependencies**: Install RAG dependencies: `pip install PyPDF2 sentence-transformers faiss-cpu`

#### Connection Errors
- **Network**: Verify network connectivity
- **Ports**: Check that required ports are not blocked
- **Firewall**: Ensure firewall allows connections to Ollama and agent endpoints

#### Memory Issues
- **Document Size**: Reduce document size or implement chunking
- **Agent Cleanup**: Ensure agents are properly stopped after use
- **Resource Monitoring**: Monitor system resource usage

### Debug Mode

Enable debug logging for more detailed information:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Dependencies

### Core Dependencies
- `daie==1.0.4` - DAIE library for multi-agent AI systems
- `pydantic==2.12.5` - Data validation and settings management
- `requests==2.32.5` - HTTP library for API calls
- `python-dotenv==1.2.2` - Environment variable management

### RAG Dependencies
- `PyPDF2` - PDF document processing
- `sentence-transformers` - Text embedding generation
- `faiss-cpu` - Vector similarity search

### Networking Dependencies
- `nats-py==2.14.0` - NATS messaging client
- `uvicorn==0.42.0` - ASGI server for agent endpoints
- `websocket-client==1.9.0` - WebSocket client for real-time communication

### Optional Dependencies
- `opencv-python==4.13.0.92` - Computer vision capabilities
- `selenium==4.41.0` - Web automation
- `rich==14.3.3` - Rich text formatting for terminal output

## License

This project is part of the DAIE (Decentralized AI Ecosystem) library. Please refer to the DAIE library documentation for licensing information.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## Support

For questions, issues, or feature requests, please refer to the DAIE library documentation or open an issue in the repository.

---

**Built with ❤️ using the DAIE Library ❤️ kanishk kumar singh**
