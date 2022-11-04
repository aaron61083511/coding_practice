class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        graph = defaultdict(list)
        bank.append(startGene)
        for gene in bank:
            for i in range(len(gene)):
                graph[gene[:i]+'*'+gene[i+1:]].append(gene)
        level = 0
        
        queue = deque([startGene])
        visited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node not in visited:
                    visited.add(node)
                for i in range(len(node)):
                    current = node[:i] + '*' + node[i+1:]
                    for n in graph[current]:
                        if n == endGene:
                            return level + 1
                        if n not in visited:
                            visited.add(n)
                            queue.append(n)
            if queue:
                level += 1
        
        return -1
