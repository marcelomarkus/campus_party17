import httpx
from fastmcp import FastMCP

client = httpx.AsyncClient(base_url="https://fakestoreapi.com/")

openai_spec = httpx.get("https://fakestoreapi.com/fakestoreapi.json").json()

mcp = FastMCP.from_openapi(openapi_spec=openai_spec, client=client)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(mcp.run(transport="streamable-http"))