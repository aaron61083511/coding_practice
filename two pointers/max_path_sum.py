# Given a 2D array of integers in the following format,
# find the maximum sum attainable by following a path that originates at the root and ends at the base,
# where you may only travel DOWN or DOWN+RIGHT
# 1
# 2 -3
#
# 3 -2
# 4 5 6
#
# 7 9 10
# 7 8 9 8
#
# 14 17 19 18
#
# nums = [
# [1],
# [2, 3],
# [4, 5, 6],
# [7, 8,9,8]]

j = 1

n = len(nums)
while j < n:
	for i in range(len(nums[j])):
		if i != 0:
			nums[j][i] += max(nums[j-1][i], nums[j-1][i-1])
		elif i == len(nums[j])-1:
			nums[j][i] += nums[j-1][i-1]
		else:
			nums[j][i] += nums[j-1][i]

return max(nums[j-1])


