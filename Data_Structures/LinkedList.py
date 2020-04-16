class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList():
    def __init__(self):
        self.head=None

    def printList(self):
        current_node=self.head
        while(current_node):
            print(current_node.data)
            current_node=current_node.next

    def append(self,data):
        new_Node=Node(data)
        if(self.head is None):
            self.head=new_Node
            return
        last_node=self.head
        while(last_node.next):
            last_node=last_node.next

        last_node.next=new_Node

    def prepend(self,data):
        new_Node=Node(data)
        if(self.head is None):
            self.head=new_Node
            return
        new_Node.next=self.head
        self.head=new_Node

    def insert_at(self,data,value):
        new_node=Node(data)
        current_node=self.head
        while(current_node):
            if(current_node.data==value):
                new_node.next=current_node.next
                current_node.next=new_node
            current_node=current_node.next
        print("data not available in node")

    def deleteNode(self,data):
        current_node=self.head
        if(current_node and current_node.data==data):
            self.head=current_node.next
            return

        previous_node=None
        while(current_node and current_node.data!=data):
            previous_node=current_node
            current_node=previous_node.next

        if(current_node is None):
            print("data to be deteleted is not present in list")
            return

        previous_node.next=current_node.next










llist=linkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("F")
llist.insert_at("E","B")
llist.printList()
print("*************************")
llist.printList()