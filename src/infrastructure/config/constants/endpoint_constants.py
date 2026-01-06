# Endpoint Constants
BASE = "/api"

# Modules
MCP_MODULES = f"{BASE}/mcp/get_modules"
MCP_MODULES_BY_LEVEL = f"{BASE}/mcp/get_modules_by_level"
MCP_MODULES_BY_WHITE_LABEL = f"{BASE}/mcp/get_modules_by_white_label"
MCP_MODULES_BY_LEVEL_AND_WHITE_LABEL = f"{BASE}/mcp/get_modules_by_level_and_white_label"
MCP_MODULES_BY_NUMBER = f"{BASE}/mcp/get_modules_by_number"
MCP_LAST_MODULE_BY_LEVEL = f"{BASE}/mcp/get_last_module_by_level"

# Modules – search & detail
MCP_SEARCH_MODULES_BY_NAME = f"{BASE}/mcp/search_modules_by_name"
MCP_MODULE_DETAIL = f"{BASE}/mcp/get_module_detail"


# Topics
MCP_TOPICS = f"{BASE}/mcp/get_topics"
MCP_TOPICS_BY_LEVEL = f"{BASE}/mcp/get_topics_by_level"
MCP_LAST_TOPIC_BY_MODULE = f"{BASE}/mcp/get_last_topic_by_module"

# Topics – assessment
MCP_TOPICS_WITH_QUIZ = f"{BASE}/mcp/get_topics_with_quiz"
MCP_TOPICS_WITH_EVAL = f"{BASE}/mcp/get_topics_with_eval"
MCP_TOPICS_WITH_DIAG = f"{BASE}/mcp/get_topics_with_diag"
MCP_TOPICS_WITHOUT_ASSESSMENT = f"{BASE}/mcp/get_topics_without_assessment"

# Topics – search & detail
MCP_SEARCH_TOPICS_BY_NAME = f"{BASE}/mcp/search_topics_by_name"
MCP_SEARCH_TOPICS_BY_NAME_IN_MODULE = f"{BASE}/mcp/search_topics_by_name_in_module"
MCP_TOPIC_DETAIL = f"{BASE}/mcp/get_topic_detail"


# Activities
MCP_ACTIVITIES_BY_MODULE = f"{BASE}/mcp/get_activities_by_module"
MCP_ACTIVITIES_BY_TYPE = f"{BASE}/mcp/get_activities_by_type"
MCP_ACTIVITIES_BY_LEVEL = f"{BASE}/mcp/get_activities_by_level"

# Activities – flow
MCP_FIRST_ACTIVITY_BY_TOPIC = f"{BASE}/mcp/get_first_activity_by_topic"
MCP_EXTRA_ACTIVITIES = f"{BASE}/mcp/get_extra_activities"

# Activities – relations & search
MCP_ACTIVITIES_BY_SKILL = f"{BASE}/mcp/get_activities_by_skill"
MCP_SEARCH_ACTIVITIES_BY_NAME = f"{BASE}/mcp/search_activities_by_name"

# Activity detail
MCP_ACTIVITY_DETAIL = f"{BASE}/mcp/get_activity_detail"


# Texts
MCP_TEXTS = f"{BASE}/mcp/get_texts"
MCP_TEXTS_BY_MODULE = f"{BASE}/mcp/get_texts_by_module"
MCP_TEXTS_BY_TOPIC = f"{BASE}/mcp/get_texts_by_topic"
MCP_TEXTS_BY_LEVEL = f"{BASE}/mcp/get_texts_by_level"

# Texts – flow
MCP_HOME_TEXTS = f"{BASE}/mcp/get_home_texts"
MCP_ENTRY_TEXTS = f"{BASE}/mcp/get_entry_texts"

# Texts – classification & search
MCP_TEXTS_BY_TYPE = f"{BASE}/mcp/get_texts_by_type"
MCP_TEXTS_BY_SKILL = f"{BASE}/mcp/get_texts_by_skill"
MCP_SEARCH_TEXTS_BY_NAME = f"{BASE}/mcp/search_texts_by_name"

# Text detail
MCP_TEXT_DETAIL = f"{BASE}/mcp/get_text_detail"


# Skills
MCP_SKILLS = f"{BASE}/mcp/get_skills"
MCP_SKILLS_BY_TYPE = f"{BASE}/mcp/get_skills_by_type"
MCP_SEARCH_SKILLS = f"{BASE}/mcp/search_skills"
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
