import requests
import sys
import json

STREAM_URL = "https://unlotted-fidelia-scratchiest.ngrok-free.dev/mcp/stream"
SEND_URL = "https://unlotted-fidelia-scratchiest.ngrok-free.dev/mcp/send"


def stream():
    with requests.get(STREAM_URL, stream=True) as r:
        for line in r.iter_lines():
            if not line:
                continue

            text = line.decode()

            if not text.startswith("data:"):
                continue

            payload = text.removeprefix("data: ").strip()

            sys.stdout.write(payload + "\n")
            sys.stdout.flush()


def send():
    for line in sys.stdin:
        if not line.strip():
            continue

        requests.post(
            SEND_URL,
            json=json.loads(line),
        )


import threading
threading.Thread(target=stream, daemon=True).start()
send()
