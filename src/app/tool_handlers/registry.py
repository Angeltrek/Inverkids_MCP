from typing import Dict, Callable, Any

from src.config.constants.tool_names import *

from src.app.tool_handlers.catalog import (
    get_full_catalog_handler,
)

from src.app.tool_handlers.courses import (
    get_courses_handler,
    get_courses_by_user_type_handler,
    get_courses_names_handler,
    get_courses_data_handler,
)

from src.app.tool_handlers.groups import (
    get_groups_handler,
    get_groups_by_level_handler,
    get_group_users_handler,
)

from src.app.tool_handlers.profile import (
    get_profile_handler,
)

from src.app.tool_handlers.statistics import (
    grades_handler,
    rates_handler,
    get_stats_handler,
    get_stats_user_handler,
    get_overview_handler,
    get_overview_groups_handler,
    get_group_progress_handler,
    get_activity_rate_handler,
    get_inactive_users_handler,
)

ToolHandler = Callable[..., Dict[str, Any]]


def get_tool_handler_registry() -> Dict[str, ToolHandler]:
    return {
        GET_FULL_CATALOG: get_full_catalog_handler,

        GET_COURSES: get_courses_handler,
        GET_COURSES_BY_USER_TYPE: get_courses_by_user_type_handler,
        GET_COURSES_NAMES: get_courses_names_handler,
        GET_COURSES_DATA: get_courses_data_handler,

        GET_GROUPS: get_groups_handler,
        GET_GROUPS_BY_LEVEL: get_groups_by_level_handler,
        GET_GROUP_USERS: get_group_users_handler,

        GET_PROFILE: get_profile_handler,

        GET_GRADES: grades_handler,
        GET_RATES: rates_handler,
        GET_STATS: get_stats_handler,
        GET_STATS_USER: get_stats_user_handler,
        GET_OVERVIEW: get_overview_handler,
        GET_OVERVIEW_GROUPS: get_overview_groups_handler,
        GET_GROUP_PROGRESS: get_group_progress_handler,
        GET_ACTIVITY_RATE: get_activity_rate_handler,
        GET_INACTIVE_USERS: get_inactive_users_handler,
    }
