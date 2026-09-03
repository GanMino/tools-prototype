import http.server, socketserver, os, functools

DIR = "/Users/mingan/Desktop/work/学习/tools-prototype"
PORT = 4180

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DIR, **kw)
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".woff2": "font/woff2",
        ".woff": "font/woff",
        ".html": "text/html; charset=utf-8",
        ".js": "text/javascript; charset=utf-8",
    }
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()
    def log_message(self, fmt, *args):
        pass

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", PORT), H) as httpd:
    print("serving on http://127.0.0.1:%d" % PORT, flush=True)
    httpd.serve_forever()
