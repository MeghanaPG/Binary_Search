from sortedcontainers import SortedDict 

class TimeMap:

    def __init__(self):
        self.key_time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #If the key doesn't exist in the dictionary, then we will create a new key 
        if not key in self.key_time_map:
            self.key_time_map[key] = SortedDict()
        
        #Will store key as (timestamp, value) pair in 'key' bucket
        self.key_time_map[key][timestamp] = value 

    def get(self, key: str, timestamp: int) -> str:
        # If the key is not present, then we will return empty string 
        if not key in self.key_time_map:
            return ""
        
        myIter = self.key_time_map[key].bisect_right(timestamp)
        # If myIter points to first element it means, no time <= timestamp exits
        if myIter == 0:
            return ""
        
        return self.key_time_map[key].peekitem(myIter-1)[1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)