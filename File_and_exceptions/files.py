data=open("abc.txt")

for line in data:
    if(not line.find(":")==-1):
        (role,line_spoken)=line.split(":",1)
        print(role,end="")
        print(" said",end="")
        print(line_spoken,end="")
    else:
        print(line)
data.close()
