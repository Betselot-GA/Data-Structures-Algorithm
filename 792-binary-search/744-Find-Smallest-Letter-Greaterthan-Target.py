class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        greater = []
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                greater.append(letters[mid])
                right = mid - 1
            elif letters[mid] <= target:
                left = mid + 1
           
        
        if len(greater) > 0:
            return min(greater)
        else:
            return letters[0]