from abc import ABC, abstractmethod
from typing import Any
from typing import Protocol


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.values: dict[int, str] = {}
        self.rank = 0

    def output(self) -> tuple[int, str]:
        try:
            first_key = next(iter(self.values))
        except StopIteration:
            print(f"No more values {self}")
            return (0, "")
        return (first_key, self.values.pop(first_key))

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass


class NumericProcessor(DataProcessor):

    def __str__(self) -> str:
        return "Numeric Processor"

    def validate(self, data: Any) -> bool:
        lst = self.get_list(data)
        if lst is None:
            return False
        for nb in lst:
            if type(nb) is not int and type(nb) is not float:
                return False
        return True

    def ingest(self, data: int | float | list[int] | list[float]) -> None:
        if self.validate(data) is False:
            print("Got exception: Improper numeric data")
            return
        lst = self.get_list(data)
        if lst is None:
            return
        for nb in lst:
            self.values.update({self.rank: str(nb)})
            self.rank += 1

    @staticmethod
    def get_list(data: Any) -> list[int] | list[float] | None:
        if type(data) is list:
            return data
        if type(data) is int or type(data) is float:
            return list({data})
        return None


class TextProcessor(DataProcessor):

    def __str__(self) -> str:
        return "Text Processor"

    def validate(self, data: Any) -> bool:
        lst = self.get_list(data)
        if lst is None:
            return False
        for item in lst:
            if type(item) is not str:
                return False
        return True

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data) is False:
            print("Got exception: Improper string data")
            return
        lst = self.get_list(data)
        if type(lst) is list:
            for string in lst:
                self.values.update({self.rank: string})
                self.rank += 1

    @staticmethod
    def get_list(data: Any) -> list[str] | None:
        if type(data) is list:
            return data
        if type(data) is str:
            lst = []
            lst.append(data)
            return lst
        return None


class LogProcessor(DataProcessor):

    def __str__(self) -> str:
        return "Log Processor"

    def validate(self, data: Any) -> bool:
        lst = self.get_list(data)
        if lst is None:
            return False
        for item in lst:
            if type(item) is not dict:
                return False
            if len(item) != 2:
                return False
            for key, value in item.items():
                if type(key) is not str or type(value) is not str:
                    return False
        return True

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data) is False:
            print("Got exception: Improper dict data")
            return
        lst = self.get_list(data)
        if lst is None:
            return
        for item in lst:
            logs = self.get_logs(item)
            self.values.update({self.rank: logs})
            self.rank += 1

    @staticmethod
    def get_logs(item: dict[str, str]) -> str:
        logs = []
        for key, value in item.items():
            logs.append(value)
            result = ": ".join(logs)
        return result

    @staticmethod
    def get_list(data: Any) -> list[dict[str, str]] | None:
        if type(data) is list:
            return data
        if type(data) is dict:
            lst = []
            lst.append(data)
            return lst
        return None


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class ExportCSV(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        for item in data:
            print(f"{item[1]}, ", end="")


class ExportJSON(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataStream():

    def __init__(self):
        self.procs = []

    def register_processor(self, proc: DataProcessor) -> None:
        if isinstance(proc, DataProcessor):
            print(f"Registering {proc}")
            self.procs.append(proc)
        else:
            print(f"{proc} couldn't be registered")

    def process_stream(self, stream: list[Any]) -> None:
        valid = 0
        procs = self.procs
        for data in stream:
            for proc in procs:
                if proc.validate(data):
                    proc.ingest(data)
                    valid = 1
            if valid == 0:
                print(
                      "DataStream error - "
                      f"Can't process element in stream: {data}"
                     )

    def print_processors_stats(self) -> None:
        procs = self.procs
        print("== DataStream statistics ==")
        if len(procs) == 0:
            print("No processor found, no data")
            return
        for proc in procs:
            print(
                  f"{proc}: total {proc.rank} items processed,"
                  f" remaining {len(proc.values.items())} on processor"
                 )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        procs = self.procs
        data = []
        for proc in procs:
            for _ in range(nb):
                data.append(proc.output())
            if plugin == ExportCSV:
                print("CSV Output:")
            elif plugin == ExportJSON:
                print("JSON Output:")
            plugin.process_output(data)
            print()


def try_input(class_name: DataProcessor, data: Any) -> str:
    return f"Trying to validate input '{data}': {class_name.validate(data)}"


def extract_inputs(class_name: DataProcessor, numbers: int) -> None:
    if type(class_name) is NumericProcessor:
        text = "Numeric value"
    if type(class_name) is TextProcessor:
        text = "Text value"
    if type(class_name) is LogProcessor:
        text = "Log entry"
    for number in range(numbers):
        output = class_name.output()
        if output[1] == "":
            break
        print(f"{text} {output[0]}: {output[1]}")


def main() -> None:
    stream = DataStream()
    num_proc = NumericProcessor()
    txt_proc = TextProcessor()
    log_proc = LogProcessor()
    csv = ExportCSV()
    json = ExportJSON()
    first_batch = [
        'Hello world', [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message':
          'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message':
          'User wil is connected'}], 42, ['Hi', 'five']]
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    stream.print_processors_stats()
    print()
    stream.register_processor(num_proc)
    stream.register_processor(txt_proc)
    stream.register_processor(log_proc)
    print()
    print(f"Send first batch of data on stream: {first_batch}")
    stream.process_stream(first_batch)
    print()
    stream.print_processors_stats()
    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, csv)
    stream.print_processors_stats()
    print()
    second_batch = [
            21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
            [{'log_level': 'ERROR', 'log_message': '500 server crash'},
             {'log_level': 'NOTICE', 'log_message':
             'Certificate expires in 10 days'}],
            [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"Send another batch of data: {second_batch}\n")
    stream.process_stream(second_batch)
    stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, json)
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
