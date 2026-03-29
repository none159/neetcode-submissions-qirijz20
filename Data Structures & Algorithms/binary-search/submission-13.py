class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1
        while True:
            middle = (low + high) // 2
            if nums[middle] == target:
                return middle
            if nums[low:high] == []:
                break
            elif nums[middle] > target:
                high = middle - 1
            else:
                low = middle + 1
            
        return -1

        
