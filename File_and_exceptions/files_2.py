try:
    data = open("abc.txt")
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(":",1)
            print(role , end="")
            print("said",end="")
            print(line_spoken,end="")

        except ValueError:
            pass
except IOError:
    print("data file is missing")