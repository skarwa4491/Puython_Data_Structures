from prompt_toolkit.application import current

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

    def delete_node_at_index(self,index):
        current_node = self.head
        if(index==0):
            self.head = current_node.next
            return

        count=1
        prev_node=current_node
        current_node=current_node.next
        while(current_node and count!=index):
            prev_node=current_node
            current_node=current_node.next
            count+=1

        if current_node is None:
            print("provided index to be deleted is not present in list")
            return

        prev_node.next=current_node.next
        current_node=None

    def len(self):
        count=1
        current_node=self.head
        if(current_node.next==None):
            return 1
        while(current_node and current_node.next!=None):
            current_node=current_node.next
            count+=1

            if(current_node.next==None):
                break
        return count

    def node_swap(self,key1,key2):
        prev_1=None
        curr_1=self.head

        if (key1==key2):
            print("values cannot be swapped as both are same")

        while(curr_1 and curr_1.data!=key1):
            prev_1=curr_1
            curr_1=curr_1.next


        print(prev_1.data,curr_1.data)
        curr_2=self.head
        prev_2=None

        while (curr_2 and curr_2.data != key2):
            prev_2 = curr_2
            curr_2 = curr_2.next
        print(prev_2.data,curr_2.data)

        if(prev_1):
            prev_1.next=curr_2
        else:
            self.head=curr_2
        if(prev_2):
            prev_2.next=curr_1
        else:
            self.head=curr_1

        print(curr_1.data,curr_2.data,prev_1.data,prev_2.data)

        curr_1.next,curr_2.next=curr_2.next,curr_1.next







llist=linkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("F")
llist.insert_at("E","B")
print("************Before Deteling _node*************")
llist.printList()
llist.deleteNode("F")
print("************After Deteling _node*************")
llist.printList()
print("************After Deteling_node_by_index*************")
llist.delete_node_at_index(2)
llist.printList()
print(llist.len())
llist.node_swap("B","C")
print("************After swapping*************")
llist.printList()
