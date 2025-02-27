import http.server
import socketserver

PORT = 8080

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        return super().do_GET()

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
