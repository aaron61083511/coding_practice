class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.count = 0
        self.sum_window = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        if self.count > self.size:
            drop = self.queue.popleft()
        else:
            drop = 0
        self.sum_window = self.sum_window - drop + val
        return sum(self.queue)/min(self.count, self.size)
