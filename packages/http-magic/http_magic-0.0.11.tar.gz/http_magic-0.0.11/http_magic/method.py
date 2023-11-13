from .http import HttpRequest, HttpResponse, HttpMethod
from .input_source import InputSource
from .output_type import OutputType
from .content import HttpContentTypes, Content
from .error_responses import HttpInternalServerErrorResponse
from .error_handling import handle_error, CustomError


class WrongOutputType(CustomError):
    def __init__(self, request: HttpRequest):
        CustomError.__init__(self, "Wrong output produced for request '%s'." % (str(request)))


def input_source_wrapper(funct, input_source: InputSource):
    if input_source == InputSource.Request:
        def wrapped_method(self, request: HttpRequest):
            return funct(self, request)
    elif input_source == InputSource.Body:
        def wrapped_method(self, request: HttpRequest):
            return funct(self, request.body)
    elif input_source == InputSource.ParsedBody:
        from json_cpp import JsonObject

        def wrapped_method(self, request: HttpRequest):
            return funct(self, JsonObject.parse(request.body))
    elif input_source == InputSource.CastedParsedBody:
        from json_cpp import JsonObject

        def wrapped_method(self, request: HttpRequest):
            str_body = request.body.decode("utf-8")
            dict_body = JsonObject.parse(str_body).to_dict()
            return funct(self, **dict_body)
    elif input_source == InputSource.Parameters:
        def wrapped_method(self, request: HttpRequest):
            return funct(self, request.parameters)
    elif input_source == InputSource.CastedParsedParameters:
        def wrapped_method(self, request: HttpRequest):
            return funct(self, **request.parameters.to_dict())
    elif input_source == InputSource.FileName:
        def wrapped_method(self, request: HttpRequest):
            return funct(self, request.parameters)
    else:  # Input.Empty
        def wrapped_method(self, request: HttpRequest):
            return funct(self)
    return wrapped_method


def output_type_wrapper(funct, output_type: OutputType):
    if output_type == OutputType.Json:
        from json_cpp import JsonObject

        def wrapped_method(self, request: HttpRequest) -> HttpResponse:
            try:
                result = funct(self, request)
            except Exception as e:
                handle_error(e)
                return HttpInternalServerErrorResponse()
            if isinstance(result, JsonObject):
                return HttpResponse(body=result, content_type=HttpContentTypes[".json"])
            else:
                raise WrongOutputType(request)
    elif output_type == OutputType.Response:
        def wrapped_method(self, request: HttpRequest) -> HttpResponse:
            try:
                result = funct(self, request)
            except Exception as e:
                handle_error(e)
                return HttpInternalServerErrorResponse()
            if isinstance(result, HttpResponse):
                return result
            else:
                raise WrongOutputType(request)
    elif output_type == OutputType.Content:
        def wrapped_method(self, request: HttpRequest) -> HttpResponse:
            try:
                result = funct(self, request)
            except Exception as e:
                handle_error(e)
                return HttpInternalServerErrorResponse()
            if isinstance(result, Content):
                return HttpResponse(content=result)
            else:
                raise WrongOutputType(request)
    else:  # OutputType.Empty:
        def wrapped_method(self, request: HttpRequest) -> HttpResponse:
            try:
                funct(self, request)
            except Exception as e:
                handle_error(e)
                return HttpInternalServerErrorResponse()
            return HttpResponse()
    return wrapped_method


def MagicMethod(funct, http_method, input_source, output_type):
    input_wrapped_method = input_source_wrapper(funct, input_source=input_source)
    magic_method = output_type_wrapper(input_wrapped_method, output_type=output_type)
    magic_method._http_method = http_method
    return magic_method


def MagicGet(funct=None, input_source=InputSource.Parameters, output_type=OutputType.Json):
    if funct:
        return MagicMethod(funct=funct, http_method=HttpMethod.Get, input_source=input_source, output_type=output_type)
    else:
        def new_magic_get(funct):
            return MagicMethod(funct=funct, http_method=HttpMethod.Get, input_source=input_source, output_type=output_type)
        return new_magic_get


def MagicPut(funct=None, input_source=InputSource.CastedParsedBody, output_type=OutputType.Empty):
    if funct:
        return MagicMethod(funct=funct, http_method=HttpMethod.Put, input_source=input_source, output_type=output_type)
    else:
        def new_magic_put(funct):
            return MagicMethod(funct=funct, http_method=HttpMethod.Put, input_source=input_source, output_type=output_type)
        return new_magic_put


def MagicPost(funct=None, input_source=InputSource.CastedParsedBody, output_type=OutputType.Empty):
    if funct:
        return MagicMethod(funct=funct, http_method=HttpMethod.Post, input_source=input_source, output_type=output_type)
    else:
        def new_magic_post(funct):
            return MagicMethod(funct=funct, http_method=HttpMethod.Post, input_source=input_source, output_type=output_type)
        return new_magic_post


def MagicDelete(funct=None, input_source=InputSource.CastedParsedParameters, output_type=OutputType.Empty):
    if funct:
        return MagicMethod(funct=funct, http_method=HttpMethod.Delete, input_source=input_source, output_type=output_type)
    else:
        def new_magic_delete(funct):
            return MagicMethod(funct=funct, http_method=HttpMethod.Delete, input_source=input_source, output_type=output_type)
        return new_magic_delete


def MagicHead(funct=None, input_source=InputSource.Parameters, output_type=OutputType.Empty):
    if funct:
        return MagicMethod(funct=funct, http_method=HttpMethod.Head, input_source=input_source, output_type=output_type)
    else:
        def new_magic_head(funct):
            return MagicMethod(funct=funct, http_method=HttpMethod.Head, input_source=input_source, output_type=output_type)
        return new_magic_head


def MagicPatch(funct=None, input_source=InputSource.Parameters, output_type=OutputType.Empty):
    if funct:
        return MagicMethod(funct=funct, http_method=HttpMethod.Patch, input_source=input_source, output_type=output_type)
    else:
        def new_magic_patch(funct):
            return MagicMethod(funct=funct, http_method=HttpMethod.Patch, input_source=input_source, output_type=output_type)
        return new_magic_patch


def MagicConnection(funct=None, input_source=InputSource.Parameters, output_type=OutputType.Empty):
    if funct:
        return MagicMethod(funct=funct, http_method=HttpMethod.Connection, input_source=input_source, output_type=output_type)
    else:
        def new_magic_connection(funct):
            return MagicMethod(funct=funct, http_method=HttpMethod.Connection, input_source=input_source, output_type=output_type)
        return new_magic_connection


def MagicOptions(funct=None, input_source=InputSource.Empty, output_type=OutputType.Empty):
    if funct:
        return MagicMethod(funct=funct, http_method=HttpMethod.Options, input_source=input_source, output_type=output_type)
    else:
        def new_magic_options(funct):
            return MagicMethod(funct=funct, http_method=HttpMethod.Options, input_source=input_source, output_type=output_type)
        return new_magic_options
