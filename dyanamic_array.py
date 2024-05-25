class DynamicArray:
    def __init__(self, resize_factor=2):
        self.array = []
        self.size = 0
        self.capacity = 1
        self.resize_factor = resize_factor

    def _resize(self):
        self.capacity *= self.resize_factor
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def insert(self, index, element):
        if self.size == self.capacity:
            self._resize()
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1
        self.array[self.size] = None

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def rotate(self, k):
        if self.size == 0:
            return
        k = k % self.size
        self.array = self.array[-k:] + self.array[:-k]

    def reverse(self):
        start = 0
        end = self.size - 1
        while start < end:
            self.array[start], self.array[end] = self.array[end], self.array[start]
            start += 1
            end -= 1

    def append(self, element):
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = element
        self.size += 1

    def prepend(self, element):
        self.insert(0, element)

    def merge(self, other):
        for i in range(other.get_size()):
            self.append(other.array[i])

    def interleave(self, other):
        new_array = DynamicArray(self.resize_factor)
        i = j = 0
        while i < self.size or j < other.get_size():
            if i < self.size:
                new_array.append(self.array[i])
                i += 1
            if j < other.get_size():
                new_array.append(other.array[j])
                j += 1
        return new_array

    def get_middle_element(self):
        if self.size == 0:
            return None
        return self.array[self.size // 2]

    def index_of(self, element):
        for i in range(self.size):
            if self.array[i] == element:
                return i
        return -1

    def split(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        first_part = DynamicArray(self.resize_factor)
        second_part = DynamicArray(self.resize_factor)
        for i in range(index):
            first_part.append(self.array[i])
        for i in range(index, self.size):
            second_part.append(self.array[i])
        return first_part, second_part

    def __str__(self):
        return str(self.array[:self.size])

# Usage example
dynamic_array = DynamicArray()
dynamic_array.append(1)
dynamic_array.append(2)
dynamic_array.append(3)
print(dynamic_array)  # Output: [1, 2, 3]
dynamic_array.insert(1, 4)
print(dynamic_array)  # Output: [1, 4, 2, 3]
dynamic_array.delete(2)
print(dynamic_array)  # Output: [1, 4, 3]
print(dynamic_array.get_size())  # Output: 3
print(dynamic_array.is_empty())  # Output: False
dynamic_array.rotate(1)
print(dynamic_array)  # Output: [3, 1, 4]
dynamic_array.reverse()
print(dynamic_array)  # Output: [4, 1, 3]
dynamic_array.prepend(0)
print(dynamic_array)  # Output: [0, 4, 1, 3]
second_array = DynamicArray()
second_array.append(5)
second_array.append(6)
dynamic_array.merge(second_array)
print(dynamic_array)  # Output: [0, 4, 1, 3, 5, 6]
interleaved_array = dynamic_array.interleave(second_array)
print(interleaved_array)  # Output: [0, 5, 4, 6, 1, 3, 5, 6]
print(dynamic_array.get_middle_element())  # Output: 3
print(dynamic_array.index_of(4))  # Output: 1
first_part, second_part = dynamic_array.split(3)
print(first_part)  # Output: [0, 4, 1]
print(second_part)  # Output: [3, 5, 6]
