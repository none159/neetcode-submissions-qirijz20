class Solution:
    def is_pal(self,i,j,s):
        while i<j:
            if s[i] != s[j]:
                return False
            j -= 1
            i+=1
        return True
    def f(self,i,j,s):
        out = []
        if i == len(s) or j == len(s):
            return []
        if self.is_pal(i,j,s):
            out.append(s[i:j+1])
            self.f(i,j+1,s)
        else:
            j = i
            self.f(i+1,j,s)

        return out
    def partition(self, s: str) -> List[List[str]]:
        out = []
        res = []
        def f(i):
            if i >= len(s):
                res.append(out.copy())
                return
            j = i
            while j <len(s):
                if self.is_pal(i,j,s):
                    out.append(s[i:j+1])
                    f(j+1)
                    out.pop()
                j += 1
 
        f(0)
        return res

