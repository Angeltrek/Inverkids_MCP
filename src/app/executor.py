from src.app.router import route_tool_call
from src.llm.client import get_llm_client
from src.rag.context_builder import build_context
from src.llm.tools.registry import get_llm_tools

def execute_agent(prompt: str) -> str:
    llm = get_llm_client()
    tools = get_llm_tools()

    context = build_context(prompt)

    response = llm.generate(
        prompt=context,
        tools=tools,
    )

    tool_call = response.get("tool_call")
    print("TOOL CALL:", tool_call)
    if not tool_call:
        return response["content"]

    tool_result = route_tool_call(tool_call)

    final_response = llm.generate(
        prompt=f"""
            Tool result:
            {tool_result}

            Answer the user in natural language.
        """,
    )

    return final_response["content"]
