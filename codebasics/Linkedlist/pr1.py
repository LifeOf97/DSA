# linkedlist

class Node:

    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"<Node: {self.data}>"


class LinkedList:

    def __init__(self) -> None:
        self.head: Node = None

    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return 
        
        values: str = ""
        current_node: Node = self.head

        while current_node:
            values += f"{current_node} --> " if current_node.next else f"{current_node}"
            current_node = current_node.next

        print(values)

    def prepend(self, data) -> None:
        """Add item at the beginning of the list"""
        self.head = Node(data, self.head)

    def insert_nodes(self, data_list: list) -> None:
        """Insert a list of data_list into list"""
        if isinstance(data_list, (list, tuple)):
            for _ in data_list:
                self.append(_)
            return

        raise ValueError("data_list must be a list of values")

    def append(self, data) -> None:
        """Add item at the end of the list"""
        if self.head is None:
            self.head = Node(data, None)
            return
        
        current_node: Node = self.head

        while current_node.next:
            current_node = current_node.next
        
        current_node.next = Node(data, None)

    def length(self) -> int:
        """Get number of elemnts (Node) in LinkedList"""
        count: int = 0
        current_node: Node = self.head

        while current_node:
            count += 1
            current_node = current_node.next
        
        return count

    def insert(self, data, index: int):
        """Insert node at index"""
        if (self.head is None) or index < 0 or index > self.length():
            raise IndexError("Index out of range")
        
        elif index == 0:
            self.prepend(data)
        
        elif index == self.length():
            self.append(data)
        
        else:
            count: int = 0
            current_node: Node = self.head

            while current_node:
                if count == index - 1:
                    current_node.next = Node(data, current_node.next)
                    break

                count += 1
                current_node = current_node.next

    def remove(self, index: int):
        """Remove node at index"""
        if (self.head is None) or index < 0 or index >= self.length():
            raise IndexError("Index out of range")
        
        elif index == 0:
            self.head = self.head.next
        
        else:
            count: int = 0
            current_node: Node = self.head

            while current_node:
                if count == index - 1:
                    current_node.next = current_node.next.next
                    break

                count += 1
                current_node = current_node.next

    def insert_after_node(self, instert_after_node: str, node_to_insert: str) -> None:
        """Insert a node after the first occurance of the node to insert after"""
        if not self.length():
            raise ValueError("LinkedList is empty")
        
        count: int = 0
        current_node: Node = self.head

        while current_node:
            if current_node.data == instert_after_node:
                current_node.next = Node(node_to_insert, current_node.next)
                break

            count += 1
            current_node = current_node.next
    
    def remove_by_node(self, node):
        """Remove first occurance of node"""
        if not self.head:
            raise ValueError("LinkedList is empty")
        
        count: int = 0
        current_node: Node = self.head

        while current_node:
            if (current_node.data == node) and (count == self.length()  - 1):
                self.remove(count)
                break

            elif current_node.data == node:
                current_node.data = current_node.next.data
                current_node.next = current_node.next.next
                break

            count += 1
            current_node = current_node.next


if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_nodes(["banana","mango","grapes","orange"])
    # ll.print()
    # ll.insert_after_node("mango","apple") # insert apple after mango
    # ll.print()
    # ll.remove_by_node("orange") # remove orange from linked list
    # ll.print()
    # ll.remove_by_node("figs")
    # ll.print()
    # ll.remove_by_node("banana")
    # ll.remove_by_node("mango")
    # ll.remove_by_node("apple")
    # ll.remove_by_node("grapes")
    ll.insert_nodes([1,2,3,4,5])
    ll.print()
    print(ll.length())
    ll.remove(5)
    ll.print()
    print(ll.length())
