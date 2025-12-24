import asyncio
import json
import sys

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

mcp_process = None

BUFFER_LIMIT = 10 * 1024 * 1024

@app.on_event("startup")
async def start_mcp():
    global mcp_process

    mcp_process = await asyncio.create_subprocess_exec(
        sys.executable,
        "start_mcp.py",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        limit=BUFFER_LIMIT,
    )

@app.get("/mcp/stream")
async def stream():
    async def event_stream():
        try:
            while True:
                line = await mcp_process.stdout.readline()
                
                if not line:
                    break
                
                decoded = line.decode('utf-8', errors='replace').strip()
                if decoded:
                    yield f"data: {decoded}\n\n"
                    
        except asyncio.CancelledError:
            pass
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        }
    )

@app.post("/mcp/send")
async def send(payload: dict):
    try:
        data = json.dumps(payload) + "\n"
        mcp_process.stdin.write(data.encode())
        await mcp_process.stdin.drain()
        return {"status": "sent"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
@app.get("/health")
async def health():
    """Health check endpoint"""
    if mcp_process and mcp_process.returncode is None:
        return {"status": "healthy", "mcp_running": True}
    return {"status": "unhealthy", "mcp_running": False}

@app.on_event("shutdown")
async def shutdown():
    if mcp_process:
        mcp_process.terminate()
        await mcp_process.wait()