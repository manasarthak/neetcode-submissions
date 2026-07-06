class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_lo,row_hi=0,len(matrix)-1
        targ=0
        while row_lo<=row_hi:
            mid=(row_lo+row_hi)//2
            if matrix[mid][0] == target or matrix[mid][-1] ==target:
                return True
            elif matrix[mid][-1]<target:
                row_lo=mid+1
            elif matrix[mid][0]<target:
                targ=mid
                break
            else:
                row_hi=mid-1
        col_lo,col_hi=0,len(matrix[0])-1
        while col_lo<=col_hi:
            mid=(col_lo+col_hi)//2
            if matrix[targ][mid]==target:
                return True
            elif matrix[targ][mid]<target:
                col_lo=mid+1
            else:
                col_hi=mid-1
        return False
        