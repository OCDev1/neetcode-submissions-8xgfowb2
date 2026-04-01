class TimeMap:

    def __init__(self):
        self.my_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.my_map:
            # add (val, time) to list of values for this key
            self.my_map[key].append([value,timestamp])
            return
        else:
            # init the the new key entry
            self.my_map[key] = []
            self.my_map[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_map:
            return ""
        else:
            val_list = self.my_map[key]
            # binary search for the timestamp:
            l,r = 0,len(val_list)-1
            while l<=r:
                m = (l+r) // 2
                if val_list[m][1] == timestamp:
                    return val_list[m][0]
                elif val_list[m][1] < timestamp:
                    l = m+1
                else:
                    r = m-1
            
            # val_list[r] is the closest number to timestamp from the right (m-1)
            return val_list[r][0] if r >= 0 else ""


