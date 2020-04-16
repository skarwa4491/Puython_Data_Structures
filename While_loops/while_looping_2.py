active=True
prompt="i am a parrot and will echo your message unitl you type 'quit'"

message=input(prompt)

while active:

    message=input(prompt)
    if(message=='quit'):
        break
    else:
        print(message)


print("**************************************************")

current_numer=0
while current_numer <10:
    current_numer+=1
    if(current_numer%2==0):
        continue
    print(current_numer)
