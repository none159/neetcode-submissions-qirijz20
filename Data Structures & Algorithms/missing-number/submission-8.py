class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i ^ sorted(nums)[i] != 0:
                return i
        return len(nums)

# bitwise attempt with hint 3
