class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
"""
this version of solution is made with help !!!

we push at the end and pop first element then get the next first element 
(we take the parent here 
for the heapq data structure because it is third largest element 
and we used heapq.heapify to make parents less than child elements 
and left just 3 elements in the list)
"""
