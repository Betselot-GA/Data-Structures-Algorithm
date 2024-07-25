class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        incr = 0
        maxi = max(arr)
        idx = arr.index(maxi)
        left = 0
        right = idx
        if idx == 0 or idx == len(arr)-1:
            return False

        while left < idx-1:
            if arr[left] >= arr[left+1]:
                return False
            left += 1
        while right < len(arr)-1:
            if arr[right] <= arr[right+1]:
                return False
            right += 1
        
        return True