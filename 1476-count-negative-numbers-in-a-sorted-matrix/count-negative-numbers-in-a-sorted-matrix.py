class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ngt = 0
        for row in grid:
            left = 0
            right = len(row)-1
            while left <= right:
                if row[left] < 0 :
                    ngt += len(row[left:])
                    break
                left +=1
        return ngt