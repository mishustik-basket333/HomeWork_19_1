from http.server import BaseHTTPRequestHandler

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_POST(self):
        data_len = int(self.headers.get('Content-Length'))
        data = self.rfile.read(data_len)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(f'{data.decode()}', "utf-8"))

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("Hello, World wide web!", "utf-8"))
