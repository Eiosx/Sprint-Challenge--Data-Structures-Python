from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
      if self.storage.length == self.capacity:
        # self.storage.delete(self.current)
        self.storage.add_to_head(item)
        counter = self.storage.head
        while counter != self.current:
          if counter.next == self.current:
            self.storage
        self.current = self.storage.head.next
      else:
        if self.storage.length == 0:
          self.storage.add_to_tail(item)
          self.current = self.storage.tail
        else:
          self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        counter = self.storage.head

        while counter:
          if  counter.value != None:
            list_buffer_contents.append(counter.value)
            counter = counter.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
