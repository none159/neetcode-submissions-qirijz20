class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        m = 0
        r = len(heights) - 1
        while l < r:
            m = max(m,min(heights[l],heights[r])* (len(heights[l:r+1]) - 1))
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
            
        return m
# optimized solution complexity => time: o(n) and space:o(1)