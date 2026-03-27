# Orchestrator Courtroom

## Description
An interactive courtroom simulation using the DAIE library's Orchestrator pattern. This example demonstrates how to create a multi-agent system where a judge coordinates with prosecutor and defense attorney agents to reach verdicts.

## Features
- **Multi-Agent Coordination**: Judge orchestrates prosecutor and defense attorney
- **Role-Based Agents**: Each agent has a specific role and perspective
- **Streaming Support**: Optional real-time streaming of reasoning and answers
- **Interactive Interface**: User acts as court clerk presenting cases
- **JSON Response Parsing**: Automatic extraction of verdicts from structured responses

## Prerequisites
- Python 3.7+
- DAIE library installed
- Ollama running with `llama3.2:1b` model

## Agent Roles
### Judge (Main Agent)
- **Name**: Judge_Justice
- **Role**: Fair and wise judge
- **Goal**: Reach verdicts based on arguments from lawyers

### Prosecutor (Sub-Agent)
- **Name**: Prosecutor_Agent
- **Role**: Determined prosecutor
- **Goal**: Prove defendant guilty beyond reasonable doubt

### Defense Attorney (Sub-Agent)
- **Name**: Defense_Attorney
- **Role**: Sharp defense attorney
- **Goal**: Protect defendant's rights and prove innocence

## Usage
```bash
python Orchestrator_courtroom.py
```

### Initial Setup
1. The script will ask if you want to enable streaming
2. Type `Y` for streaming or `n` for non-streaming mode
3. The courtroom session begins

### Commands
- Present your case as the court clerk
- Type `exit` or `quit` to end the session
- Press `Ctrl+C` to interrupt

## Code Structure
```python
# Main components:
1. LLM Configuration: set_llm() with streaming preference
2. Agent Creation: Judge, Prosecutor, and Defense Attorney agents
3. Orchestrator Setup: Court orchestrator with main and sub-agents
4. Court Session Loop: Interactive case presentation and verdict
5. Cleanup: Graceful shutdown
```

## Orchestrator Configuration
```python
court = Orchestrator(
    main_agent=judge,
    sub_agents=[prosecutor, defense],
    context_name="Courtroom",
    main_role="Judge",
    sub_role="Lawyer"
)
```

## Example Session
```
==================================================
   AI COURTROOM INTERACTIVE DEMO (Ollama)
==================================================

Enable real-time streaming (reasoning & answers)? [Y/n]: Y

[*] Streaming is ENABLED
Type 'exit' or 'quit' to end the session.

[*] Initializing courtroom environment...
[+] Court is in session! Judge: Judge_Justice, Lawyers: Prosecutor_Agent, Defense_Attorney

You (Court Clerk): The defendant is accused of stealing a loaf of bread.

Judge_Justice is presiding over the case...

Final Verdict/Guidance from Judge:
After careful consideration of the arguments presented by both the prosecution and defense, I find the defendant not guilty. The prosecution failed to prove beyond reasonable doubt that the defendant had the intent to steal, and the defense successfully argued that the defendant was in a state of extreme hunger and desperation.

------------------------------
```

## How It Works
1. **User Input**: Court clerk presents a case or question
2. **Orchestration**: Judge receives the input and coordinates with lawyers
3. **Agent Collaboration**: Prosecutor and defense attorney provide their arguments
4. **Verdict**: Judge synthesizes arguments and delivers a verdict
5. **Display**: Final verdict is displayed to the user

## Customization
You can modify the agents' behavior by changing their `system_prompt`:
- Adjust the judge's fairness criteria
- Modify the prosecutor's argumentation style
- Change the defense attorney's approach

## Use Cases
- Legal education and training
- Debate simulation
- Decision-making scenarios
- Multi-agent coordination examples
- AI reasoning demonstration

## Error Handling
The application handles:
- Keyboard interrupts (Ctrl+C)
- Empty input (ignored)
- JSON parsing errors (displays raw response)
- Agent communication errors
