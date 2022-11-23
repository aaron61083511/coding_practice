class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        graph = defaultdict(list)
        for i in regions:
            graph[i[0]]=i[1:]
        root = regions[0][0]
        ans = []
                
        def dfs(root, region1, region2):
            curr = [0,0]
            if root == region1 or root == region2:
                curr= [1,0] if root == region1 else [0,1]
                
            for nei in graph[root]:
                ret = dfs(nei, region1, region2)
                curr = [curr[0] or ret[0], curr[1] or ret[1]]
                if all(curr):
                    ans.append(root)
                    return [0,0]
            return curr
        
        dfs(root, region1, region2)
        return ans[0]

    def findSmallestRegion_alternative(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parents = {region[i] : region[0] for region in regions for i in range(1, len(region))}
        ancestry_history = {region1}
        while region1 in parents:
            region1 = parents[region1]
            ancestry_history.add(region1)
        while region2 not in ancestry_history:
            region2 = parents[region2]
        return region2