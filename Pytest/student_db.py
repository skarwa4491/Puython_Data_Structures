import json

class student_db():
    def __init__(self):
        self.__data=None


    def connect(self,data_files):
        with open(data_files) as json_file:
            self.__data=json.load(json_file)


    def get_Data(self,name):
        for student in self.__data["students"]:
            if(student["name"]==name):
                print(student)
                return student

    def close_connections(self):
        pass