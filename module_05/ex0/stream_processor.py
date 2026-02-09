from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if self.validate(data):
            if not isinstance(data, (tuple, list)):
                count = 1
                total = data
                avg = data
            else:
                count = len(data)
                total = sum(data)
                avg = total / count
            result = (f"Processed {count} numeric values, "
                      f"sum={total}, avg = {avg}")
            return result
        return "Invalid numeric entry"

    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, (int, float)):
                return True
            if len(data) <= 0:
                return False
            numeric = 0
            for num in data:
                numeric += num
            return True
        except Exception:
            return False


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if self.validate(data):
            count = len(data)
            total_word = len(data.split())
            result = f"Processed text: {count} characters, {total_word} words"
            return result
        return "Invalid text entry"

    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, str):
                return True
        except Exception:
            return False


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if self.validate(data):
            level = data.strip().split(':')[0]
            content = data.strip().split(':')[1]
            if level == "ERROR":
                prefix = "[ALERT]"
            else:
                prefix = f"[{level}]"
            result = f"{prefix} {level} level detected:{content}"
            return result
        return "Invalid log entry"

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                return False
            level = data.strip().split(':')[0]
            if level in ["ERROR", "DEBUG", "WARN", "INFO"]:
                return True
            return False
        except Exception:
            return False


proc = [NumericProcessor(), TextProcessor(), LogProcessor()]
data = [[1, 2, 3, 4, 5], "Hello Nexus World", "ERROR: Connection timeout"]
data1 = [[1, 2, 3], "hello world!", "INFO: System ready"]
print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
print("Initializing Numeric Processor...")
print(f"Processing data: {data[0]}")
if proc[0].validate(data[0]):
    print("Validation: Numeric data verified")
else:
    print("Validation: failed")
result = proc[0].process(data[0])
print(f"{proc[0].format_output(result)}")
print("\nInitializing Text Processor...")
print(f'Processing data: "{data[1]}"')
if proc[1].validate(data[1]):
    print("Validation: Text data verified")
else:
    print("Validation: failed")
result = proc[1].process(data[1])
print(f"{proc[1].format_output(result)}")
print("\nInitializing Log Processor...")
print(f'Processing data: "{data[2]}"')
if proc[2].validate(data[2]):
    print("Validation: Log entry verified")
else:
    print("Validation: failed")
result = proc[2].process(data[2])
print(f"{proc[2].format_output(result)}")

print("\n=== Polymorphic Processing Demo ===")
print("Processing multiple data types through same interface...")
for i in range(len(proc)):
    print(f"Result {i + 1}: {proc[i].process(data1[i])}")
print("\nFoundation systems online. Nexus ready for advanced streams.")
