from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
      if self.storage.length == self.capacity:

        if self.current is None:
          self.current = self.storage.head
          self.storage.remove_from_head()
          self.storage.add_to_head(item)
          self.current = self.storage.head.next

        else:
          tempNode = self.storage.head
          while self.current:
            if tempNode == self.current:
              self.current = self.current.next
              tempNode.insert_before(item)
              # Need to manually lengthen doubly linked list since insert_before is an individual node method 
              self.storage.length += 1
              self.storage.delete(tempNode)
              break
            elif tempNode is None:
              self.current = self.storage.head
              break
            else:
              tempNode = tempNode.next

      else:
        self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

         # TODO: Your code here
        counter = self.storage.head

        while counter:
          # if  counter is not None:
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
