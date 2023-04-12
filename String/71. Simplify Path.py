class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        
        path = path.split('/')
        for s in path:
            if ans and s == '..':
                ans.pop()
            if s not in ['', '.', '..']:
                ans.append(s)


        return "/" + "/".join(ans)
