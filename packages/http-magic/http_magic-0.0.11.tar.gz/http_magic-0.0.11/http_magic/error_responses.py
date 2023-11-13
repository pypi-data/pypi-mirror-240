from .http import HttpResponse
from .content import HttpContentTypes


class HttpMethodNotSupportedResponse(HttpResponse):
    def __init__(self, method: str):
        from json_cpp import JsonObject
        HttpResponse.__init__(self,
                              code=405,
                              body=str(JsonObject(code=405,
                                                  message="Method %s not supported" % method)),
                              content_type=HttpContentTypes[".json"])


class HttpInternalServerErrorResponse(HttpResponse):

    def __init__(self):
        from json_cpp import JsonObject
        HttpResponse.__init__(self,
                              code=500,
                              body=str(JsonObject(code=500,
                                                  message="Internal server error")),
                              content_type=HttpContentTypes[".json"])


class HttpFileNotFoundResponse(HttpResponse):
    def __init__(self, file_name: str):
        from json_cpp import JsonObject
        HttpResponse.__init__(self,
                              code=404,
                              body=JsonObject(code=404,
                                              message="File %s not found" % file_name),
                              content_type=HttpContentTypes[".json"])


class HttpListNotAllowedResponse(HttpResponse):
    def __init__(self):
        from json_cpp import JsonObject
        HttpResponse.__init__(self,
                              code=403,
                              body=JsonObject(code=403,
                                              message="Listing not allowed"),
                              content_type=HttpContentTypes[".json"])


class HttpRouteNotFoundResponse(HttpResponse):
    def __init__(self, file_name: str):
        from json_cpp import JsonObject
        HttpResponse.__init__(self,
                              code=404,
                              body=str(JsonObject(code=404,
                                                  message="Route %s not found" % file_name)),
                              content_type=HttpContentTypes[".json"])

