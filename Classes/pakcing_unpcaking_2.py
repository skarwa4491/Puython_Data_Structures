records=[

    ('foo',1,2),
    ('bar',1,2),
    ('foo',3,4)
]

def do_foo(x,y):
    print("Foo",x,y)
def do_bar(x,y):
    print("o_bar")


for tag,*args in records:
    if tag=='foo':
        do_foo(*args)


items = [1, 10, 7, 4, 5, 9]

head, *tail= items

sum=head+sum(tail)

print(sum)