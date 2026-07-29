class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        if key in self.store:
            entries = self.store[key]
        else:
            return ""
        
        left = 0
        right = len(entries) - 1
        ans = ""
        while left <= right:
            middle = (left + right) // 2
            middle_timestamp = entries[middle][1]

            if middle_timestamp <= timestamp:
                ans = entries[middle][0]
                left = middle + 1

            else:
                right = middle - 1
        return ans
