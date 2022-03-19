# Плюсом данной реализации можно отметить константное время вставки и удаления в начале и конце буфера.
# Простота для понимания кода кода
# Меньше занимает памяти, так как не испльзуем указатели, в отличает от второй реализации.

class CircularBuffer_v1:
    def __init__(self, size):
        self.data = [None for i in range(size)]

    def append(self, x):
        self.data.pop(0)
        self.data.append(x)

    def get(self):
        return self.data


class CircularBuffer_v2:
    def __init__(self, size_max):
        self.max = size_max
        self.data = []

    class Full:
        def append(self, x):
            self.data[self.cur] = x
            self.cur = (self.cur + 1) % self.max

        def get(self):
            return self.data[self.cur:] + self.data[:self.cur]

    def append(self, x):
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            self.__class__ = self.Full

    def get(self):
        return self.data
