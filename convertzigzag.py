class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        print(rows)
        index = 0
        step = 1

        for char in s:
            rows[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(rows)

# Example usage
contoh = Solution()
s = "PAYPALISHIRING"
numRows = 3
result = contoh.convert(s, numRows)
print(result)
