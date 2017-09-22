class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if timeSeries == []:
            return 0
        res = 0
        diff = [timeSeries[i + 1] - timeSeries[i] for i in range(len(timeSeries) - 1)]
        for k in diff:
            if k >= duration:
                res += duration
            else:
                res += k
        res += duration
        return res
