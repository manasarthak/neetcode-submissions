class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target:
                return mid
            elif nums[lo]==target:
                return lo
            elif nums[hi]==target:
                return hi
            if nums[mid]<nums[hi]:
                if nums[mid]<target:
                    if nums[hi]<target:
                        hi=mid-1
                    else:
                        lo=mid+1
                else:
                    hi=mid-1
            elif nums[mid]>nums[hi]:
                if nums[mid]>target:
                    if nums[hi]<target:
                        hi=mid-1
                    else:
                        lo=mid+1
                else:
                    lo=mid+1
            else:
                break
        return -1

            
        
        