class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        
        char_index = {}  # Dictionary to store the index of each character in the current substring
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1  # Move the start pointer to the next index of the repeating character

            char_index[char] = end  # Update the index of the current character
            current_length = end - start + 1  # Calculate the length of the current substring

            max_length = max(max_length, current_length)

        return max_length

w = Solution()
result = w.lengthOfLongestSubstring('abcabcbb')
print(result)
