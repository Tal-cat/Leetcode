class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # START
        parent = [i for i in range(n)]

        def ufind(x):
            if parent[x] != x:
                parent[x] = ufind(parent[x])
            return parent[x]

        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)

            parent[ua] = parent[ub]

        for u, v in edges:
            uunion(u, v)
        
        counts = collections.Counter()
        for i in range(n):
            counts[ufind(i)] += 1

        total = 0
        for k in counts.keys():
            total += counts[k] * (n - (counts[k]))

        return total//2
