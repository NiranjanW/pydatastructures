class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return "ListNode=" + str(self.value) + " ,next ={" + str(self.next) + "}"


class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
                current.next = new_node
        else:
            self.head = new_node

    def listprint(self):
        printval = self.head

        while printval is not None:
            print(printval.value)
            printval = printval.next

    # def __str__(self):
    #     return "->".join([str[node] for node in self])

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")

        print( "->".join(nodes))


def main():
    list = LinkedList()
    list.addNode(Node("Mon"))
    list.addNode(Node("Tue"))
    list.addNode(Node("Wed"))
    list.__repr__()
    print(list)
    # list.listprint()


if __name__ == "__main__":
    main()
