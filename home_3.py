import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Пример использования
linked_list = LinkedList()
n = 5
numbers = []
for i in range(n):
    random_number = random.randint(5, 100)
    numbers.append(random_number)
for i in numbers:
    linked_list.append(i)


print("Исходный список:")
linked_list.display()

linked_list.reverse()

print("Развёрнутый список:")
linked_list.display()