from .resource import resource_file_path
from .error_responses import HttpMethodNotSupportedResponse, HttpFileNotFoundResponse, HttpListNotAllowedResponse
from .container import MagicContainer
from .http import HttpRequest, HttpResponse, HttpMethod
from .content import Content, HttpContentTypes
from json_cpp import JsonList, JsonObject
from .dynamic_content import DynamicContent


def get_file_content(file_path: str) -> HttpResponse:
    extension = "." + file_path.split(".")[-1]
    content = Content(content_type=HttpContentTypes[extension])
    with open(file_path) as f:
        content.content = f.read()
        f.close()
    return HttpResponse(content=content)


def load_file_list(folder_path: str):
    import os
    file_list = JsonList(list_type=JsonObject)
    for file in os.listdir(folder_path):
        file_list.append(JsonObject(name=file))
    return file_list


class MagicFileContainer(MagicContainer):

    def __init__(self, path: str, recursive: bool = False, allow_listing: bool = False, response_format: str = "html"):
        self._path = path
        self._recursive = recursive
        self._allow_listing = allow_listing
        self._response_format = response_format
        MagicContainer.__init__(self)

    def __route__(self, request: HttpRequest, path: list = None) -> HttpResponse:
        if path is None:
            path = list()

        if request.path:
            route = request.path[0]
            if route in self._routes:
                request.path = request.path[1:]
                path.append(route)
                return self._routes[route].__route__(request=request, path=path)

        if request.path and not self._recursive:
            return HttpFileNotFoundResponse(file_name=request.file_name)

        if request.method == HttpMethod.Get:
            if request.file_name == "":
                if self._allow_listing:
                    response_format = self._response_format
                    if "format" in request.parameters:
                        response_format = request.parameters.format
                    if response_format not in ["html", "json"]:
                        response_format = "html"
                    if response_format == "json":
                        file_list = load_file_list(self._path)
                        return HttpResponse(content=Content(content_type=HttpContentTypes[".json"],
                                                            content=file_list))
                    else:
                        return get_file_content(file_path=resource_file_path("html", "browse.html"))
                else:
                    return HttpListNotAllowedResponse()
            else:
                file_path = "/".join([self._path] + request.path + [request.file_name])
                import os
                if os.path.isfile(file_path):
                    if DynamicContent.is_dynamic(file_path):
                        return DynamicContent.get_dynamic_content(file_path)(request)
                    else:
                        return get_file_content(file_path=file_path)
                else:
                    return HttpFileNotFoundResponse(file_name=request.file_name)
        else:
            return HttpMethodNotSupportedResponse(request.method)


def MagicFolder(container=None,
                path: str = ".",
                recursive: bool = False,
                allow_listing: bool = False,
                response_format: str = "html"):
    if container:
        class NewMagicFolder(MagicFileContainer, container):
            def __init__(self):
                MagicFileContainer.__init__(self,
                                            path=path,
                                            recursive=recursive,
                                            allow_listing=allow_listing,
                                            response_format=response_format)

        return NewMagicFolder
    else:
        class NewMagicFolder(MagicFileContainer):
            def __init__(self):
                MagicFileContainer.__init__(self,
                                            path=path,
                                            recursive=recursive,
                                            allow_listing=allow_listing,
                                            response_format=response_format)

        return NewMagicFolder
