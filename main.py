from fastmcp import FastMCP
from typing import List, Dict, Any

mcp_servidor = FastMCP(
    name="MCP Server",
    instructions="Você é um assistente de lista de compras. Ajude o usuário a adicionar itens e listar os itens da lista de compras.",
)


lista_de_compras: List[Dict[str, Any]] = []

@mcp_servidor.tool()
def adicionar_item(item: str, quantidade: str = "1 unidade") -> str:
    """Adiciona um item à lista de compras."""
    global lista_de_compras
    lista_de_compras.append({"item": item, "quantidade": quantidade})
    return f"Item '{item}' adicionado com quantidade {quantidade}."

@mcp_servidor.tool()
def listar_itens() -> List[Dict[str, Any]]:
    """Lista todos os itens da lista de compras."""
    return lista_de_compras

@mcp_servidor.prompt()
def prompt() -> str:
    return "Você é um assistente de lista de compras. Ajude o usuário a adicionar itens e listar os itens da lista de compras."


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(mcp_servidor.run(transport="sse"))
