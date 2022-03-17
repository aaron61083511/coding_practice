# # Reverse word in a string
# # s = "the sky    is blue"
# s = 's,dfs,df'
# a = s.split(',')[::-1]
# b = ','.join(a)
# print(b)
#
# def reverse(s):
#     s_list = s.split()
#     s_reverse = s_list[::-1]
#     output = " ".join(s_reverse)
#     return output

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
di = dict.fromkeys(keys, values)
print(di)
di = dict(zip(keys, values))
print(di)
print(di.get('Ten'))

# # Given a string s, find the length of the longest substring without repeating characters.
#
# a = ['a', 'b', 'a', 'c']
# b = list(set(a))
# c = list(dict.fromkeys(a))
# print(b)
# print(c)

aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList.count(4))

# resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
# print(resList)
#
# aList = [5, 10, 15, 25]
# print(aList[::-2])

