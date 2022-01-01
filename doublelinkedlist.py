class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node:Node):
        if self.head:
            current = self.head
            while current.next != None:
                current = current.next
            new_node.prev = current
            current.next = new_node
        else: 
             self.head = new_node

           
        



    def display(self):
        print("Normal order:", end="")
        temp_node = self.head
        while temp_node.next is not None:
            print(temp_node.data, end="")
            temp_node = temp_node.next
        print("Normal order:", end="")
        # getting the last node


def main():
    list = LinkedList()
    list.insert(Node("Mon"))
    list.insert(Node("Tue"))
    list.insert(Node("Wed"))

    list.display()


if __name__ == "__main__":
    main()
