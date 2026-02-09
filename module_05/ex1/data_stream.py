from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self, name: str, stream_id: str, stream_type: str) -> None:
        self.name = name
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        return "NO Data"

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {'count_read': self.processed_count}

    def display(self) -> str:
        return (f"\nInitializing {self.name} Stream..."
                f"\nStream ID: {self.stream_id}, Type: {self.stream_type}")


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        name = "Sensor"
        stream_types = "Environmental Data"
        super().__init__(name, stream_id, stream_types)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            total_read = 0
            av_temp = 0
            sum_temp = 0
            for item in data_batch:
                content, result = item.split(':')
                result = float(result)
                if content == "temp":
                    sum_temp += result
                    av_temp += 1
                total_read += 1
            self.processed_count = total_read
            if av_temp == 0:
                avg = ""
            else:
                average = sum_temp / av_temp
                avg = f", avg temp: {average}°C"

            return f"{total_read} readings processed{avg}"
        except Exception as e:
            return f"Error processing sensor batch: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {'count_read': f"{self.processed_count} readings processed"}

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            if not criteria:
                return data_batch
            filter_result = []
            for data in data_batch:
                content, value = data.split(':')
                value = float(value)
                if content == "temp" and value >= 30:
                    filter_result.append(data)
            return filter_result
        except Exception as e:
            print(f"Error filtering sensor batch : {e}")
            return []


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        name = "Transaction"
        stream_types = "Financial Data"
        super().__init__(name, stream_id, stream_types)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            amount = 0
            total_read = 0
            for item in data_batch:
                content, value = item.split(':')
                value = int(value)
                if content == "buy":
                    amount += value
                elif content == "sell":
                    amount -= value
                total_read += 1
            self.processed_count = total_read
            if amount == 0:
                net_flow = ""
            else:
                net_flow = f", net flow: +{amount} units"
            return f"{total_read} operations{net_flow}"
        except Exception as e:
            return f"Error processing Transaction batch: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {'count_read': f"{self.processed_count} operations processed"}

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:

        try:
            large = []
            for data in data_batch:
                content, value = data.split(':')
                value = int(value)
                if criteria is None:
                    if value >= 100:
                        large.append(data)
                else:
                    if content == criteria and value >= 100:
                        large.append(data)
            return large
        except Exception as e:
            print(f"Error filtering transaction batch: {e}")
            return []


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        name = "Event"
        stream_types = "System Events"
        super().__init__(name, stream_id, stream_types)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            total_read = 0
            total_error = 0
            for item in data_batch:
                content = item.lower()
                if content == "error":
                    total_error += 1
                total_read += 1
            self.processed_count = total_read
            if total_error == 0:
                decte = ""
            else:
                decte = f", {total_error} error detected"
            return f"{total_read} events{decte}"
        except Exception as e:
            return f"Error processing event batch: {e}"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {'count_read': f"{self.processed_count} events processed"}


class StreamProcessor:

    def __init__(self, streams: List[DataStream]) -> None:
        self.streams = streams
        print("Processing mixed stream types through unified interface...\n")

    def all_stream_processing(self, data_batch: dict[str, list[Any]]) -> None:
        print("Batch 1 Results:")
        try:
            for stream in self.streams:
                batch = data_batch.get(stream.stream_id)
                stream.process_batch(batch)
                print(
                    f"- {stream.name} data: {stream.get_stats()['count_read']}"
                )
        except Exception as e:
            print(f"Error processing: {e}")

    def all_stream_filtering(self, data_batch: List[Any]) -> str:
        try:
            sensor_count = len(self.streams[0].filter_data(
                data_batch.get(self.streams[0].stream_id), "temp"))
            transaction_count = len(self.streams[1].filter_data(
                data_batch.get(self.streams[1].stream_id), "sell"))

            print("\nStream filtering active: High-priority data only")
            print(f"Filtered results: {sensor_count} critical sensor alerts, "
                  f"{transaction_count} large transaction")
        except Exception as e:
            print(f"Error filtering: {e}")


print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

"""Sensor"""
sensor = SensorStream("SENSOR_001")
data_batch = [["temp:22.5", "humidity:65", "pressure:1013"],
              ["buy:100", "sell:150", "buy:75"], ["login", "error", "logout"]]
event_batch = data_batch[0]
if not isinstance(event_batch, list):
    event_batch = []
process = ", ".join(str(x) for x in event_batch)
print(sensor.display())
print(f"Processing sensor batch: [{process}]")
print(f"Sensor analysis: {sensor.process_batch(data_batch[0])}")

""" Transaction"""
trans = TransactionStream("TRANS_001")
event_batch = data_batch[1]
if not isinstance(event_batch, list):
    event_batch = []
process1 = ", ".join(str(x) for x in event_batch)
print(trans.display())
print(f"Processing transaction batch: [{process1}]")
print(f"Transaction analysis: {trans.process_batch(data_batch[1])}")

""" Event """
event = EventStream("EVENT_001")
event_batch = data_batch[2]
if not isinstance(event_batch, list):
    event_batch = []
process2 = ", ".join(str(x) for x in event_batch)
print(event.display())
print(f"Processing event batch: [{process2}]")
print(f"Event analysis: {event.process_batch(data_batch[2])}")

""" mixed stream """
print("\n=== Polymorphic Stream Processing ===")
sensor1 = SensorStream("SENSOR_002")
transaction1 = TransactionStream("TRANS_002")
event1 = EventStream("EVENT_002")
streams = [sensor1, transaction1, event1]
data_batch1 = {
    "SENSOR_002": ["temp:50.5", "temp:45.2"],
    "TRANS_002": ["buy:100", "sell:150", "buy:10", "sell:25"],
    "EVENT_002": ["login", "error", "large"]
}
results = StreamProcessor(streams)
results.all_stream_processing(data_batch1)
results.all_stream_filtering(data_batch1)
print("\nAll streams processed successfully. Nexus throughput optimal.")
