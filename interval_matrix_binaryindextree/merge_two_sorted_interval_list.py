# Merge two sorted (ascending) lists of
# interval and return it as a new sorted list.
# The new sorted list should be made by splicing together
# the intervals of the two lists and sorted in ascending order.

# The intervals in the given list do not overlap.
# The intervals in different lists may overlap.

# e.g.
# Given list1 =[(1,2),(3,4)]and list2 =[(2,3),(5,6)], return[(1,4),(5,6)].

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1

        index1, index2 = 0, 0
        ans = []

        #now代表list1和list2中将要加入ans的区间

        while index1 < len(list1) and index2 < len(list2):
            a = list1[index1]
            b = list2[index2]

            #如果a左端点较小，说明a将被加入ans中，
            #所以令now = a，同时将i加一以便后面继续加入
            #如果b左端点较小，也类似操作

            if a.start <= b.start:
                now = a
                index1 += 1
            else:
                now = b
                index2 += 1

            #如果ans为空，那就直接将区间加进去
            #否则将ans末尾的区间与now进行合并

            if not ans:
                ans.append(now)
            else:
                self.merge(ans, ans[len(ans) - 1], now)

        #如果list1已经全被加进去了，则将list2的区间一个一个merge进ans中

        while index2 < len(list2):
            self.merge(ans, ans[len(ans) - 1], list2[index2])
            index2 += 1
        #同上
        while index1 < len(list1):
            self.merge(ans, ans[len(ans) - 1], list1[index1])
            index1 +=1
        return ans

    #merge函数将ans末尾的区间与now合并后加入ans

    def merge(self, ans, last, now):
        #如果last与now不相交，那直接将now加进ans即可
    	#否则直接拓展last的右端点
        if last.end < now.start:
            ans.append(now)
        else:
            last.end = max(last.end, now.end)

