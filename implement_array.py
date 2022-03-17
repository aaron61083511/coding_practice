class array(object):
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def get_index(self, item):
        index = list(self.data.values()).index(item)
        return index

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return last_item

    def shiftItems(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1

    def delete(self, index):
        item = self.data[index]
        self.shiftItems(index)
        return item

    def reverse(self):
        reversed_data = {}
        for i in range(self.length):
            reversed_data[i] = self.data[self.length-1-i]
        return reversed_data

    def insert(self, item, index):
        for i in range(index, self.length):
            temp = self.data[i]
            self.data[i] = item
            item = temp
        self.data[self.length] = item

x = array()
x.push('Hey')
x.push(18)
x.push('sdf')
x.push(12)
# x.push(12)
# x.push(12)
# print(x.data)
# print(x.get(1))
# print(x.pop())
print(x.data, x.length)
# print(x.delete(1))
# print(x.get_index(12))
x.insert(1111, 1)
print(x.data, x.length)
# print(x.reverse())


# reversed_data = {}
# for i in range(x.length):
#     reversed_data[i] = x.data[4]
# print(reversed_data)
