def print_lol(the_list , level=0 , indent=False):
    for each_item in the_list:
        if(isinstance(each_item,list)):
            print_lol(each_item,level+1, indent)
        else:
            if indent==True:
                for tab_stop in range(level):
                    print("\t", end=" ")
            print(each_item)




movies = ['John', 'Eric', ['Cleese', 'Idle'], 'Michael', ['Palin']]

print_lol(movies,indent=True)