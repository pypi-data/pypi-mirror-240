import http.cookies
from json_cpp import JsonObject, JsonList
from datetime import datetime
from .content import Content


class HttpDate:
    date_format = "%a, %d %b %Y %H:%M:%S GMT"


class HttpMethod:
    Post = "POST"
    Get = "GET"
    Put = "PUT"
    Delete = "DELETE"
    Head = "HEAD"
    Patch = "PATCH"
    Connection = "CONNECTION"
    Options = "OPTIONS"
    @staticmethod
    def all_methods():
        return [getattr(HttpMethod, m) for m in vars(HttpMethod)
                if m[0] != "_" and isinstance(getattr(HttpMethod, m), str)]


class Header(JsonObject):
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        JsonObject.__init__(self)


class Headers(JsonList):
    def __init__(self, headers_dict=None):
        if headers_dict is None:
            headers_dict = dict()
        JsonList.__init__(self, list_type=Header)
        self._dict = {}
        for key in headers_dict:
            self.append(Header(key, headers_dict[key]))
            self._dict[key] = headers_dict[key]

    def __getitem__(self, item):
        if type(item) is str:
            return self._dict[item]
        else:
            return self[item]

    def __contains__(self, item):
        return item in self._dict

    def __setitem__(self, key, value):
        header = Header(key, value)
        if key in self._dict:
            i = self.find_first_index(key=lambda c: c.key == key)
            self.pop(i)
        self.append(header)
        self._dict[key] = header

    def to_dict(self):
        d = {}
        for h in self:
            d[h.key] = h.value


class Cookie(JsonObject):
    def __init__(self,
                 key="",
                 value="",
                 expires: datetime = None,
                 path: str = None,
                 comment: str = None,
                 domain: str = None,
                 max_age: str = None,
                 secure: str = None,
                 http_only: str = None,
                 version: str = None,
                 same_site: str = None):
        self.key = key
        self.value = value
        self.expires = expires
        self.path = path
        self.comment = comment
        self.domain = domain
        self.max_age = max_age
        self.secure = secure
        self.http_only = http_only
        self.version = version
        self.same_site = same_site
        JsonObject.__init__(self)


    @staticmethod
    def from_morsel(morsel):
        if morsel["expires"]:
            expires = datetime.strptime(morsel["expires"], HttpDate.date_format)
        else:
            expires = None
        nc = Cookie(
            key=morsel.key,
            value=morsel.value,
            expires=expires,
            path=morsel["path"],
            comment=morsel["comment"],
            domain=morsel["domain"],
            max_age=morsel["max-age"],
            secure=morsel["secure"],
            http_only=morsel["httponly"],
            version=morsel["version"],
            same_site=morsel["samesite"]
        )
        return nc


class Cookies(JsonList):

    def __init__(self, cookie_reader=None):
        if cookie_reader is None:
            cookie_reader = {}
        JsonList.__init__(self, list_type=Cookie)
        self._dict = {}
        for cookie in cookie_reader:
            nc = Cookie.from_morsel(cookie_reader[cookie])
            self.append(nc)
            self._dict[nc.key] = nc

    def __getitem__(self, item):
        if type(item) is str:
            return self._dict[item]
        else:
            return self[item]

    def __contains__(self, item):
        return item in self._dict

    def __setitem__(self, key, value: Cookie):
        if key in self._dict:
            i = self.find_first_index(lambda c: c.key == value.key)
            self.pop(i)
        self._dict[key] = value
        self.append(value)

    def to_simple_cookie(self) -> http.cookies.SimpleCookie:
        simple_cookie = http.cookies.SimpleCookie()
        for cookie_name in self._dict:
            cookie = self._dict[cookie_name]
            simple_cookie[cookie_name] = self._dict[cookie_name].value
            if cookie.expires:
                simple_cookie[cookie_name]["expires"] = cookie.expires.strftime(HttpDate.date_format)
            if cookie.path:
                simple_cookie[cookie_name]["path"] = cookie.path
            if cookie.comment:
                simple_cookie[cookie_name]["comment"] = cookie.comment
            if cookie.domain:
                simple_cookie[cookie_name]["domain"] = cookie.domain
            if cookie.max_age:
                simple_cookie[cookie_name]["max-age"] = cookie.max_age
            if cookie.secure:
                simple_cookie[cookie_name]["secure"] = cookie.secure
            if cookie.http_only:
                simple_cookie[cookie_name]["httponly"] = cookie.http_only
            if cookie.version:
                simple_cookie[cookie_name]["version"] = cookie.version
            if cookie.same_site:
                simple_cookie[cookie_name]["samesite"] = cookie.same_site
        return simple_cookie


class Parameters(JsonObject):
    def __init__(self, querystring=""):
        from urllib.parse import unquote
        self._dict = {}
        query_string_parts = querystring.split("&")
        for qp in query_string_parts:
            if "=" not in qp:
                continue
            param = qp.split("=")
            self[param[0]] = unquote(param[1])
        JsonObject.__init__(self)


class HttpMessage(JsonObject):
    def __init__(self,
                 headers: Headers = None,
                 cookies: Cookies = None,
                 body=None):
        if headers is None:
            headers = Headers()
        if cookies is None:
            cookies = Cookies()
        self.headers = headers
        self.cookies = cookies
        self.body = bytes()
        if body:
            if not isinstance(body, bytes):
                body = bytes(str(body), "utf-8")

            self.set_body(body)
        JsonObject.__init__(self)

    def set_body(self, body):
        if isinstance(body, bytes):
            self.body = body
        else:
            self.body = bytes(str(body), 'utf-8')


class HttpRequest(HttpMessage):
    def __init__(self, handler=None):
        if handler:
            import http
            headers = Headers(handler.headers)
            cookies = None
            if "Cookie" in handler.headers:
                cookies = Cookies(http.cookies.SimpleCookie(headers["Cookie"]))

            body = bytes()
            if 'Content-Length' in headers:
                content_len = int(headers['Content-Length'])
                body = handler.rfile.read(content_len)

            HttpMessage.__init__(self,
                                 headers=headers,
                                 cookies=cookies,
                                 body=body)

            import urllib.parse
            parsed_url = urllib.parse.urlparse(handler.path)
            path_parts = parsed_url.path.split("/")[1:]
            self.file_name = ""
            if path_parts:
                if path_parts[-1] == "":
                    path_parts = path_parts[:-1]
                if path_parts and "." in path_parts[-1]:
                    self.file_name = path_parts[-1]
                    path_parts = path_parts[:-1]
                self.path = JsonList(list_type=str,
                                     iterable=path_parts)
            else:
                self.path = JsonList(list_type=str)
            self.parameters = Parameters(parsed_url.query)
            self.method = handler.command
        else:
            HttpMessage.__init__(self)
            self.path = JsonList(list_type=str)
            self.parameters = Parameters()
            self.method = ""
            self.file_name = ""

    def get_body_as(self, t: type):
        body = self.body.decode("utf-8")
        if issubclass(t, (JsonObject, JsonList)):
            if t is JsonObject or t is JsonList:
                return JsonObject.parse(body)
            else:
                return t.load(body)
        return t(body)


class HttpResponse(HttpMessage):
    def __init__(self,
                 code: int = 200,
                 headers: Headers = None,
                 cookies: Cookies = None,
                 body=None,
                 content_type: str = "",
                 content: Content = ""):

        if content:
            body = content.content
            content_type = content.content_type

        HttpMessage.__init__(self,
                             headers=headers,
                             cookies=cookies,
                             body=body)
        self.code = code
        self.content_type = content_type

    def write(self, value):

        if isinstance(value, bytes):
            self.body += value
        else:
            self.body += bytes(str(value), encoding='utf-8')

