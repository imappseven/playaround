class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counts = {}
        if len(arr) == 1:
            return True
        else:
            for e in arr:
                if e in counts:
                    counts[e] += 1
                else:
                    counts[e] = 1
            
        my_set = set(list(counts.values()))
        if len(my_set) == len(list(counts.values())):
            return True
        else:
            return False

                