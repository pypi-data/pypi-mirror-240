from .http import HttpRequest, HttpResponse
from .content import HttpContentTypes
from enum import Enum
from .error_handling import handle_error, CustomError


class MagicDynamicContentPartType(Enum):
    Static = 0
    Dynamic = 1


class MagicDynamicContentPart:
    def __init__(self, part_type, content):
        self.part_type = part_type
        self.content = content


class DynamicContent:
    cache = {}

    def __init__(self, file_path: str, content_type: str = ""):
        content_parts = DynamicContent.read_dynamic_content_parts(file_path=file_path)
        self.content_parts = content_parts
        if content_type:
            self.content_type = content_type
        else:
            fp = file_path.split(".")
            if fp and fp[-1][:4] == "pdc_":
                if content_type == "":
                    extension = "." + fp[-1][4:]
                    self.content_type = HttpContentTypes[extension]
                else:
                    self.content_type = content_type
            else:
                raise CustomError("Unexpected file extension '%s', dynamic pages extension must start with 'pdc_'" % fp[-1])

        # caches the content for future executions
        DynamicContent.cache[file_path] = self

    @staticmethod
    def read_dynamic_content_parts(file_path: str) -> list:
        with open(file_path, "r") as f:
            file_content = f.read()
        parts = []
        starter = "<%"
        ender = "%>"
        sections = file_content.split(starter)
        parts.append(MagicDynamicContentPart(MagicDynamicContentPartType.Static, sections[0]))
        for section in sections[1:]:
            sp_sec = section.split(ender)
            if len(sp_sec) < 2:
                raise RuntimeError("Unterminated python sequence found in %s" % file_path)
            # compiles the python part to expedite execution
            parts.append(MagicDynamicContentPart(MagicDynamicContentPartType.Dynamic, compile(sp_sec[0], '', 'exec')))
            parts.append(MagicDynamicContentPart(MagicDynamicContentPartType.Static, sp_sec[1]))
        return parts

    @staticmethod
    def get_dynamic_content(file_path: str) -> "DynamicContent":
        if file_path not in DynamicContent.cache:
            return DynamicContent(file_path=file_path)
        return DynamicContent.cache[file_path]

    def __call__(self, request: HttpRequest) -> HttpResponse:
        response = HttpResponse(content_type=self.content_type)
        context = {"request": request, "response": response}
        for part in self.content_parts:
            if part.part_type == MagicDynamicContentPartType.Static:
                response.write(part.content)
            elif part.part_type == MagicDynamicContentPartType.Dynamic:
                try:
                    exec(part.content, context)
                except Exception as e:
                    handle_error(e, "Error processing:\n%s", part.content)
        return response

    @staticmethod
    def is_dynamic(file_path: str) -> bool:
        return file_path.split(".")[-1][:4] == "pdc_"
