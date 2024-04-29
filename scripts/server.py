import urllib.parse
import http.server
import socketserver
import json
from template import homepageHTML

from game import Game

demoGame = Game()

class CarHandler(http.server.SimpleHTTPRequestHandler):
    def _send_content(self, data, status=200, content_type="text/plain"):
        if isinstance(data, str):
            data = data.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)
        self.wfile.flush()

    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        if url.path == "/":
            return self._send_content(
                homepageHTML,
                content_type="text/html",
            )
        elif url.path == "/try":
            qs = urllib.parse.parse_qs(url.query)
            answer = qs["input"][0]
            if demoGame.check(answer):
                res = {"correct":True}
            else:
                res = {"correct":False}
            return self._send_content(json.dumps(res), content_type="application/json")
        else:
            return self._send_content(f"404: {url}", status=400)


if __name__ == "__main__":
    PORT = 5000
    with socketserver.TCPServer(("", PORT), CarHandler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()




