class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for idx in range(len(startTime)):
            if startTime[idx] < queryTime and endTime[idx] > queryTime:
                count +=1
            elif startTime[idx] == queryTime or endTime[idx] == queryTime:
                count +=1
        return count