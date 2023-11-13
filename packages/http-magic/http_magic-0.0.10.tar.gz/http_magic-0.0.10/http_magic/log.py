from enum import Enum


class LogType(Enum):
    Event = 0
    Warning = 1
    Error = 2
    Critical = 3


class LoggingLevel(Enum):
    Event = 0
    Warning = 1
    Error = 2
    Critical = 3


class Log:

    level = LoggingLevel.Event
    file_path = "application_log.log"
    function = None
    date_format = "%Y-%m-%d %H:%M:%S"
    entry_format = "{entry_time} - {entry_type}: {entry_text}"

    def __init__(self, entry_text, log_type: LogType = LogType.Event):
        if log_type.value >= self.level.value:
            from datetime import datetime
            formatted_entry = self.entry_format.format(entry_type=log_type.name,
                                                       entry_text=entry_text,
                                                       entry_time=datetime.now().strftime(self.date_format))
            if not Log.function:
                Log.set_logging(Log.st_output_logging)
            Log.function(formatted_entry, log_type)

    @staticmethod
    def file_logging(formatted_entry, log_type: LogType):
        with open(Log.file_path, "w") as f:
            f.write(formatted_entry + "\n")

    @staticmethod
    def st_output_logging(formatted_entry, log_type: LogType):
        if log_type.value >= LogType.Error.value:
            import sys
            print(formatted_entry, file=sys.stderr)
        else:
            print(formatted_entry)

    @staticmethod
    def set_log_file(file_path: str):
        Log.log_file_path = file_path

    @staticmethod
    def set_logging(logging_function):
        Log.function = logging_function
