# # Check all_combo_dict
# from collections import defaultdict
# wordList = ["hot","dot","dog","lot","log","cog"]
# all_combo_dict = defaultdict(list)
# for word in wordList:
#     for i in range(3):
#         all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
# print(all_combo_dict)


from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                 all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        visited = {beginWord: True}
        queue = [(beginWord, 1)]
        while queue:
            current, level = queue.pop(0)
            for i in range(len(beginWord)):
                intermediate = current[:i] + "*" + current[i+1:]
                for word in all_combo_dict[intermediate]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level+1))
                all_combo_dict[intermediate] = []
        return 0
