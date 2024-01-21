def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        else:
            prev = 1 
            curr = 1

            #for _ in range(2, n + 1):
            #fib_prev, fib_current = fib_current, fib_prev + fib_current
            for _ in range(1, n):
                x = prev
                prev = curr
                curr = x + curr
            return curr

y = climbStairs(8)
print(y)