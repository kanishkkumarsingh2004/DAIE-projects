# Hybrid Parliament Orchestrator

## Description
The Hybrid Parliament Orchestrator is the pinnacle of the DAIE architecture, implementing a "Deliberate then Delegate" workflow. This example demonstrates how to combine the strategic deliberation of a `Parliament` assembly with the tactical execution of an `OrchestratorAgent`.

## Architecture: Deliberate then Delegate
1. **Deliberation Phase (Parliament)**: A group of specialized agents (Architect, Researcher, Manager) debate a complex task until they reach a consensus roadmap.
2. **Execution Phase (Orchestrator)**: Once a plan is finalized and meets the confidence threshold, it is passed to an Orchestrator who assigns sub-tasks to execution agents and tools.

## Features
- **Consensus Roadmap**: Generates a peer-reviewed strategic plan Before execution.
- **Confidence Threshold**: Prevents execution if the Parliament's consensus confidence is below a set percentage (e.g., 60%).
- **Specialized Assemblies**: Highly modular setup with distinct roles for architectural design, market research, and project management.
- **Automated Handover**: Seamless transition from abstract planning to concrete tool usage.

## Configuration
### Parliament Assembly
- **Architect**: Focuses on structural integrity and technical design.
- **Researcher**: Prioritizes data gathering and validation.
- **Manager**: Focuses on timelines, feasibility, and product-market fit.

### Orchestrator
- **Type**: `OrchestratorAgent`
- **Role**: Plan execution and sub-agent delegation.

### Pipeline Config
- **Min Confidence**: 60.0%
- **Max Review Rounds**: 2 (within Parliament)

## Usage
```bash
python hybrid_parliament.py
```

## Example Prompts
- "Analyze the financial impact of the Indian Budget 2026 on the tech sector."
- "Design a decentralized P2P network protocol and document the execution steps."
- "Write a full-stack React app that integrates with an external LLM provider."

## Technical Implementation
```python
# 1. Define Parliament Agents
parliament_agents = [Agent(config=architect_config), ...]

# 2. Create Parliament
parliament = Parliament(sub_agents=parliament_agents, speaker=parliament_agents[0])

# 3. Create Orchestrator
orchestrator = OrchestratorAgent()

# 4. Integrate into Hybrid Pipeline
hybrid_pipeline = HybridParliamentOrchestrator(
    parliament=parliament,
    orchestrator=orchestrator,
    min_confidence_threshold=60.0
)

# 5. Launch Chat Loop
config = HybridParliamentChatConfig(hybrid_pipeline=hybrid_pipeline)
config.run()
```

## Benefits of Hybrid Architecture
- **Accuracy**: Multi-agent cross-referencing reduces hallucinations during the planning phase.
- **Feasibility**: The "Manager" agent ensures that the proposed roadmap is realistic before the Orchestrator starts calling tools.
- **Quality**: Peer review ensures that edge cases are considered early.

## Use Cases
- **Strategic Business Planning**: Multi-departmental analysis before taking action.
- **Complex Software Engineering**: Designing system architecture before generating code.
- **Policy Research**: Deep evaluation of political or economic changes with executable reporting.
