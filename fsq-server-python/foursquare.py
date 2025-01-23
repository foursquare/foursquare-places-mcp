from typing import Any
import geocoder
import httpx
import json
from mcp.server.fastmcp import FastMCP
import os
from urllib.parse import urlencode


# Initialize FastMCP server
mcp = FastMCP("foursquare")

# Constants
FSQ_API_BASE = "https://api.foursquare.com"
FSQ_API_TOKEN = os.getenv("FOURSQUARE_API_TOKEN")

async def submit_fsq_request(url: str) -> dict[str, Any] | None:
    """Make a request to the Foursquare API with proper error handling."""
    headers = {
        "Authorization": FSQ_API_TOKEN,
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


@mcp.tool()
async def search_near(where: str, what: str) -> str:
    """Search for places near a particular named region

    Args:
        where: a geographic region (e.g., Los Angeles, Fort Greene)
        what: concept you are looking for (e.g., coffee shop, Hard Rock Cafe)
    """
    params = {
        "query": what,
        "near": where
    }
    encoded_params = urlencode(params)
    url = f"{FSQ_API_BASE}/v3/places/search?{encoded_params}&limit=5"
    res = await submit_fsq_request(url)

    return json.dumps(res)


@mcp.tool()
async def search_near_point(what: str, ll: str, radius: int) -> str:
    """Search for places near a particular point

    Args:
        what: concept you are looking for (e.g., coffee shop, Hard Rock Cafe)
        ll: comma separated latitude and longitude pair (e.g., 40.74,-74.0)
        radius: distance in meters (e.g., 1000)
    """
    params = {
        "query": what,
        "ll": ll,
        "radius": radius
    }
    encoded_params = urlencode(params)
    url = f"{FSQ_API_BASE}/v3/places/search?{encoded_params}&limit=5"
    res = await submit_fsq_request(url)

    return json.dumps(res)


@mcp.tool()
async def get_ip_location() -> str:
    """Guess user's location based on ip address. Useful if the user has
       not provided their own location.
    """
    location = geocoder.ip('me')
    if not location.ok:
        return "I don't know where you are"
    return f"{location.lat},{location.lng}"


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
