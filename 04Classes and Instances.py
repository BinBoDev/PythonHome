# Phân biệt giữa class và intance
#class là một bản thiết kế dành cho đối tượng,nó chứa các thuộc tính và chứa các phương thức mà đối tượng có thể có
#intance thể hiện có đặc tính riêng cảu đối tượng mặc dù cùng được tạo ra từ một class
#Class có Class-level Atributes và intance có intance-level Attribute riêng
class Dog():
    species = "animal" #class -level
    def __init__(self,name):
        self.name = name
    def say(self):
        print(f"{self.name} say is Woof!")
dog1 = Dog("Buck")
print(dog1.name)
dog1.say()
print(dog1.species)
#Intance Method là phương thức cho chính các thuộc tính của đối tượng
# Class Method là phương thức cảu class không liên quan gì đến intance
#Static Method là phương thức không phụ thuộc vào cả class và Intance

class Exam():
    class_variable = "I am class Variable"
    def __init__(self,intance_variable):
        self.intance_variable = intance_variable
    @classmethod
    def showClassVar(cls):
        print(cls.class_variable)
    def showIntanceVar(self):
        print(self.intance_variable)
    @staticmethod
    def staticMethod():
        print("I am static method")
obj = Exam("I am intanceVar")
obj.showIntanceVar()
Exam.showClassVar()
Exam.staticMethod()


