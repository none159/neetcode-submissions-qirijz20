class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            letters = [0]*26
            for l in s:
                l_index = ord(l) - ord('a')
                letters[l_index] += 1
            anagrams[tuple(letters)].append(s)
            
        return list(anagrams.values())
            

# o(m*n) time , o(m) extra space and o(m*n) space for the output list complexity solution with a help