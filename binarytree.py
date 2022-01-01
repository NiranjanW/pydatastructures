class Node:
    def __init__(self,value=None ):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        

class BinaryTree :
     def __init__(self):
         self.root = None

     def insert(self,value):
         new_node = Node(value)
         if self.root is None:
             self.root =Node(value)
         else:
             self._insert(value ,self.root)
        #  if data < self.head.data:
        #      if self.left is None:
        #          self.left = new_node
        #      else:
        #          self.head.left(data)
        #  elif data > self.head.data:
        #          if self.right is None:
        #              self.right = new_node
        #          else :
        #              self.head.right(data)
        #  else:
        #      self.head = new_node

     def _insert(self,value,cur_node):
         if value < cur_node.value:
             if cur_node.left == None:
                 cur_node.left=Node(value)
             else:
                  self._insert(value,cur_node.left)
         elif value > cur_node.value:
             if cur_node.right ==None:
                cur_node.right=Node(value)
             else:
                 self._insert(value,cur_node.right)
         else:
             print ("Value already in tree")

     def print_tree(self):
         if self.root is not None:
             self._print_tree(self.root)

     def _print_tree(self, cur_node):
         if cur_node != None:
             self._print_tree(cur_node.left )
             print (str(cur_node.value)+ "/")
             self._print_tree(cur_node.right )
             print (str(cur_node.value)+ "\\")

     def height(self):
         if self.root is  None:       
             return 0
         else:
             return self._height(self.root,0)

     def _height(self, cur_node, cur_height):
         if cur_node is  None : return cur_height
         left_height = self._height(cur_node.left , cur_height+1)
         right_height = self._height(cur_node.right , cur_height+1)
         return max(left_height , right_height)


    #  def PrintTree(self):
    #       if self.head.left :
    #           self.head.left.PrintTree()
    #       print (self.data),
    #       if self.right:
    #            self.right.PrintTree()

def fill_tree( btree , num_elems=10 , max_int=100):
    from  random import randint
    for _ in range(num_elems):  
        cur_elem =randint(0, max_int)
        tree.insert(cur_elem)
    return tree

if __name__ == '__main__':
    tree = BinaryTree()
    tree = fill_tree(tree)
    # print(tree.root.value , tree.root.left.value, tree.root.right.value)
    tree.print_tree()

    