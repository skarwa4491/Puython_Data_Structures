class polygon():

    def set_height_width(self,height,width):
        self.__height=height
        self.__width=width

    def get_height(self):

        return self.__width,self.__height

    def __cant_override(self):
        print("cannot override")

class triangle(polygon):

    def area(self):

        self.height,self.weight=self.get_height()
        self.__cant_override()
        return (self.height*self.weight)/2

    def cant_override(self):
        return super().__cant_override


tt=triangle()
tt.set_height_width(10,20)
func=tt.cant_override()
func()