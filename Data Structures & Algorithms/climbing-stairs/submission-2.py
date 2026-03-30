class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        next = 1
        count = 1
        while count < n:
            
            a = b
            b = next 
            next = a+b

            count +=1
        return next