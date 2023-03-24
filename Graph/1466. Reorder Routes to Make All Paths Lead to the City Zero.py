class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # START
        self.result = 0
        roads = set()
        graph = collections.defaultdict(list)

        for u, v in connections:
            # add directed roads
            roads.add((u, v))
            # create undirectred graph for dfs
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u, parent):
            if (parent, u) in roads:
                self.result += 1
            
            # check adjacent nodes
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)
            
        dfs(0, -1)
        
        return self.result
