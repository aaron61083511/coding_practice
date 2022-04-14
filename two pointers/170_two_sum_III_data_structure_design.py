class TwoSum:
# # two pointers:
#     def __init__(self):
#         self.num = []


#     def add(self, number: int) -> None:
#         self.num.append(number)



#     def find(self, value: int) -> bool:
#         self.num.sort()
#         left, right = 0, len(self.num)-1
#         while left < right:
#             two_sum = self.num[left] + self.num[right]
#             if two_sum == value:
#                 return True
#             elif two_sum > value:
#                 right -= 1
#             else:
#                 left += 1
#         return False

# hash map
    def __init__(self):
        self.nums = {}
    def add(self, number: int) -> None:
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1
    def find(self, value: int) -> bool:
        for i in self.nums.keys():
            if i != value - i:
                if value - i in self.nums:
                    return True
            elif self.nums[i] > 1:
                return True
        return False
