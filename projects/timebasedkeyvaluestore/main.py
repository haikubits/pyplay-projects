import bisect
from typing import defaultdict, List

class TimeBasedKVStore:
    
    def __init__(self):
        self.store = defaultdict(list)
    
    def set(self, key, value, timestamp) -> None:
        self.store[key].append((timestamp, value))
    
    def get(self, key, ts):
        if key not in self.store:
            return ""
        key_history = self.store[key]
        max_timestamp_idx = bisect.bisect_right(key_history, ts, key = lambda x: x[0]) - 1
        if max_timestamp_idx >= 0:
            return key_history[max_timestamp_idx][1]
        return ""

myKVStore = TimeBasedKVStore()
myKVStore.set("hello", 22, 10)
myKVStore.set("hello", 18, 11)
myKVStore.set("hello", 27, 12)
myKVStore.set("hello", 31, 15)
myKVStore.set("hello", 25, 21)
myKVStore.set("hello", 10, 72)

print("Key: ", "hello1", "ts: ", 10, "Result: ", myKVStore.get("hello1", 10))
print("Key: ", "hello", "ts: ", 9, "Result: ", myKVStore.get("hello", 9))
print("Key: ", "hello", "ts: ", 12, "Result: ", myKVStore.get("hello", 12))
print("Key: ", "hello", "ts: ", 50, "Result: ", myKVStore.get("hello", 50))
print("Key: ", "hello", "ts: ", 16, "Result: ", myKVStore.get("hello", 16))
print("Key: ", "hello", "ts: ", 100, "Result: ", myKVStore.get("hello", 100))