class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_ref, sorted_data = zip(*sorted(zip(position, speed),reverse=True))
        position = list(sorted_ref)
        speed = list(sorted_data)
        stack = []

        for i,p in enumerate(position):
            stack.append((p,speed[i],i))

            if len(stack)>=2:
                t_1 = (target - stack[-1][0]) / stack[-1][1]
                t_2 = (target - stack[-2][0]) / stack[-2][1]
                if t_1 <= t_2:
                    stack.pop()

        return len(stack)

# solution with the help of the video => time:o(nlogn) because of the sorting but the loop is o(n) and space o(n)
