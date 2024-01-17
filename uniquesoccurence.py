class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counts = {}
        for e in arr:
            if e in counts:
                counts[e] += 1
            else:
                counts[e] = 1

        for val in counts.values():
            if list(counts.values()).count(val) > 1:
                return False
            else:
                return True