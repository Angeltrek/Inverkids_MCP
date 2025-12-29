import requests
import sys
import json
import threading
import time

STREAM_URL = "https://unlotted-fidelia-scratchiest.ngrok-free.dev/mcp/stream"
SEND_URL = "https://unlotted-fidelia-scratchiest.ngrok-free.dev/mcp/send"

CHUNK_SIZE = 8192


def stream():
    """Recibir respuestas del MCP server"""
    try:
        with requests.get(
            STREAM_URL, 
            stream=True,
            timeout=None,
            headers={
                "Accept": "text/event-stream",
                "Cache-Control": "no-cache",
            }
        ) as r:
            for line in r.iter_lines(decode_unicode=True, chunk_size=CHUNK_SIZE):
                if not line:
                    continue

                if line.startswith("data:"):
                    payload = line.removeprefix("data:").strip()
                    
                    if payload:
                        sys.stdout.write(payload + "\n")
                        sys.stdout.flush()
                        
    except requests.exceptions.Timeout:
        print("Error: Stream timeout", file=sys.stderr)
    except requests.exceptions.ConnectionError as e:
        print(f"Error: Connection failed - {e}", file=sys.stderr)
    except KeyboardInterrupt:
        print("\nStream closed by user", file=sys.stderr)
    except Exception as e:
        print(f"Error in stream: {e}", file=sys.stderr)


def send():
    """Enviar comandos al MCP server"""
    try:
        for line in sys.stdin:
            line = line.strip()
            
            if not line:
                continue
            
            try:
                payload = json.loads(line)
                
                response = requests.post(
                    SEND_URL,
                    json=payload,
                    timeout=300,
                )
                
                if response.status_code != 200:
                    print(f"Error sending: {response.status_code}", file=sys.stderr)
                    
            except json.JSONDecodeError as e:
                print(f"Invalid JSON: {e}", file=sys.stderr)
            except requests.exceptions.Timeout:
                print("Error: Send timeout", file=sys.stderr)
            except Exception as e:
                print(f"Error sending: {e}", file=sys.stderr)
                
    except KeyboardInterrupt:
        print("\nClient stopped", file=sys.stderr)


def main():
    """Iniciar cliente MCP"""
    print("Starting MCP client...", file=sys.stderr)
    print(f"Connecting to: {STREAM_URL}", file=sys.stderr)
    
    stream_thread = threading.Thread(target=stream, daemon=True)
    stream_thread.start()
    
    time.sleep(1)
    
    try:
        send()
    except KeyboardInterrupt:
        print("\nShutting down...", file=sys.stderr)


if __name__ == "__main__":
    main()