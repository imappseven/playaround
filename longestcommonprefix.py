from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        common_prefix = strs[0]

        for word in strs[1:]:
            for i, char in enumerate(common_prefix):
                if i < len(word) and char == word[i]:
                    continue
                else:
                    common_prefix = common_prefix[:i]
                    break

        return common_prefix

# example
x = Solution()
result = x.longestCommonPrefix(["permutation", "persist", "periscope", "percentage"])
print(result)
