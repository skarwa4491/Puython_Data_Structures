import os
import pickle
man=[]
other_man=[]
try:
    data=open(os.getcwd()+"/abc.txt")
    for line in data:
        try:
            (role,line_said)=line.split(":",1)
            if(role =="Man"):
                man.append(line_said)
            elif(role =="Other Man"):
                other_man.append(line_said)
        except ValueError:
            pass
except IOError:
    print("file is not present")

try:
    with open("man.txt","wb") as man_data,open("other_man.txt","wb") as other_man_data:
        pickle.dump(man,man_data)
        pickle.dump(other_man,other_man_data)
except IOError as err:
    print(err)
except pickle.PicklingError as prr:
    print(prr)

try:
    with open("man.txt","rb") as man_data:
        new_man_data=[line.rstrip() for line in pickle.load(man_data)]
        print(new_man_data)
except IOError as err:
    print(err)
except pickle.UnpicklingError as uerr:
    print(uerr)




