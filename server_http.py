import asyncio
import sys
import json
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

mcp_process = None

@app.on_event("startup")
async def start_mcp():
    global mcp_process

    mcp_process = await asyncio.create_subprocess_exec(
        sys.executable,
        "start_mcp.py",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
    )

@app.get("/mcp/stream")
async def stream():
    async def event_stream():
        while True:
            line = await mcp_process.stdout.readline()
            if not line:
                break
            yield f"data: {line.decode()}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
    )

@app.post("/mcp/send")
async def send(payload: dict):
    data = json.dumps(payload) + "\n"
    mcp_process.stdin.write(data.encode())
    await mcp_process.stdin.drain()

    return {"status": "sent"}

