# doubly linkedlist
# Implement doubly linked list. The only difference with regular linked list is
# that double linked has prev node reference as well. That way you can iterate in
# forward and backward direction.

from typing import Any


class Node:

    def __init__(self, data = None, next = None, prev = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return f"<Node: {self.data}>"



class DoublyLinkedList:

    def __init__(self) -> None:
        self.head: Node = None

    def length(self) -> int:
        """Return the number of nodes in the list"""
        count: int = 0
        current_node: Node = self.head

        while current_node:
            current_node = current_node.next
            count += 1
        
        return count

    def print_forward(self) -> None:
        """Print all node in list"""
        if not self.head:
            print("Doubly linkedlist is empty")
        
        values: str = ""
        current_node: Node = self.head

        while current_node:
            values += f"{current_node} <--> " if current_node.next else f"{current_node}"
            current_node = current_node.next
        
        print(values)

    def print_backward(self):
        """Print all node in list from right to left"""
        if not self.head:
            print("Doubly linkedlist is empty")

        values: str = ""
        tail_node: Node = self.get_last_node()

        while tail_node:
            values += f"{tail_node} <--> " if tail_node.prev else f"{tail_node}"
            tail_node = tail_node.prev
        
        print(values)

    def get_last_node(self) -> Node:
        """Return the last node in linked list"""
        if not self.head:
            print("Doubly linkedlist is empty")

        current_node: Node = self.head

        while current_node.next:
            current_node = current_node.next

        return current_node


    def prepend(self, data: Any) -> None:
        """Add a new node at the head of the linkedlist"""

        if not self.head:
            self.head = Node(data)
        else:
            node = Node(data, self.head)
            self.head.prev = node
            self.head = node

    def append(self, data):
        """Add a new node at the end of the linkedlist"""
        if not self.head:
            self.prepend(data)
            return

        current_node: Node = self.head

        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data, None, current_node)

    def insert_datas(self, data_list: list) -> None:
        """Insert a list of data into the list"""
        if not isinstance(data_list, (list, tuple)):
            raise ValueError("data_list must be a list of values")
        
        for _ in data_list:
            self.append(_)

    def insert(self, data, index: int) -> None:
        """Insert data at a specific index"""
        if not self.head or index < 0 or index > self.length():
            raise IndexError()
        
        if index == 0:
            self.prepend(data)
        
        count: int = 0
        current_node: Node = self.head

        while current_node:
            if count == index - 1:
                node = Node(data, current_node.next, current_node)

                if node.next:
                    current_node.next.prev = node

                current_node.next = node
                break

            count += 1
            current_node = current_node.next

    def remove(self, index: int) -> None:
        """Remove node at a specific index"""

        if not self.head or index < 0 or index >= self.length():
            raise IndexError()

        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count: int = 0
        current_node: Node = self.head

        while current_node:
            if count == index:
                current_node.prev.next = current_node.next
                
                if current_node.next:
                    current_node.next.prev = current_node.prev
                break

            count += 1
            current_node = current_node.next

    def insert_after_node(self, instert_after_node: str, node_to_insert: str) -> None:
        """Insert a node after the first occurance of the node to insert after"""
        
        if not self.head:
            raise ValueError("LinkedList is empty")
        
        current_node: Node = self.head

        while current_node:
            if current_node.data == instert_after_node:
                node: Node = Node(node_to_insert, current_node.next, current_node)

                if node.next:
                    current_node.next.prev = node

                current_node.next = node
                break

            current_node = current_node.next


    def remove_by_node(self, node):
        """Remove first occurance of node"""
        if not self.head:
            raise ValueError("LinkedList is empty")
        
        if self.head.data == node:
            self.head = self.head.next
            self.head.prev = None
            return 
        
        current_node: Node = self.head

        while current_node:
            if current_node.data == node:
                current_node.prev = current_node.next

                if current_node.next:
                    current_node.next.prev = current_node.prev
                
                break

            current_node = current_node.next


if __name__ == "__main__":
    dll = DoublyLinkedList()
    print(dll.length())
    dll.insert_datas([1,2,3,4,5])
    dll.append(22)
    dll.print_forward()
    dll.print_backward()
