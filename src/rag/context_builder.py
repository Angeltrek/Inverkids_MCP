def build_context(prompt: str) -> str:
    """
    Normalize the user prompt.
    No retrieval. No documents. No RAG yet.
    """

    return f"""
        You are an educational assistant.
        Answer using available tools when appropriate.

        User question:
        {prompt}
    """.strip()
