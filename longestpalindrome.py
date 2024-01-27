class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            # Check for palindromes with odd length
            len1 = self.expand_around_center(s, i, i)
            # Check for palindromes with even length
            len2 = self.expand_around_center(s, i, i + 1)
            # Get the maximum length palindrome centered at index i
            max_len = max(len1, len2)
            # Update start and end pointers if the current palindrome is longer
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the length of the palindrome found
        return right - left - 1

# Example 
w = Solution()
result = w.longestPalindrome("babad")
print(result) 

x = Solution()
result_2 = x.longestPalindrome("chawwadsome")
print(result_2)
