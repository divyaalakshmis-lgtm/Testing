import requests
from fastmcp import FastMCP

mcp = FastMCP("WeatherTime", stateless_http=True)

@mcp.tool(description="Order Cancellation based on the user query.")
def order_cancellation(usermessage: str) -> dict:
    response = requests.post(
        "http://localhost:5000/query_api",
        headers={"Content-Type": "application/json"},
        json={
            "user_query": usermessage,
            "agentId": "688",
            "UserID": "pagetest",
            "chat_id": ""
        },
    )
    response.raise_for_status()
    return response.json()

@mcp.tool(description="Use this tool ONLY when the user wants to browse, list,or search for general products without asking for recommendations.Examples: 'show me phones', 'list available products','what items are in stock'.DO NOT use this tool for recommendations, comparisons, or laptops.")
def product_listing(usermessage: str) -> dict:
    response = requests.post(
        "http://localhost:5000/query_api",
        headers={"Content-Type": "application/json"},
        json={
            "user_query": usermessage,
            "agentId": "684",
            "UserID": "pagetest",
            "chat_id": ""
        },
    )
    response.raise_for_status()
    return response.json()

@mcp.tool(description="Place an order based on the user query.")
def place_order(usermessage: str) -> dict:
    response = requests.post(
        "http://localhost:5000/query_api",
        headers={"Content-Type": "application/json"},
        json={
            "user_query": usermessage,
            "agentId": "689",
            "UserID": "pagetest",
            "chat_id": ""
        },
    )
    response.raise_for_status()
    return response.json()

@mcp.tool(description="Use this tool ONLY when the user explicitly asks for a LAPTOP recommendation. This includes choosing a laptop based on brand, size, color, budget, performance needs, or comparisons. Examples: 'recommend a Dell laptop', 'best laptop under 1000', 'laptop with 16GB RAM'. DO NOT use this tool for general product listings.")
def laptop_recommendation(usermessage: str) -> dict:
    response = requests.post(
        "http://localhost:5000/query_api",
        headers={"Content-Type": "application/json"},
        json={
            "user_query": usermessage,
            "agentId": "695",
            "UserID": "pagetest",
            "chat_id": ""
        },
    )
    response.raise_for_status()
    return response.json()

mcp.add_tool(order_cancellation)
mcp.add_tool(product_listing)
mcp.add_tool(place_order)
mcp.add_tool(laptop_recommendation)

app = mcp.http_app(path="/mcp")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)