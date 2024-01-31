class Solution:
    def myAtoi(self, s: str) -> int:
        # new_s = s.strip()

        # if new_s == '' or new_s[0].isalpha():
        #     return 0

        # result = "".join([char for char in new_s if char.isdigit()])

        # if new_s[new_s.index(result[0])-1] == '-':
        #     result = '-' + result

        if not s:
            return 0
        
        i = 0
        while i < len(s) and s[i].isspace():
            i += 1
        
        sign = 1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        result *= sign
        
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        
        return result


x = Solution()
to_print = x.myAtoi("   -134")
to_print_2 = x.myAtoi(" ada 349 anak domba")
to_print_3 = x.myAtoi("words and 987")
to_print_4 = x.myAtoi("3.5424")
print(to_print)
print(to_print_2)
print(to_print_3)
print(to_print_4)
