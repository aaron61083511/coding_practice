# 沿用sort color方法
def sortColors(nums, k):
    count = 0
    start = 0
    end = len(nums) - 1
    while count < k:
        min_value = float('inf')
        max_value = float('-inf')
        for i in range(start, end):
            min_value = min(min_value, nums[i])
            max_value = max(max_value, nums[i])
        left = start
        right = end
        current = left
        while current <= right:
            if nums[current] == min:
                nums[left], nums[current] = nums[current], nums[left]
                current += 1
                left += 1
            elif nums[current] == max_value:
                nums[right], nums[current] = nums[current], nums[right]
                right -= 1
            else:
                current += 1
        count += 2
        start = left
        end = right

# 可以借用merge sort的折中分段 + quick sort的partition方法
def sortColors2(colors, left, right, colorFrom, colorTo):
    if colorFrom == colorTo:
        return None
    if left >= right:
        return None
    colorMid = (colorFrom + colorTo)//2
    l, r = left, right
    while l <= r:
        while l <= r and colors[l] <= colorMid:
            l += 1
        while l <= r and colors[r] > colorMid:
            r -= 1
        if l <= r:
            colors[l], colors[r] = colors[r], colors[l]

    sortColors2(colors, left, r, colorFrom, colorMid)
    sortColors2(colors, l, right, colorMid+1, colorTo)
