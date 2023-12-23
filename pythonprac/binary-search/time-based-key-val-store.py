#https://leetcode.com/problems/time-based-key-value-store/


class TimeMap:

    def __init__(self):
        #actually just use a dict
        self.store={} #key=string, value=[listof [val,timestamp]]
        # self.keys=[]
        # self.timeval=[] #for each key, there will be a dict? or array
                        #should store timestamp as first value.
        #actually cant do this because u have to check if new key is in keys
        #making it n^2. nvm
        #well i knew that before watching soln. u have to put timestamp first value, and 
        #values are given as increasing, meaning already sorted.just dont know what structure to use.
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append([value,timestamp])
        
        

    def get(self, key: str, timestamp: int) -> str:
        res=""
        values=self.store.get(key,  []) 
        #will get the value in store with key "key". if not, return [].
        #binarysearch:
        l,r=0,len(values)-1

        while l<=r:
            m=(l+r)//2
            if values[m][1]<=timestamp:
                res=values[m][0] #this is what i forgot earlier, set the "closest so far"
                l=m+1  #this code doesnt have a case that returns if already hit exact timestamp.
            else:
                r=m-1

                #return values[m][0]


        return res

        