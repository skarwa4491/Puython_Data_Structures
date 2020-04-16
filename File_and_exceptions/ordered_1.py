import os
# controller goes to start of the file.

data=open("abc.txt")
for item in data:
    print(item ,end="")

os.chdir("..")
print(os.getcwd())
os.chdir(os.getcwd()+"/File_and_exceptions")
print(os.getcwd())
