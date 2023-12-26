#declaring a class to strore human entity
class human :
    #declare the constructor
    def __init__(self, name="", age=""):
        self.name=name
        self.age=age

    #declare the str function to retun value
    def __str__(self) :
        return "Name : "+str(self.name)+", Age : "+str(self.age)

    #declaring the proprties of the human
    name =""
    age=""


adam=human("adam", 18)
eva=human("Eva", 18)

print(adam)
print(eva)