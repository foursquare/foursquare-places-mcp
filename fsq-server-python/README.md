# Python Server for Foursquare API

## Getting Started

### Prerequisites

* Download Claude Desktop
* Get a Foursquare API Key
* Ensure Python 3.10 or higher
* Install `uv`, a lightweight dev python server, e.g.:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

* Clone this repo
* Add the "foursquare" server with correct local configuration to ~/Library/Application\ Support/Claude/claude_desktop_config.json based on the example [claude_desktop_config.json](claude_desktop_config.json) in the project
* Run Claude Desktop and verify that search_near and other foursquare MCP tools are available
* Test it out by asking Claude for place recommendations near you!