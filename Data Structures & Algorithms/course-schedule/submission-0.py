class Solution:
    import collections
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = collections.defaultdict(list)
        output = []
        for dep,pre in prerequisites:
            d[dep].append(pre)
        visited,cycles = set(),set()
        def dfs(dep):
            if dep in cycles:
                return False
            if dep in visited:
                return True
            cycles.add(dep)
            for pre in d[dep]:
                if dfs(pre) == False:
                    return False
            cycles.remove(dep)
            visited.add(dep)
            output.append(dep)
            return True
        for i in range(numCourses):
            if(dfs(i) == False):
                return False
        return True