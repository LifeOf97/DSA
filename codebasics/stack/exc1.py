"""
Write a function in python that checks if paranthesis in the string are balanced or not.
Possible parantheses are "{}',"()" or "[]".

Example test cases:
    is_balanced("({a+b})")     --> True
    is_balanced("))((a+b}{")   --> False
    is_balanced("((a+b))")     --> True
    is_balanced("))")          --> False
    is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

"""

from collections import deque
import re

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


def is_match(char1, char2) -> bool:
    match_dict: dict = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    return match_dict[char1] == char2


def is_balanced(value: str) -> bool:
    stack = Stack()
    chars: list = re.findall(r"[(){}[\]]", value)

    for char in chars:
        match char:
            case "(" | "{" | "[":
                stack.push(char)
            case ")" | "}" | "]":
                # if no paranthesis in the stack
                if stack.size() == 0:
                    return False
                if not is_match(char, stack.pop()):
                    return False


    return stack.size() == 0


if __name__ == "__main__":
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))