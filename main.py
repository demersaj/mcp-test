import asyncio
import os
from dotenv import load_dotenv
from mcp_use import MCPClient

load_dotenv()

async def main():
    config = {
        "mcpServers": {
            "weather": {
                "command": "npx",
                "args": ["-y", "@timlukahorstmann/mcp-weather"],
                "env": {
                    "ACCUWEATHER_API_KEY": os.getenv("ACCUWEATHER_API_KEY")
                }
            }
        }
    }

    client = MCPClient.from_dict(config)
    await client.create_all_sessions()

    session = client.get_session("weather")
    result = await session.call_tool(name="weather-get_hourly", arguments={"location": "Austin, TX", "units": "imperial"})

    print(f"Result: {result.content[0].text}")
    await client.close_all_sessions()

asyncio.run(main())
