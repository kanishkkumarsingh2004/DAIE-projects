# Parliament Architecture: Mixture-of-Agents

## Description
The Parliament Architecture is a sophisticated "Mixture-of-Agents" setup designed for high-stakes decision making, philosophical debate, and complex multi-perspective analysis. Instead of relying on a single agent, this architecture uses a assembly of specialized agents that peer-review each other's work and synthesize a final consensus result.

## Core Concepts
- **Consensus Building**: Multiple agents evaluate a topic from different ideological or professional backgrounds.
- **Peer Review**: Agents can critque and refine the answers provided by their peers.
- **Synthesis (Speaker)**: A designated "Speaker" (synthesizer) takes the best parts of the deliberation to form the final response.

## Assembly Roles
This demo uses four distinct perspectives:
- **Economist**: Analyzes financial implications, resource constraints, and market dynamics.
- **Lawyer**: Evaluates security, legal frameworks, and regulatory compliance.
- **Scientist**: Focuses on empirical data, technical feasibility, and research-backed evidence.
- **Ethicist**: Considers moral implications, social impact, and humanist values.

## Features
- **Low Temperature for Accuracy**: Most agents are configured with `temperature=0.3` to reduce hallucinations during factual analysis.
- **Specialized System Prompts**: Each agent has a custom prompt defining their professional perspective.
- **Interactive Synthesis**: Users can observe the deliberation process (if logging is enabled) and receive the final synthesized consensus.

## Prerequisites
- Python 3.7+
- DAIE library installed
- Ollama running with `llama3.2:1b` model

## Usage
```bash
python parliament_architecture.py
```

## Example Debate Topics
- "Should a highly developed but resource-constrained nation adopt Universal Basic Income?"
- "Is the deployment of autonomous weapons ethical if they mathematically reduce civilian casualties?"
- "Should artificial intelligence research be paused immediately?"

## Code Structure
```python
# 1. Initialize specialized configurations
economist_config = AgentConfig(name="Economist", role=AgentRole.DATA_ANALYST, ...)
lawyer_config = AgentConfig(name="Lawyer", role=AgentRole.SECURITY_AUDITOR, ...)
# ...

# 2. Create Agent Assembly
agents = [Agent(config=economist_config), ...]

# 3. Create Parliament
parliament = Parliament(sub_agents=agents, speaker=agents[0])

# 4. Launch Parliamentary Chat Loop
config = ParliamentChatConfig(parliament=parliament)
config.run()
```

## When to Use This Architecture
- **Policy Analysis**: Evaluating laws or corporate policies.
- **Ethical Decision Making**: Solving trolley problems or AI safety concerns.
- **Complex System Design**: When technical, financial, and legal requirements must all be met simultaneously.
- **Research Synthesis**: Comparing multiple conflicting data sources.

## Best Practices
- **Diverse Perspectives**: Ensure the assembly roles are distinct and potentially conflicting to get a balanced view.
- **Explicit Synthesizer**: Clearly define which agent should act as the speaker to ensure a coherent final answer.
- **Review Rounds**: Adjust `max_review_rounds` in the Parliament configuration to balance depth vs. speed.
