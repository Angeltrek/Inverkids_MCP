from src.app.dto.curriculum import (
    GetModulesInput,
    GetTopicsByModuleInput,
)
from src.db.queries.curriculum import (
    search_modules,
    get_topics_by_module,
)


def get_modules_handler(args):
    dto = GetModulesInput(
        level=args["level"]
    )

    return {
        "modules": search_modules(
            level=dto.level,
            search=dto.search,
            limit=dto.limit,
        )
    }


def get_topics_by_module_handler(args):
    dto = GetTopicsByModuleInput(
        module_id=args["module_id"]
    )

    return {
        "topics": get_topics_by_module(
            module_id=dto.module_id
        )
    }
