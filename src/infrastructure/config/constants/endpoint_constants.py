# Endpoint Constants
BASE = "/api"

# Modules
MCP_MODULES = f"{BASE}/mcp/get_modules"
MCP_MODULES_BY_WHITE_LABEL = f"{BASE}/mcp/get_modules_by_white_label"
MCP_MODULES_BY_LEVEL_AND_WHITE_LABEL = f"{BASE}/mcp/get_modules_by_level_and_white_label"
MCP_MODULES_BY_NUMBER = f"{BASE}/mcp/get_modules_by_number"

# Modules – search & detail
MCP_MODULE_DETAIL = f"{BASE}/mcp/get_module_detail"


# Topics
MCP_TOPICS = f"{BASE}/mcp/get_topics"
MCP_TOPICS_BY_LEVEL = f"{BASE}/mcp/get_topics_by_level"
MCP_TOPICS_BY_TAGS = f"{BASE}/mcp/get_topics_by_tags"

# Topics – search & detail
MCP_TOPIC_DETAIL = f"{BASE}/mcp/get_topic_detail"


# Activities
MCP_ACTIVITIES_BY_MODULE = f"{BASE}/mcp/get_activities_by_module"
MCP_ACTIVITIES_BY_LEVEL = f"{BASE}/mcp/get_activities_by_level"

# Activities – relations & search
MCP_ACTIVITIES_BY_SKILL = f"{BASE}/mcp/get_activities_by_skill"

# Activity detail
MCP_ACTIVITY_DETAIL = f"{BASE}/mcp/get_activity_detail"


# Texts
MCP_TEXTS = f"{BASE}/mcp/get_texts"
MCP_TEXTS_BY_MODULE = f"{BASE}/mcp/get_texts_by_module"
MCP_TEXTS_BY_TOPIC = f"{BASE}/mcp/get_texts_by_topic"
MCP_TEXTS_BY_LEVEL = f"{BASE}/mcp/get_texts_by_level"

# Texts – classification & search
MCP_TEXTS_BY_TYPE = f"{BASE}/mcp/get_texts_by_type"
MCP_TEXTS_BY_SKILL = f"{BASE}/mcp/get_texts_by_skill"

# Text detail
MCP_TEXT_DETAIL = f"{BASE}/mcp/get_text_detail"


# Skills
MCP_SKILLS = f"{BASE}/mcp/get_skills"
MCP_SKILL_DETAIL = f"{BASE}/mcp/get_skill_detail"


# Grades
MCP_GRADES_BY_LEVEL = f"{BASE}/mcp/get_grades_by_level"
MCP_GRADES_BY_GROUP = f"{BASE}/mcp/get_grades_by_group"
MCP_GRADES_BY_STUDENT = f"{BASE}/mcp/get_grades_by_student"
MCP_GRADES_BY_MODULE = f"{BASE}/mcp/get_grades_by_module"
MCP_GRADES_BY_TOPIC = f"{BASE}/mcp/get_grades_by_topic"
MCP_GRADES_BY_ACTIVITY = f"{BASE}/mcp/get_grades_by_activity"

# Grades – summary & detail
MCP_GRADES_SUMMARY = f"{BASE}/mcp/get_grades_summary"
MCP_GRADE_DETAIL = f"{BASE}/mcp/get_grade_detail"


# Feedback
MCP_FEEDBACK_LIST = f"{BASE}/mcp/get_feedback_list"
MCP_FEEDBACK_DETAIL = f"{BASE}/mcp/get_feedback_detail"


# Users
MCP_USERS_LIST = f"{BASE}/mcp/get_users_list"
MCP_USER_DETAIL = f"{BASE}/mcp/get_user_detail"


# Groups
MCP_GROUPS_LIST = f"{BASE}/mcp/get_groups_list"
MCP_GROUP_DETAIL = f"{BASE}/mcp/get_group_detail"


# Schools
MCP_SCHOOLS_LIST = f"{BASE}/mcp/get_schools_list"
MCP_SCHOOL_DETAIL = f"{BASE}/mcp/get_school_detail"

# Tags
MCP_TAGS_LIST = f"{BASE}/mcp/get_tags"

# Virtual Modules
MCP_CREATE_VIRTUAL_MODULE = f"{BASE}/mcp/create_virtual_module"
MCP_VIRTUAL_MODULES = f"{BASE}/mcp/get_virtual_modules_list"
MCP_VIRTUAL_MODULE_DETAIL = f"{BASE}/mcp/get_virtual_module_detail"
