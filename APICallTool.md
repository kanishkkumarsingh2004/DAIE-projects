# API Call Tool

## Description
A simple demonstration of the DAIE library's `APICallTool` for making HTTP API requests. This example shows how to execute API calls programmatically using the built-in tool system.

## Features
- **HTTP API Calls**: Execute GET, POST, PUT, DELETE requests
- **JSON Response Handling**: Automatic parsing of JSON responses
- **Custom Headers**: Support for custom HTTP headers
- **Async Execution**: Non-blocking API calls using asyncio

## Prerequisites
- Python 3.7+
- DAIE library installed
- Internet connection for API calls

## Usage
```bash
python APICallTool.py
```

## Code Structure
```python
# Main components:
1. Import: APICallTool from daie.tools
2. Tool Initialization: Create APICallTool instance
3. API Execution: Execute HTTP request with URL, method, and headers
4. Result Handling: Print JSON response
```

## Example Output
```json
{
  "login": "octocat",
  "id": 583231,
  "node_id": "MDQ6VXNlcjU4MzIzMQ==",
  "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=4",
  "gravatar_id": "",
  "url": "https://api.github.com/users/octocat",
  "html_url": "https://github.com/octocat",
  "followers_url": "https://api.github.com/users/octocat/followers",
  "following_url": "https://api.github.com/users/octocat/following{/other_user}",
  "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
  "organizations_url": "https://api.github.com/users/octocat/orgs",
  "repos_url": "https://api.github.com/users/octocat/repos",
  "events_url": "https://api.github.com/users/octocat/events{/privacy}",
  "received_events_url": "https://api.github.com/users/octocat/received_events",
  "type": "User",
  "site_admin": false,
  "name": "The Octocat",
  "company": "GitHub",
  "blog": "https://github.blog",
  "location": "San Francisco",
  "email": null,
  "hireable": null,
  "bio": "How people build software",
  "twitter_username": null,
  "public_repos": 8,
  "public_gists": 8,
  "followers": 9000,
  "following": 9,
  "created_at": "2011-01-25T18:44:36Z",
  "updated_at": "2023-01-01T12:00:00Z"
}
```

## API Configuration Options
The `execute()` method accepts the following parameters:
- `url` (required): The API endpoint URL
- `method` (optional): HTTP method (GET, POST, PUT, DELETE). Default: GET
- `headers` (optional): Dictionary of HTTP headers
- `data` (optional): Request body for POST/PUT requests
- `params` (optional): URL query parameters

## Use Cases
- Fetching data from REST APIs
- Integrating external services
- Web scraping (with appropriate APIs)
- Testing API endpoints
- Automating API interactions

## Error Handling
The tool handles common HTTP errors and returns structured responses that can be checked for success or failure.
