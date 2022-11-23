class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win, lose = [], []
        graph = {}

        for i in matches:
            graph[i[0]] = graph.get(i[0], [0,0])
            graph[i[0]][0] += 1
            graph[i[1]] = graph.get(i[1], [0,0])
            graph[i[1]][1] += 1
        
        for i in graph:
            if graph[i][1] == 0:
                win.append(i)
            if graph[i][1] == 1:
                lose.append(i)
        
        return [sorted(win), sorted(lose)]