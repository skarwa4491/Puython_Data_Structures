class Node():
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

class Binary_Tree():
    def __init__(self):
        pass
    def create_new_Node(self,val):
        self.node=Node(val)
        return self.node

    def insert(self,node,val):
        if(node==None):
            return self.create_new_Node(val)
        else:
            if(val<node.val):
                node.left=self.insert(node.left,val)
            else:
                node.right=self.insert(node.right,val)
        return node



root=None
a=Binary_Tree()
root=a.insert(root,8)
root=a.insert(root,3)
root=a.insert(root,10)
root=a.insert(root,1)








