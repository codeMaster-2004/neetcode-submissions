class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        if len(intervals) < 1:
            return []
        ret = [intervals[0]]

        for i in range(1, len(intervals)):
            i1 = ret[-1]
            i2 = intervals[i]

            if i2[0] <= i1[1]:
                ret[-1][1] = max(i1[1], i2[1])
                continue
            ret.append(i2)

        return ret