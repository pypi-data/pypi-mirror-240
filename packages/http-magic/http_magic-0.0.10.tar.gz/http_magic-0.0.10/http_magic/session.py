from datetime import timedelta
from .http import HttpRequest, HttpResponse, Cookie
from json_cpp import JsonObject, JsonParseBehavior
from .error_handling import CustomError

class MagicSession(JsonObject):
    def __init__(self, session_key: str = ""):
        self.session_key = session_key
        JsonObject.__init__(self)

    def key(self):
        return self.session_key


class MagicSessionManager:
    key_field_name = "session_key"
    duration = 30

    def __init__(self, save_session=None, load_session=None):
        if save_session:
            self.save_session = save_session
        if load_session:
            self.load_session = load_session

    def get_session_key(self, request: HttpRequest) -> str:
        if request.cookies and self.key_field_name in request.cookies:
            key = request.cookies[self.key_field_name].value
        else:
            import uuid
            key = "S_" + (str(uuid.uuid4()) + str(uuid.uuid4())).replace("-", "")
        return key

    def set_session_key(self, response: HttpResponse, key: str):
        from datetime import datetime, timezone
        response.cookies[self.key_field_name] = Cookie(key=self.key_field_name,
                                                       value=key,
                                                       expires=datetime.now(timezone.utc) + timedelta(minutes=self.duration))

    def get_session(self, request: HttpRequest) -> MagicSession:
        raise NotImplemented("load_session is not implemented")

    def save_session(self, response: HttpResponse, session: MagicSession):
        raise NotImplemented("save_session is not implemented")


class MagicMemorySessionManager(MagicSessionManager):
    key_field_name = "mem_session_key"

    def __init__(self):
        self.sessions_data = JsonObject()
        MagicSessionManager.__init__(self)

    def get_session(self, request: HttpRequest) -> MagicSession:
        key = self.get_session_key(request)
        if hasattr(self.sessions_data, key):
            session = getattr(self.sessions_data, key)
        else:
            session = MagicSession(session_key=key)

        return session

    def save_session(self, response: HttpResponse, session: MagicSession):
        setattr(self.sessions_data, session.key(), session)
        self.set_session_key(response=response, key=session.key())


class MagicFileSessionManager(MagicSessionManager):
    session_key_cookie_name = "file_session_key"

    def __init__(self, path: str = "", duration: int = 30):
        import os
        import tempfile

        self.using_temp = False
        if not path:
            path = tempfile.mkdtemp()
            self.using_temp = True

        if os.path.exists(path):
            if not os.path.isdir(path):
                raise CustomError("path %s is not a folder")
        else:
            raise CustomError("path %s cannot be found")
        self.path = path
        self.duration = duration
        MagicSessionManager.__init__(self)

    def get_session(self, request: HttpRequest) -> MagicSession:
        key = self.get_session_key(request)
        import os
        session_file = self.path + "/" + key
        if os.path.exists(session_file):
            session = JsonObject.load_from_file(session_file).into(MagicSession,
                                                                   behavior=JsonParseBehavior.IncorporateNewAttributes)
        else:
            session = MagicSession(session_key=key)

        return session

    def save_session(self, response: HttpResponse, session: MagicSession):
        session_file = self.path + "/" + session.key()
        session.save(session_file)
        self.set_session_key(response=response, key=session.key())

    def __del__(self):
        if self.using_temp:
            import os
            os.rmdir(self.path)
