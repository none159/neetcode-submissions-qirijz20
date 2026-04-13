
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        arr = []
        for key,value in freq.items():
            arr.append([value,key])
        arr.sort()
        freq = []
        while arr and len(freq) < k:
            freq.append(arr.pop()[1])
        
        return freq

# Optimized solution using help 