from src.app.dto.activities import (
    GetActivityInput,
    GetActivitiesByTopicInput,
)
from src.db.queries.activities import (
    get_activity_by_id,
    get_activities_by_topic,
)


def get_activity_handler(args):
    dto = GetActivityInput(
        activity_id=args["activity_id"]
    )

    return {
        "activity": get_activity_by_id(
            activity_id=dto.activity_id
        )
    }


def get_activities_by_topic_handler(args):
    dto = GetActivitiesByTopicInput(
        topic_id=args["topic_id"],
        activity_type=args.get("activity_type"),
        limit=args.get("limit", 5),
    )

    return {
        "activities": get_activities_by_topic(
            topic_id=dto.topic_id,
            activity_type=dto.activity_type,
            limit=dto.limit,
        )
    }
