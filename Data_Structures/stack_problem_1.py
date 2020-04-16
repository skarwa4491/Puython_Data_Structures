"""Problem _1"""
"""use the stack to check is String have balanced set of paranthesis
balanced =(),()(),{}{},([({})])
unbalalnced:(()
"""
from Data_Structures.Stack import Stack


is_balanced=True
s=Stack()
index=0

def is_match(p2,p1):
    if p1=="(" and p2==")":
        return True
    elif p1=="{" and p2=="}":
        return  True
    elif p1=="[" and p2=="]":
        return  True
    else:
        return False
def is_paren_balanced(paren_string):
    global index
    global is_balanced
    while(index<len(paren_string) and  is_balanced):
        paren = paren_string[index]
        if (paren in "[{("):
            s.push(paren)
        else:
            if s.isempty():
                print("it is balanced")
            else:
                top=s.pop()
                if not is_match(paren,top):
                    is_balanced=False
        index+=1

    if(s.isempty() and is_balanced==True):
        return "String is balanced"
    else:
        return "Not Balanced"


result=is_paren_balanced("([({})])")
print(result)
