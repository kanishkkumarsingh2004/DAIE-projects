import asyncio
from daie.tools import APICallTool

async def main():
    api = APICallTool()
    result = await api.execute({
        "url": "https://api.github.com/users/octocat",
        "method": "GET",
        "headers": {"Accept": "application/json"},
    })
    print(result["json"])

if __name__ == "__main__":
    asyncio.run(main())