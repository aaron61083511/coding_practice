# test
def xx(arr):
    visited = set()
    min_value = float('inf')
    for i in arr:
        if i > 0:
            visited.add(i)
            min_value = min(i, min_value)
    res = min_value
    if not visited:
        return 1
    for j in visited:
        if res in visited:
            res += 1
        else:
            return res
    return res
# print(xx([1,3,6,4,1,2]))
print(xx([1,2,3]))

# 1
s = 'John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brain Parker'
c = 'Example'
def xx(s, c):
    visited = {}
    list_s = s.split('; ')
    res = ''
    for i in list_s:
        first = i.split(' ')[0].lower()
        last = i.split(' ')[-1].lower().replace('-', '')
        if len(last) > 8:
            last = last[:8]
        name = first+'.'+last
        if name not in visited:
            visited[name] = visited.get(name, 0) + 1
            res += name + '@' + c.lower() + '.com; '
        else:
            visited[name] += 1
            res += name + str(visited[name]) + '@' + c.lower() + '.com; '
    return res[:-2]
print(xx(s, c))

# 2 (leetcode 1904)
def xx(startTime, finishTime):
    ts = 60 * int(startTime[:2]) + int(startTime[-2:])
    tf = 60 * int(finishTime[:2]) + int(finishTime[-2:])
    if 0 <= tf - ts < 15: return 0 # edge case 
    # tf//15 -> convert finish time to the same / earlier 15 min count, we are effectively getting the floor.
    # (ts+14)//15 -> convert start time to the same / later 15 min count, we are effectively getting the ceiling.
    # (ts>tf)*96 -> if start time is later than finish time, add 4 quarters per hour * 24 hours = 96 counts, otherwise add 0.
    # +14 is to calculate each quarter in an hour. (0+14)//15 -> 0, but (1 + 14 )//15 -> 1, (15+14)//15 -> 1. So we are effectively rounding up. 4 * 24 is for 4 quarters per hour and 24 hours per day. Also edited the annotation.
    return tf//15 - (ts+14)//15 + (ts>tf)*96