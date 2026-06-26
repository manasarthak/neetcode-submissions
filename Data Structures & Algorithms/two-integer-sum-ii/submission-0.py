class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo,hi=0,len(numbers)-1
        while lo<hi:
            temp=numbers[lo]+numbers[hi]
            if temp ==target:
                return [lo+1,hi+1]
            elif temp<target:
                lo+=1
            else:
                hi-=1
        return "dummy"

        