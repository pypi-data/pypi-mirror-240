from .container import MagicContainer


def MagicRoute(cls=None, route=""):
    if cls:
        class NewRoute(cls, MagicContainer):
            _route = route
            pass

        return NewRoute
    else:
        def new_route(cls):
            class NewRoute(cls, MagicContainer):
                _route = route
                pass
            return NewRoute
        return new_route

