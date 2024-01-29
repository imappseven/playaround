class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x > 0:
            reversed_x = int(str(x)[::-1])
            if reversed_x > 2**31 - 1:
                return 0
            return reversed_x
        if x < 0:
            reversed_x = int('-'+str(x)[1:][::-1])
            if reversed_x < -2**31:
                return 0
            return reversed_x
        

x = Solution()
res1 = x.reverse(435)
res2 = x.reverse(-467)
res3 = x.reverse(3900)
res4 = x.reverse(1534236469)
print(res1,res2,res3,res4)
