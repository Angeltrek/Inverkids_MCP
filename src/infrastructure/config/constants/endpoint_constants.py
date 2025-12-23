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

# Courses Endpoints
COURSES_LIST = f"{BASE}/courses"
COURSES_DATA = f"{BASE}/courses/get_courses_data"
COURSES_NAMES = f"{BASE}/courses/get_courses_names"

# Groups Endpoints
GROUPS_LIST = f"{BASE}/groups"
GROUPS_BY_LEVEL = f"{BASE}/groups/get_groups_level"
GROUP_USERS = f"{BASE}/groups/get_group_users"