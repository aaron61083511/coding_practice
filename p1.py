items=[['A','B'],['A','C'],['B','D'],['B','C'],['R','M'], ['S'],['P'], ['A']]
result=dict()
print(result)
for item in items:
    if item[0] not in result.keys():
        result[item[0]]=len(item)-1
        print(item)
        print(len(item))
        print(result)
    elif item[0] in result.keys():
        result[item[0]]+=len(item)-1
        print(result)
print(result)
