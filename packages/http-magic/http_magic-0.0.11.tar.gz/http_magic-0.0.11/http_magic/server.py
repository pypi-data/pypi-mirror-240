from .log import Log
from .session import MagicSessionManager
from .http import HttpRequest, HttpResponse
from .container import MagicContainer
from http.server import BaseHTTPRequestHandler, HTTPServer


class MagicServer:
    class Handler(BaseHTTPRequestHandler):
        _session_manager: MagicSessionManager = None
        _root_container: MagicContainer = None

        def log_request(self, code='-', size='-'):
            pass

        def log_error(self, *args):
            pass

        def log_message(self, format, *args):
            pass

        def __init__(self, *args, **kwargs):
            self.session = None
            BaseHTTPRequestHandler.__init__(self, *args, **kwargs)

        def __send_response__(self, response: HttpResponse):
            Log("Response started")
            self.send_response(response.code)
            for cookie in response.cookies.to_simple_cookie().values():
                self.send_header('Set-Cookie', cookie.OutputString())
            response.headers['Content-length'] = str(len(response.body))
            response.headers['Content-type'] = response.content_type
            for header in response.headers:
                self.send_header(header.key, header.value)
            response_body = response.body
            self.end_headers()
            self.wfile.write(response_body)
            Log("Response sent")

        def __process_request__(self):
            request = HttpRequest(self)
            Log("%s request received" % request.method)
            if self._session_manager:
                request.session = self._session_manager.get_session(request)
                Log("Session %s loaded" % request.session.key())
            else:
                request.session = None

            response = self._root_container.__route__(request)

            if self._session_manager:
                self._session_manager.save_session(response, request.session)
                Log("Session %s saved" % request.session.key())

            self.__send_response__(response)

    def __init__(self,
                 root_container,
                 session_manager: MagicSessionManager = None,
                 port: int = 8080,
                 ip: str = "0.0.0.0"):
        self.ip = ip
        self.port = port
        self.root_container = root_container()
        self.session_manager = session_manager

        class NewHandler(MagicServer.Handler):
            _session_manager = self.session_manager
            _root_container = self.root_container

        self.handler = NewHandler
        from .method import HttpMethod
        for method in HttpMethod.all_methods():
            setattr(NewHandler, "do_%s" % method, self.handler.__process_request__)

        self.http_server = None

    def start(self):
        Log("Server started on port %i" % self.port)
        self.http_server = HTTPServer(("", self.port), self.handler)
        self.http_server.serve_forever()
