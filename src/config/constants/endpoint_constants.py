# Endpoint Constants
BASE = "/api"

# Login Endpoints
LOGIN = f"{BASE}/login"
GOOGLE_LOGIN = f"{BASE}/google_login"
LOBBY_LOGIN = f"{BASE}/lobby_login"

# User Profile Endpoints
PROFILE_GET = f"{BASE}/profile"

# Catalog Endpoints
CATALOG_FULL = f"{BASE}/catalog/full_catalog"

# Topics Endpoints
TOPICS_LIST = f"{BASE}/topics"
TOPICS_NAMES = f"{BASE}/topics_list"
TOPIC_CONTENT = f"{BASE}/topics/get_topic_content"

TOPIC_ACTIVITY_CONTENT = f"{BASE}/topics/get_activity_content"
TOPIC_TEXT_CONTENT = f"{BASE}/topics/get_text_content"
TOPIC_BOOK_CONTENT = f"{BASE}/topics/get_book_content"
TOPIC_VIDEO_CONTENT = f"{BASE}/topics/get_video_content"
TOPIC_GAME_CONTENT = f"{BASE}/topics/get_game_content"

# Modules Endpoints
MODULE_CONTINUE = f"{BASE}/modules/get_continue_module"
MODULE_CONTENT = f"{BASE}/modules/get_module_content"
MODULE_NAMES = f"{BASE}/modules/get_module_names"
LEVEL_NAMES = f"{BASE}/modules/get_level_names"
LABEL_NAMES = f"{BASE}/modules/get_label_names"

# Courses Endpoints
COURSES_LIST = f"{BASE}/courses"
COURSES_DATA = f"{BASE}/courses/get_courses_data"
COURSES_NAMES = f"{BASE}/courses/get_courses_names"

# Grades Endpoints
GRADES_INDEX = f"{BASE}/grades"
GRADES_USER = f"{BASE}/grades/user_grades"
GRADES_FULL = f"{BASE}/grades/full_grades"
GRADES_TOPIC = f"{BASE}/topic_grades"

# Groups Endpoints
GROUPS_LIST = f"{BASE}/groups"
GROUPS_BY_LEVEL = f"{BASE}/groups/get_groups_level"
GROUP_USERS = f"{BASE}/groups/get_group_users"

# Students Endpoints
STUDENTS_LIST = f"{BASE}/students"
STUDENTS_BY_TEACHER = f"{BASE}/students/my_students"

# Leaderboards Endpoints
LEADERBOARDS = f"{BASE}/leaderboards"
LEADERBOARDS_GENERAL = f"{BASE}/leaderboards_general"
LEADERBOARDS_TEACHER = f"{BASE}/leaderboards_teacher/"
LEADERBOARDS_TOP_SCHOOLS = f"{BASE}/leaderboards/index_top_5_schools"

# Analytics Endpoints
USER_GRADES_STATS = f"{BASE}/statistics/grades"
USER_GRADES_KIDS = f"{BASE}/statistics/gradesKids"

USER_RATES_STATS = f"{BASE}/statistics/rates"
USER_RATES_KIDS = f"{BASE}/statistics/ratesKids"

GET_STATS = f"{BASE}/statistics/get_stats"
GET_STATS_USER = f"{BASE}/statistics/get_stats_user"

USER_OVERVIEW = f"{BASE}/statistics/get_overview"
USER_OVERVIEW_GROUPS = f"{BASE}/statistics/get_overview_groups"

GROUP_PROGRESS = f"{BASE}/statistics/get_group_progress"
ACTIVITY_RATE = f"{BASE}/statistics/get_activity_rate"

INACTIVE_USERS = f"{BASE}/statistics/get_inactive_users"