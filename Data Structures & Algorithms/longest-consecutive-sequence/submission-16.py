class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        i = 0
        m = 0
        for n in nums:

            while n + i in s:
                i += 1
            m = max(m,i)
            i = 0
            while n - i in s:
                i += 1
            i = 0
        return m
           

# solved with this method with the help of the video