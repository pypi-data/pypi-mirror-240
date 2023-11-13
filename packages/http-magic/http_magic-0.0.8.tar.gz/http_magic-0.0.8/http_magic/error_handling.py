from .log import Log, LogType


def handle_error(exc_obj: Exception, data: str = ""):
    import traceback
    tb_str = ''.join(traceback.format_exception(None, exc_obj, exc_obj.__traceback__))
    if data:
        Log(tb_str + "\n" + data, LogType.Error)
    else:
        Log(tb_str, LogType.Error)


class CustomError(RuntimeError):
    def __init__(self, desc):
        RuntimeError.__init__(self, desc)
        handle_error(self, "Description: " + desc)
