class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  
        self._size = 0

    def append(self, value):
        new_node = Node(value)
        
        if self.head is None:  
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1  

    def prepend(self, value):
        new_node = Node(value, next=self.head)
        self.head = new_node
        
        if self.tail is None:  
            self.tail = new_node
        
        self._size += 1  

    def insert(self, idx, value):
        if idx < 0 or idx > self._size:  
            raise IndexError
        
        if idx == 0:
            self.prepend(value)
            return
        
        if idx == self._size:
            self.append(value)
            return
        
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        new_node = Node(value, next=current.next)
        current.next = new_node
        
        self._size += 1  

    def remove(self, value):
        if self.head is None:  
            return

        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:  
                self.tail = None
            self._size -= 1
            return
        
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        
            if current.next == self.tail:  
                self.tail = current
            current.next = current.next.next
            self._size -= 1

    def remove_at(self, idx):
        if idx < 0 or idx >= self._size:  
            raise IndexError
        
        if idx == 0:  
            self.head = self.head.next
            if self.head is None:  
                self.tail = None
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            if current.next == self.tail:  
                self.tail = current
            current.next = current.next.next
        
        self._size -= 1  

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"
    def peek_first(self):
        if self.head is None:
            return None
        return self.head.value

    def peek_last(self):
        if self.tail is None:
            return None
        return self.tail.value
    
if __name__ == "__main__":
    lst = SinglyLinkedList()
    
    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(lst)  
    print(f"Size: {len(lst)}")  
    
    lst.prepend(0)
    print(lst)  
    
    lst.insert(2, 1.5)
    print(lst)  
    
    lst.remove(1.5)
    print(lst)    

    print("Итерация:")
    for item in lst:
        print(item)
    
  
    print(f"First: {lst.peek_first()}, Last: {lst.peek_last()}")  