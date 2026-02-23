import threading
import time
from queue import Queue
from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
queue = Queue() # In-memory queue for incoming messages
def worker():
    """Background worker that processes messages from the queue."""
    print("[WORKER] Starting background worker, waiting for messages...")
    while True:
        message = queue.get()  # blocks until a message is available
        try:
            print(f"[WORKER] Received: {message}")
            time.sleep(1) # Simulate processing
            result = message.upper()
            print(f"[WORKER] Processed result: {result}")
        except Exception as e:
            print(f"[WORKER] Error while processing: {e}")
        finally:
            queue.task_done()
 
# Start the worker thread
thread = threading.Thread(target=worker, daemon=True)
thread.start()
 
@app.route("/healthz")
def health():
    return "ok", 200
 
@app.route("/log", methods=["POST"])
def log_message():
    data = request.get_json(force=True, silent=True) or {}
    message = data.get("message")
    if not message:
        return jsonify({"error": "message is required"}), 400
 
    # Enqueue message instead of processing synchronously
    queue.put(message)
    return jsonify({"status": "queued", "message": message}), 202
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
