from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._values: dict[int, str] = {}
        self._rank = 0

    def output(self) -> tuple[int, str]:
        try:
            first_key = next(iter(self._values))
        except StopIteration:
            print("No more values")
            return (0, "")
        return (first_key, self._values.pop(first_key))

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass


class NumericProcessor(DataProcessor):

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
            self._values.update({self._rank: str(nb)})
            self._rank += 1

    @staticmethod
    def get_list(data: Any) -> list[int] | list[float] | None:
        if type(data) is list:
            return data
        if type(data) is int or type(data) is float:
            return list({data})
        return None


class TextProcessor(DataProcessor):

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
                self._values.update({self._rank: string})
                self._rank += 1

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
            self._values.update({self._rank: logs})
            self._rank += 1

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
    num_proc = NumericProcessor()
    txt_proc = TextProcessor()
    log_proc = LogProcessor()
    test_values_list = [1, 2, 3, 4, 5]
    test_words_list = ['Hello', 'Nexus', 'World']
    test_dict_list = [
         {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
         {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print("=== Code nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    print(try_input(num_proc, 42))
    print(try_input(num_proc, 'Hello'))
    print("Test invalid ingestion of string 'foo' without prior validation:")
    num_proc.ingest('foo')
    print(f"Processing data: {test_values_list}")
    num_proc.ingest(test_values_list)
    print("Extracting 3 values...")
    extract_inputs(num_proc, 3)
    print("\nTesting Text Processor...")
    print(try_input(txt_proc, 42))
    print(f"Processing data: {test_words_list}")
    txt_proc.ingest(test_words_list)
    extract_inputs(txt_proc, 1)
    print("\nTesting Log Processor...")
    print(try_input(log_proc, 'Hello'))
    print(f"Processing data: {test_dict_list}")
    log_proc.ingest(test_dict_list)
    extract_inputs(log_proc, 2)


if __name__ == "__main__":
    main()
