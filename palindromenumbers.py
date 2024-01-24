class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        # if len(y) % 2 == 0:
        #     for i in range(int(len(y)/2)):
        #         if y[i] == y[-(i+1)]:
        #             return True
        # else:
        #     for i in range(int((len(y)-1)/2)):
        #         if y[i] == y[-(i+1)]:
        #             return True
        # return False
        return y == y[::-1]