# Write a function in python that can reverse a string using stack data structure.
# EXAMPLE:
#   reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

from collections import deque


class Stack:

    def __init__(self) -> None:
        self.container = deque()

    def push(self, value):
        return self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]
    
    def is_empty(self) -> bool:
        return len(self.container) == 0
    
    def size(self) -> int:
        return len(self.container)
    
    def data(self):
        return self.container

    def reverse(self) -> None:
        self.container.reverse()

# Solution before seeing exercise solution
# def reverse_string(data: str) -> str:
#     value: str = ""
#     stack = Stack()
#     [stack.push(x) for x in data.split()]

#     for x in range(stack.size()):
#         d = list(stack.pop())
#         d.reverse()
#         value += "".join(d) + " "

#     print(value)


# solution after seeing exercise solution
def reverse_string(data: str) -> str:
    value: str = ""
    stack = Stack()
    [stack.push(x) for x in data]

    for x in range(stack.size()):
        value += stack.pop()

    print(value)


if __name__ == "__main__":
    reverse_string("91-DIVOC ereuqnoc lliw eW")