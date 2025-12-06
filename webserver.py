# webserver.py
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# -------------------------
# BOT RUNNER
# -------------------------
def run_bot():
    # Importing bot.py will automatically start the bot
    # because VJ-FILTER-BOT starts running on import.
    import bot  # noqa: F401


# -------------------------
# SIMPLE WEB SERVER FOR RENDER
# -------------------------
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"VJ-FILTER-BOT is running!")


def start_webserver():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"Web server running on port {port}")
    server.serve_forever()


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    # Start bot in background thread
    t = threading.Thread(target=run_bot)
    t.daemon = True
    t.start()

    # Start HTTP server (keeps Render service alive)
    start_webserver()
