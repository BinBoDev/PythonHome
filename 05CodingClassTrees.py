#Ứng dụng tạo cấu trúc cây thư mục
#Tạo phân cấp tổ chức
#Game kiểu Cờ vua
#Rất nhiều những ứng dụng cuả cây thw mục
#Có 2 loại Cây nhị phân (Binary trees) và cây tổng quát (General tree)
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
#Them phan tu vao cay
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root,value)
    def _insert(self,current_node,value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left,value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right,value)
#Duyet  cay (Inoder Traversal)
    def Inoder_Traversal(self,node = None,result = None):
        if result is None:
            result = []
        if node:
            self.Inoder_Traversal(node.left,result)
            result.append(node.value)
            self.Inoder_Traversal(node.right,result)
        return  result
#Vi du uwng dung
tree = BinaryTree()
tree.insert(10)
tree.insert(15)
tree.insert(20)
tree.insert(5)
tree.insert(3)
print(tree.Inoder_Traversal(tree.root))

#Genera tree
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.children = []
    def add_Child(self,child):
        self.children.append(child)
class GeneralTree:
    def __init__(self):
        self.root = None

    #Duyet cay (Depth First Search)
    def dfs(self,node = None,result = None):
        if result is None:
            result = []
        if node:
            result.append(node.value)
            for child in node.children:
                self.dfs(child,result)
        return  result
    #Su dung
root = TreeNode("A")
child1 = TreeNode("B")
child2 = TreeNode("C")
child1.add_Child(TreeNode("D"))
child1.add_Child(TreeNode("E"))
child2.add_Child(TreeNode("F"))
root.add_Child(child1)
root.add_Child(child2)
tree = GeneralTree()
tree.root = root
print(tree.dfs(tree.root))


