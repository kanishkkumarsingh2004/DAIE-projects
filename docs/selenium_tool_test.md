# Selenium Tool Test

## Description
A comprehensive demonstration of the `SeleniumChromeTool` for browser automation with the DAIE library. This example showcases both agent-based and direct tool usage for web scraping, element interaction, screenshot capture, JavaScript execution, multi-tab management, and cookie handling.

## Features
- **Agent-Based Automation**: Use AI agent to control browser through natural language
- **Direct Tool Usage**: Programmatic control without agent overhead
- **Web Scraping**: Extract data from websites
- **Element Interaction**: Find, click, and type into web elements
- **Screenshot Capture**: Save page screenshots
- **JavaScript Execution**: Run custom JavaScript in the browser
- **Multi-Tab Management**: Open, switch, and close browser tabs
- **Navigation Control**: Back, forward, and refresh actions
- **Cookie Management**: Get and set browser cookies
- **Form Automation**: Fill and submit web forms

## Prerequisites
- Python 3.7+
- DAIE library installed
- Ollama running with `llama3.2:1b` model (or more capable model recommended)
- Google Chrome installed
- ChromeDriver compatible with your Chrome version
- `webdriver-manager` package (for automatic ChromeDriver management)

## Important Notes
> **Model Recommendation**: While this example uses `llama3.2:1b`, more capable models like `llama3.2:latest`, `mistral`, or `qwen2.5` are recommended for better tool parameter handling.

> **Chrome Driver**: If you encounter "DevToolsActivePort file doesn't exist" errors, try setting `headless=False` or ensure Chrome and ChromeDriver versions match.

## Configuration
The agent is configured with the following settings:
- **Name**: BrowserBot
- **Role**: General Purpose
- **System Prompt**: Web automation expert with detailed tool usage instructions
- **Tools**: SeleniumChromeTool

## Usage
```bash
python selenium_tool_test.py
```

### Running Direct Tool Example
Uncomment the following line in the script to run the direct tool example:
```python
# asyncio.run(direct_tool_example())
```

## Code Structure
```python
# Main components:
1. LLM Configuration: set_llm() with Ollama model
2. Agent Creation: Agent with SeleniumChromeTool
3. Agent-Based Examples: 9 automation tasks
4. Direct Tool Example: Programmatic browser control
5. Cleanup: Graceful agent shutdown
```

## Agent-Based Examples

### 1. Basic Web Scraping
```python
result = await agent.execute_task(
    "Open https://example.com and tell me the page title and current URL"
)
```

### 2. Element Interaction
```python
result = await agent.execute_task(
    "Go to https://example.com and find the main heading element. "
    "Tell me what text it contains."
)
```

### 3. Screenshot Capture
```python
result = await agent.execute_task(
    "Navigate to https://example.com and take a screenshot. "
    "Save it as 'example_screenshot.png'"
)
```

### 4. JavaScript Execution
```python
result = await agent.execute_task(
    "Go to https://example.com and execute JavaScript to get the "
    "page title. Return the result."
)
```

### 5. Multi-Tab Management
```python
result = await agent.execute_task(
    "Open https://example.com in the current tab, then open a new tab "
    "with https://httpbin.org/get. Switch back to the first tab and "
    "tell me the URL."
)
```

### 6. Navigation
```python
result = await agent.execute_task(
    "Go to https://example.com, then navigate to https://httpbin.org/get, "
    "then go back to the previous page. Tell me the current URL."
)
```

### 7. Cookie Management
```python
result = await agent.execute_task(
    "Go to https://example.com, get all cookies, then set a custom "
    "cookie named 'test_cookie' with value 'hello_world'. "
    "Verify the cookie was set."
)
```

### 8. Complex Automation
```python
result = await agent.execute_task(
    "Perform these steps:\n"
    "1. Go to https://httpbin.org/forms/post\n"
    "2. Find the customer name input field and type 'John Doe'\n"
    "3. Find the telephone input field and type '555-1234'\n"
    "4. Find the email input field and type 'john@example.com'\n"
    "5. Take a screenshot of the filled form\n"
    "6. Tell me what you did"
)
```

### 9. Data Extraction
```python
result = await agent.execute_task(
    "Go to https://httpbin.org/html and extract all the text content "
    "from the page. Return the main content."
)
```

## Direct Tool Usage

### Opening a URL
```python
tool = SeleniumChromeTool()
result = await tool._execute({
    "action": "open_url",
    "url": "https://example.com",
    "headless": True,
})
```

### Finding Elements
```python
result = await tool._execute({
    "action": "find_element",
    "element_selector": "h1",
    "selector_type": "css",
})
```

### Taking Screenshots
```python
result = await tool._execute({
    "action": "screenshot",
    "screenshot_path": "direct_screenshot.png",
})
```

### Executing JavaScript
```python
result = await tool._execute({
    "action": "execute_script",
    "script": "return document.title;",
})
```

### Getting Cookies
```python
result = await tool._execute({
    "action": "get_cookies",
})
```

## Available Actions
The `SeleniumChromeTool` supports the following actions:
- `open_url`: Navigate to a URL
- `find_element`: Locate elements on the page
- `click`: Click on elements
- `type`: Enter text into input fields
- `get_text`: Extract text from elements
- `screenshot`: Capture page screenshots
- `execute_script`: Run JavaScript code
- `navigate`: Browser navigation (back, forward, refresh)
- `get_cookies`: Retrieve browser cookies
- `set_cookie`: Set custom cookies
- `new_tab`: Open a new browser tab
- `close_tab`: Close the current tab

## Troubleshooting

### Chrome Driver Errors
If you see "DevToolsActivePort file doesn't exist":
1. Check Chrome is installed: `google-chrome --version`
2. Update ChromeDriver: `pip install --upgrade webdriver-manager`
3. Try non-headless mode: set `headless=False`
4. Use direct tool example (more reliable)
5. Check Chrome version matches ChromeDriver version

### Model Limitations
If the agent struggles with tool parameters:
- Use a more capable model (llama3.2:latest, mistral, qwen2.5)
- Provide clearer instructions in the system prompt
- Use direct tool usage for complex automation

## Example Output
```
============================================================
  Selenium Browser Automation Demo
============================================================

[1] Basic Web Scraping - Getting page title and URL
    Result: The page title is "Example Domain" and the current URL is https://example.com/

[2] Element Interaction - Finding and reading elements
    Result: The main heading contains the text "Example Domain"

[3] Screenshot Capture - Taking a screenshot of the page
    Result: Screenshot saved as 'example_screenshot.png'

...

============================================================
  Demo complete! Cleaning up...
============================================================
```

## Customization Options
You can modify the agent's behavior by adjusting the `AgentConfig`:
- `name`: Set the agent's display name
- `role`: Choose from available agent roles
- `system_prompt`: Customize tool usage instructions
- `model`: Use a more capable LLM for better tool handling

## When to Use Agent-Based Approach
- **Natural Language Control**: Describe tasks in plain English
- **Complex Workflows**: Multi-step automation tasks
- **Interactive Demos**: Showcase AI capabilities
- **Rapid Prototyping**: Quick automation without code

## When to Use Direct Tool Usage
- **Reliability**: More predictable than agent interpretation
- **Performance**: No LLM overhead
- **Precision**: Exact control over parameters
- **Production**: Stable automation scripts

## Best Practices
1. Use more capable models for complex tool parameters
2. Provide detailed system prompts with action examples
3. Handle exceptions gracefully in production code
4. Use direct tool usage for critical automation
5. Set appropriate timeouts for web operations
6. Clean up resources with `agent.stop()`
7. Use headless mode for background automation
8. Match Chrome and ChromeDriver versions

## Related Examples
- [Basic Chat](basic_chat.md) - Simple chat loop
- [Custom Tool](Custom_tool.md) - Creating custom tools
- [Node Agents Interactive](node_agents_interactive.md) - Multi-agent systems
