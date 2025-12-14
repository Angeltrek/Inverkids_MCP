from src.app.dto.communication import RequestGuardianContactInput


def request_guardian_contact_handler(args):
    dto = RequestGuardianContactInput(
        reason=args["reason"],
        channel=args["channel"],
    )

    # At this stage, this is intentionally a stub.
    # In the future this may:
    # - enqueue a message
    # - trigger a workflow
    # - notify a teacher/guardian
    # - require admin approval

    return {
        "status": "queued",
        "channel": dto.channel,
        "reason": dto.reason,
    }
