class Parent():
    def __init__(self,last_name, eye_color):
        print "parent construction called"
        self.last_name =last_name
        self.eye_color=eye_color

    def show_info(self):
        print "last name - "+self.last_name
        print "eye color - "+self.eye_color

class Child(Parent):
    def __init__(self,last_name,eye_color, number_of_toys):
        print "child construction called"
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self): #method overriding
        print "last name - "  +self.last_name
        print "eye color - " +self.eye_color
        print "number of toys - " +self.number_of_toys

prakash = Parent("jain","black")
print prakash.show_info()

ashok = Child("jain","blacks","2")
print ashok.show_info()

"""print ashok.eye_color
print ashok.number_of_toys
print ashok.last_name
print prakash.eye_color
print prakash.last_name"""

