class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Zip them, sort them, and unpack them
        sorted_a, sorted_b = zip(*sorted(zip(position, speed)))

        # 2. Convert back to lists (zip unpacking returns tuples)
        position = list(sorted_a)[::-1]
        speed = list(sorted_b)[::-1]
        time=[0]*len(position)
        for i in range(len(position)):
            time[i]=(target-position[i])/speed[i]
        
        ans=1
        fleet_time=time[0]
        for i in range(1,len(time)):
            if time[i]<=fleet_time:
                continue
            else:
                ans+=1
                fleet_time=time[i]
        return ans



        

                
        

        