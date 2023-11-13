from json_cpp import JsonObject


class MagicUser(JsonObject):

    def __init__(self, name: str, data: JsonObject):
        self.name = name
        self.data = data
        JsonObject.__init__(self)


class MagicUserProfile(JsonObject):

    def __init__(self):
        JsonObject.__init__(self)
