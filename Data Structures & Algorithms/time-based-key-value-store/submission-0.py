class TimeMap:

    def __init__(self):
        self.dct={}
        self.timestamps=[]
        self.values=[]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dct.keys():
            self.dct[key]["v"].append(value)
            self.dct[key]["t"].append(timestamp)
        else:
             self.dct[key] = {"v": [value], "t": [timestamp]}
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dct.keys():
            return ""
        else:
            tmp=self.dct[key]["t"]
            if tmp[0]>timestamp:
                return ""
            lo,hi=0,len(tmp)-1
            while lo<=hi:
                mid=(lo+hi)//2
                if tmp[mid]==timestamp:
                    return self.dct[key]["v"][mid]
                elif tmp[mid]>timestamp:
                    hi=mid-1
                else:
                    lo=mid+1
            if hi>=0 and tmp[hi]<timestamp:
                return self.dct[key]["v"][hi]
            else:
                return ""
                
            
            
        
