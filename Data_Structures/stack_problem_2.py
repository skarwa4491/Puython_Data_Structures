"""use stack data structure to convert int value to binary data structure"""
from Data_Structures.Stack import Stack

s=Stack()
def convert_to_binary(int):

    while(int>0):
        reminder=int%2
        s.push(reminder)
        int=int//2
    bin_num=""
    while(not s.isempty()):
        bin_num+=str(s.pop())
    return bin_num

num=convert_to_binary(242)
print(int(num,2))




