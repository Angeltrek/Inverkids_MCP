from typing import Any

from src.utils.exceptions import ValidationError

CHOICE_BASED_TYPES = {"multiple_choice", "true_false"}


def validate_exercises(exercises: Any) -> list[dict]:
    if not isinstance(exercises, list) or not exercises:
        raise ValidationError(
            "activity.exercises must be a non-empty list",
            field="exercises",
        )

    for idx, exercise in enumerate(exercises):
        if not isinstance(exercise, dict):
            raise ValidationError(
                f"exercises[{idx}] must be an object",
                field="exercises",
            )

        exercise_type = exercise.get("type")
        if not exercise_type or not isinstance(exercise_type, str):
            raise ValidationError(
                f"exercises[{idx}].type is required",
                field="exercises",
            )

        if exercise_type not in CHOICE_BASED_TYPES:
            continue

        options = exercise.get("options")
        if not isinstance(options, list) or len(options) < 2:
            raise ValidationError(
                f"exercises[{idx}] has type '{exercise_type}' and REQUIRES a non-empty "
                "'options' array (at least 2 choices). Regenerate this exercise with its "
                "options included.",
                field="exercises",
            )

        if any(not isinstance(opt, str) or not opt.strip() for opt in options):
            raise ValidationError(
                f"exercises[{idx}].options must contain only non-empty strings",
                field="exercises",
            )

        correct_option = exercise.get("correct_option")
        if not correct_option or not isinstance(correct_option, str):
            raise ValidationError(
                f"exercises[{idx}] has type '{exercise_type}' and REQUIRES a "
                "'correct_option' field naming the correct choice.",
                field="exercises",
            )

        if correct_option not in options:
            raise ValidationError(
                f"exercises[{idx}].correct_option ('{correct_option}') must match one of "
                "its 'options'",
                field="exercises",
            )

    return exercises


def validate_activity_content(activity: Any) -> dict:
    if not isinstance(activity, dict):
        raise ValidationError("activity must be an object", field="activity")

    validate_exercises(activity.get("exercises"))

    return activity