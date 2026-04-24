class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        stack = []
        print(pair)
        for p,s in sorted(pair,reverse=True):
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        
        return len(stack)

# solution with the help of the video => time:o(nlogn) because of the sorting but the loop is o(n) and space: o(n)