# Endpoint Constants
BASE = "/api"

# Login Endpoints
LOGIN = f"{BASE}/login"
GOOGLE_LOGIN = f"{BASE}/google_login"
LOBBY_LOGIN = f"{BASE}/lobby_login"

# User Profile Endpoints
MCP_PROFILE = f"{BASE}/mcp/get_current_user"

# Catalog Endpoints
CATALOG_FULL = f"{BASE}/catalog/full_catalog"

# Courses Endpoints
COURSES_LIST = f"{BASE}/courses"
COURSES_DATA = f"{BASE}/courses/get_courses_data"
COURSES_NAMES = f"{BASE}/courses/get_courses_names"

# Groups Endpoints
MCP_GROUPS = f"{BASE}/mcp/get_groups"
GROUPS_BY_LEVEL = f"{BASE}/groups/get_groups_level"
GROUP_USERS = f"{BASE}/groups/get_group_users"

# MCP Endpoints
MCP_MODULES = f"{BASE}/mcp/get_modules"
MCP_TOPICS = f"{BASE}/mcp/get_topics"
MCP_ACTIVITIES = f"{BASE}/mcp/get_activities"
MCP_TEXTS = f"{BASE}/mcp/get_texts"
MCP_USERS = f"{BASE}/mcp/get_users"
MCP_SCHOOLS = f"{BASE}/mcp/get_schools"
MCP_GRADES = f"{BASE}/mcp/get_grades"
MCP_FEEDBACK = f"{BASE}/mcp/get_feedback"