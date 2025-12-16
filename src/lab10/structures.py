from collections import deque
from typing import Any

class Stack:
    def __init__(self):
        self._data: list[Any] =[]

    def push(self, item: Any) -> None:
        self._data.append(item)

    def pop(self) -> Any:
     if self.is_empty():
        raise IndexError('стек пуст')
     return self._data.pop()
    
    def peek(self)-> Any:
       if self.is_empty():
          return None
       return self._data[-1]
    
    def is_empty(self)-> bool:
       return len(self._data) == 0
    
    def __len__(self) -> int:
       return len(self._data)
    
    def __repr__(self) -> str:
       return self.__str__()
    def __str__(self) ->str:
       return f"Stack({self._data})"
    
class Queue:
    def __init__(self):
        self._data= deque()
    
    def enqueue(self, item: Any) -> None:
       self._data.append(item)
    
    def dequeue(self) -> Any:
       if self.is_empty():
          raise IndexError('очередь пуста')
       return self._data.popleft()
    
    def peek(self) -> Any:
       if self.is_empty():
          return None
       return self._data[0]
    
    def is_empty(self) -> bool:
       return not self._data
    
    def __len__(self) -> int:
       return len(self._data)
    
    def __repr__(self) -> str:
       return self.__str__()
    def __str__(self) -> str:
       return f"Queue({list(self._data)})"
      

def test():
    print("тест стека:")
    s = Stack()

    s.push(15)
    s.push(25)
    s.push(35)
    print(f"после push 15,25,35: peek={s.peek()}")
    
    print(f"1: {s.pop()}")
    print(f"2: {s.pop()}")
    print(f"3: {s.pop()}")
    
    try:
        s.pop()
    except IndexError as e:
        print(f"ошибка при pop пустого стека: {e}")
    
    print("\nтест очереди:")
    q = Queue()
    print(f"пустая очередь: is_empty={q.is_empty()}, peek={q.peek()}")
    
    q.enqueue('A')
    q.enqueue('S')
    q.enqueue('C')
    q.enqueue('I')
    q.enqueue('I')
    print(f"после enqueue A,S,C,I,I: peek={q.peek()}")
    
    print(f"1: {q.dequeue()}")
    print(f"2: {q.dequeue()}")
    print(f"3: {q.dequeue()}")
    print(f"4: {q.dequeue()}")
    print(f"5: {q.dequeue()}")
    
    try:
        q.dequeue()
    except IndexError as e:
        print(f"ошибка при dequeue пустой очереди: {e}")

if __name__ == "__main__":
    test()