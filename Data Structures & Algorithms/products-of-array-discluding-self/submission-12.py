class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        i = 0
        prefix = 1
        while i < len(nums):
            result[i] *= prefix
            prefix *= nums[i]
            i+=1
        prefix = 1
        i-=1
        while i >= 0:
            result[i] *= prefix
            prefix *= nums[i]
            i-=1
        return result