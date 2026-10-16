class TimeMap:

    def __init__(self):
        self.timemap = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap: 
            self.timemap[key] = []
        self.timemap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap: 
            return "" 
        
        entries = self.timemap[key]
        l = 0
        r = len(entries) - 1
        res = "" 
        
        while l <= r: 
            m = (l + r) // 2
            if entries[m][0] <= timestamp: 
                res = entries[m][1]
                l = m + 1 
            else: 
                r = m - 1 
        return res

        
