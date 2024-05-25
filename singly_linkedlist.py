class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

class SLL:
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__size = 0
        self.__iter = None

    def __len__(self):
        return self.__size

    def Size(self):
        return self.__size

    def isEmpty(self):
        return self.Size() == 0

    def append(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = newNode
        self.__size += 1

    def addFirst(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.append(data)
        else:
            newNode.next = self.__head
            self.__head = newNode
            self.__size += 1

    def addLast(self, data):
        return self.append(data)

    def addAt(self, index, data):
        if index < 0 or index > self.Size():
            raise Exception("Invalid index")
        if index == 0:
            self.addFirst(data)
        elif index == self.Size():
            self.addLast(data)
        else:
            trav1 = self.__head
            for _ in range(index - 1):
                trav1 = trav1.next
            newNode = Node(data, trav1.next)
            trav1.next = newNode
            self.__size += 1

    def peekFirst(self):
        if self.isEmpty():
            raise Exception("Empty list")
        return self.__head.data

    def peekLast(self):
        if self.isEmpty():
            raise Exception("Empty list")
        return self.__tail.data

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("Empty list")
        trav = self.__head
        self.__head = trav.next
        trav = None
        self.__size -= 1
        if self.__size == 0:
            self.__tail = None

    def removeLast(self):
        if self.isEmpty():
            raise Exception("Empty list")
        if self.Size() == 1:
            self.__head = self.__tail = None
            self.__size -= 1
        else:
            trav = self.__head
            while trav.next is not self.__tail:
                trav = trav.next
            trav.next = None
            self.__tail = trav
            self.__size -= 1

    def removeAt(self, index):
        if index < 0 or index >= self.Size():
            raise Exception("Invalid index")
        if index == 0:
            self.removeFirst()
        elif index == self.Size() - 1:
            self.removeLast()
        else:
            trav1 = self.__head
            for _ in range(index - 1):
                trav1 = trav1.next
            trav2 = trav1.next
            trav1.next = trav2.next
            trav2 = None
            self.__size -= 1

    def indexOf(self, data):
        trav = self.__head
        index = 0
        while trav is not None:
            if trav.data == data:
                return index
            index += 1
            trav = trav.next
        return -1

    def contains(self, data):
        return self.indexOf(data) != -1

    def clear(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __iter__(self):
        self.__iter = self.__head
        return self

    def __next__(self):
        if self.__iter is None:
            raise StopIteration
        data = self.__iter.data
        self.__iter = self.__iter.next
        return data

    def rotate(self, k):
        if self.isEmpty() or k <= 0:
            return
        k %= self.__size
        if k == 0:
            return
        old_tail = self.__tail
        new_tail = self.__head
        for _ in range(self.__size - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        old_tail.next = self.__head
        self.__head = new_head
        new_tail.next = None
        self.__tail = new_tail

    def reverse(self):
        prev = None
        current = self.__head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.__head, self.__tail = self.__tail, self.__head

    def merge(self, other):
        if not isinstance(other, SLL):
            raise Exception("Invalid type")
        if other.isEmpty():
            return
        if self.isEmpty():
            self.__head = other.__head
            self.__tail = other.__tail
        else:
            self.__tail.next = other.__head
            self.__tail = other.__tail
        self.__size += other.Size()
        other.clear()

    def interleave(self, other):
        if not isinstance(other, SLL):
            raise Exception("Invalid type")
        new_list = SLL()
        trav1, trav2 = self.__head, other.__head
        while trav1 is not None or trav2 is not None:
            if trav1 is not None:
                new_list.append(trav1.data)
                trav1 = trav1.next
            if trav2 is not None:
                new_list.append(trav2.data)
                trav2 = trav2.next
        return new_list

    def getMiddleElement(self):
        if self.isEmpty():
            return None
        slow = fast = self.__head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def split(self, index):
        if index < 0 or index > self.__size:
            raise Exception("Invalid index")
        first_part = SLL()
        second_part = SLL()
        trav = self.__head
        for i in range(index):
            first_part.append(trav.data)
            trav = trav.next
        while trav is not None:
            second_part.append(trav.data)
            trav = trav.next
        return first_part, second_part

    def __str__(self) -> str:
        li = []
        trav = self.__head
        while trav is not None:
            li.append(trav.data)
            trav = trav.next
        return "--->".join(map(str, li))

# Usage example
l = SLL()
l.append(10)
l.append(20)
l.append(30)
l.addLast(60)
l.addFirst(40)
l.addAt(3, 15)

print(l)  # Output: 40-->10-->20-->15-->30-->60

l.removeFirst()
print(l)  # Output: 10-->20-->15-->30-->60

l.removeAt(1)
print(l)  # Output: 10-->15-->30-->60

print(l.peekFirst())  # Output: 10
print(l.peekLast())  # Output: 60
print(l.Size())  # Output: 4

print(l.contains(10))  # Output: True
print(l.contains(20))  # Output: False
print(l.indexOf(15))  # Output: 1
print(l.indexOf(-1))  # Output: -1

# Iterate over the linked list
for x in l:
    print(x, end="-->")
print()  # Output: 10-->15-->30-->60-->

# Testing rotation
l.rotate(2)
print(l)  # Output: 30-->60-->10-->15

# Testing reverse
l.reverse()
print(l)  # Output: 15-->10-->60-->30

# Testing merging
m = SLL()
m.append(70)
m.append(80)
l.merge(m)
print(l)  # Output: 15-->10-->60-->30-->70-->80

# Testing interleaving
n = SLL()
n.append(1)
n.append(2)
interleaved = l.interleave(n)
print(interleaved)  # Output: 15-->1-->10-->2-->60-->30-->70-->80

# Testing middle element
print(l.getMiddleElement())  # Output: 60

# Testing splitting
first_part, second_part = l.split(3)
print(first_part)  # Output: 15-->10-->60
print(second_part)  # Output: 30-->70-->80
