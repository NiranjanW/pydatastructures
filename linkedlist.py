class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

    # def __repr__(self):
    #     return "ListNode=" + str(self.value) + " ,next ={" + str(self.nextNode) + "}"


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while True:
            if current.nextNode is None:
                current.nextNode = new_node
                break
            current = current.nextNode

    def printLinkedList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, " -> ",)
            current_node = current_node.nextNode
        print("None")

    def addNode(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.nextNode:
                current = current.nextNode
                current.nextNode = new_node
        else:
            self.head = new_node

    def listprint(self):
        printval = self.head

        while printval is not None:
            print(printval.value)
            printval = printval.next

    def __str__(self):
        s = "Node with value {} and next node: {} .".format(self.head.value , self.head.nextNode.value)
        return s
        # node = self.node
        # nodes =[]
        # while node is not None:
        #     nodes.append(node.value)
        #     node = node.nextNode
        # return [str[node] for node in nodes]

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
            node = node.nextNode
        nodes.append("None")

        print("->".join(nodes))
    def reverseList( self, head:Node) ->Node:
        if head ==None or head.nextNode ==None:
            return head
        prev ,curr =None , head
        while curr:
            next_node = curr.nextNode
            curr.nextNode = prev
            prev = curr
            curr = next_node
        return prev



def main():
    list = LinkedList()
    list.insert("Mon")
    list.insert("Tue")
    list.insert("Wed")
  
    # list.__repr__()
    print(list)
    list.printLinkedList()


if __name__ == "__main__":
    main()
