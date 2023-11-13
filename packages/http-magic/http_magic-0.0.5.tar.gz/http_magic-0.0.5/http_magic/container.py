from .http import HttpRequest, HttpResponse
from .error_responses import HttpRouteNotFoundResponse
from .log import Log
from .error_handling import CustomError


class EmptyRouteError(CustomError):
    def __init__(self, parent_route: str):
        CustomError.__init__(self, "Empty child route found on route '%s'." % parent_route)


class DuplicatedRouteError(CustomError):
    def __init__(self, parent_route: str, route: str):
        CustomError.__init__(self, "Duplicate route '%s' on route '%s'." % (route, parent_route))


class DuplicatedRouteMethodError(CustomError):
    def __init__(self, route: str, http_method: str):
        CustomError.__init__(self, "Duplicate method '%s' on route '%s'." % (http_method, route))


class MagicContainer:
    _route = ""

    def __init__(self):
        self._routes = dict()
        self._methods = dict()
        for candidate_name in dir(self):
            if candidate_name[0] == "_":
                continue
            candidate = getattr(self, candidate_name)
            if isinstance(candidate, type) and issubclass(candidate, MagicContainer):
                if candidate_name in self._methods:
                    raise DuplicatedRouteError(candidate_name)
                if not candidate._route:
                    raise EmptyRouteError(self._route)
                self._routes[candidate._route] = candidate()
            elif hasattr(candidate, "_http_method"):
                http_method = candidate._http_method
                if http_method in self._methods:
                    raise DuplicatedRouteMethodError(self._route, http_method)
                self._methods[http_method] = candidate

    def __route__(self, request: HttpRequest, path: list = None) -> HttpResponse:
        Log("Routing %s" % "/".join(request.path))
        if path is None:
            path = list()
        if request.path:
            route = request.path[0]
            if route not in self._routes:
                return HttpRouteNotFoundResponse(route)
            request.path = request.path[1:]
            path.append(route)
            return self._routes[route].__route__(request=request, path=path)
        method = request.method
        if method in self._methods:
            return self._methods[method](request=request)
