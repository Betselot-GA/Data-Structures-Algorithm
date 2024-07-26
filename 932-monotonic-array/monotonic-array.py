class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = 0
        dec = 0
        mini = min(nums)
        lst_idx = len(nums)-1
        idx = nums.index(mini)
        if not ((mini == nums[0]) or (mini == nums[lst_idx])):
            return False
        elif idx == 0:
            while inc < len(nums)-1:
                if nums[inc] > nums[inc+1]:
                    return False
                inc += 1
        else:
            while dec < len(nums)-1:
                if nums[dec] < nums[dec+1]:
                    return False
                dec += 1
        return True