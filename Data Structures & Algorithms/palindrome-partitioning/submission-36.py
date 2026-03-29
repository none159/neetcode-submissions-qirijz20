class Solution:
    def is_pal(self,i,j,s):
        while i < j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        output = []
        res = []
        def dfs(i):
            if i >= len(s):
                if output != []:
                    res.append(output.copy())
                return 
            j = i
            while j < len(s):
                if self.is_pal(i,j,s):
                    output.append(s[i:j+1])
                    dfs(j+1)
                    output.pop()
                j+=1
 
        
        dfs(0)
        return res