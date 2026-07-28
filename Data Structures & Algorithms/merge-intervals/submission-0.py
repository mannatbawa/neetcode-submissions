class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        answer = []
        current = intervals[0]

        for interval in intervals[1:]:
            if current[1] >= interval[0]:
                current[1] = max(current[1], interval[1])
            else:
                answer.append(current)
                current = interval

        answer.append(current)
        return answer
        