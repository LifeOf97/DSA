
class Node:

    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"<Node: {self.data}>"


class LinkedList:
    head: Node = None

    def prepend(self, data):
        """Add item at the beginning of the list"""
        self.head = Node(data, self.head)
        
    def append(self, data):
        """Add item at the end of the list"""
        if self.head is None:
            self.head = Node(data, None)
            return
        
        cur_node: Node = self.head

        while cur_node.next:
            cur_node = cur_node.next
        
        cur_node.next = Node(data, None)

    def length(self):
        count: int = 0
        cur_node: Node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        
        return count

    def insert(self, data, index: int):
        """Insert node at index"""
        if (self.head is None) or index < 0 or index >= self.length():
            raise IndexError("INDEX ERROR: Index out of range")
        
        elif index == 0:
            self.prepend(data)
        
        elif index == self.length() - 1:
            self.append(data)
        
        else:
            count: int = 0
            cur_node: Node = self.head

            while cur_node:
                if count == index - 1:
                    cur_node.next = Node(data, cur_node.next)
                    break

                count += 1
                cur_node = cur_node.next


    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return 
        
        values: str = ""
        cur_node: Node = self.head

        while cur_node:
            values += f"{cur_node} --> " if cur_node.next else f"{cur_node}"
            cur_node = cur_node.next

        print(values)
            


if __name__ == "__main__":
    ll = LinkedList()
    ll.print()
    ll.append("first")
    ll.print()
    ll.prepend("second")
    ll.prepend("Third")
    ll.prepend("Fourth")
    ll.print()
    ll.insert("OTHERS", 1)
    ll.print()
