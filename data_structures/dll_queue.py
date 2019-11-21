from dll import DoublyLinkedList
# import sys
# sys.path.append('./dll')


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        value = self.storage.remove_from_head()

        if value is not None:
            self.size -= 1

        return value

    def len(self):
        return self.size
