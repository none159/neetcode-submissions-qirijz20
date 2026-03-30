class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        m = 1
        count = 1
        while count < n:
            a,b = b,m
            m = a+b
            count +=1
        return m