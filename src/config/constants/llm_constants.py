# LLM provider and model defaults
DEFAULT_LLM_PROVIDER = "openai"
DEFAULT_OPENAI_MODEL = "gpt-4.1"

# Agent execution defaults
DEFAULT_MAX_AGENT_STEPS = 5
AGENT_FAILURE_MESSAGE = "I could not complete the request safely."

# Message roles (provider-agnostic)
LLM_ROLE_SYSTEM = "system"
LLM_ROLE_USER = "user"
LLM_ROLE_ASSISTANT = "assistant"
LLM_ROLE_TOOL = "tool"

# Message keys (provider-agnostic)
LLM_KEY_ROLE = "role"
LLM_KEY_CONTENT = "content"
LLM_KEY_TOOL_CALLS = "tool_calls"
LLM_KEY_TOOL_CALL_ID = "tool_call_id"


# Tool call structure keys (provider-agnostic)
LLM_TOOL_KEY_ID = "id"
LLM_TOOL_KEY_TYPE = "type"
LLM_TOOL_KEY_FUNCTION = "function"
LLM_TOOL_KEY_NAME = "name"
LLM_TOOL_KEY_ARGUMENTS = "arguments"

LLM_TOOL_TYPE_FUNCTION = "function"
