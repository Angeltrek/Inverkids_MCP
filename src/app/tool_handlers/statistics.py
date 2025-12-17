from src.backend.client import BackendClient
from src.config.constants.endpoint_constants import (
    USER_GRADES_STATS,
    USER_RATES_STATS,
    GET_STATS,
    GET_STATS_USER,
    USER_OVERVIEW,
    USER_OVERVIEW_GROUPS,
    GROUP_PROGRESS,
    ACTIVITY_RATE,
    INACTIVE_USERS,
)
from src.app.models.statistics import (
    GradesInput,
    RatesInput,
    StatsInput,
    StatsUserInput,
    OverviewInput,
    OverviewGroupsInput,
    GroupProgressInput,
)


def grades_handler(args, *, backend_client: BackendClient):
    dto = GradesInput(ids=args["ids"])
    return backend_client.get(
        USER_GRADES_STATS,
        params={"ids": dto.ids},
    )


def rates_handler(args, *, backend_client: BackendClient):
    dto = RatesInput(ids=args["ids"])
    return backend_client.get(
        USER_RATES_STATS,
        params={"ids": dto.ids},
    )


def get_stats_handler(args, *, backend_client: BackendClient):
    dto = StatsInput(
        group_ids=args["group_ids"],
        user_lang=args["user_lang"],
        user_level=args["user_level"],
        user_label=args["user_label"],
    )
    return backend_client.get(
        GET_STATS,
        params=dto.__dict__,
    )


def get_stats_user_handler(args, *, backend_client: BackendClient):
    dto = StatsUserInput(
        user_id=args["user_id"],
        user_lang=args["user_lang"],
        user_level=args["user_level"],
        user_label=args["user_label"],
    )
    return backend_client.get(
        GET_STATS_USER,
        params=dto.__dict__,
    )


def get_overview_handler(args, *, backend_client: BackendClient):
    dto = OverviewInput(school_ids=args["school_ids"])
    return backend_client.get(
        USER_OVERVIEW,
        params={"school_ids": dto.school_ids},
    )


def get_overview_groups_handler(args, *, backend_client: BackendClient):
    dto = OverviewGroupsInput(group_ids=args["group_ids"])
    return backend_client.get(
        USER_OVERVIEW_GROUPS,
        params={"group_ids": dto.group_ids},
    )


def get_group_progress_handler(args, *, backend_client: BackendClient):
    dto = GroupProgressInput(
        group_ids=args["group_ids"],
        white_label=args["white_label"],
        exclude_extra=args.get("exclude_extra", True),
    )
    return backend_client.get(
        GROUP_PROGRESS,
        params=dto.__dict__,
    )


def get_activity_rate_handler(args, *, backend_client: BackendClient):
    return backend_client.get(ACTIVITY_RATE)


def get_inactive_users_handler(args, *, backend_client: BackendClient):
    return backend_client.get(INACTIVE_USERS)
