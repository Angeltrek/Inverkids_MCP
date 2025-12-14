from src.app.dto.users import SearchUsersInput
from src.db.queries.users import search_users_by_name


def search_users_by_name_handler(args):
    dto = SearchUsersInput(
        query=args["query"],
        user_type=args.get("user_type"),
        limit=args.get("limit", 5),
    )

    return {
        "users": search_users_by_name(
            query=dto.query,
            user_type=dto.user_type,
            limit=dto.limit,
        )
    }
