#Cách Python tìm kiếm một thuộc tính attribute trong một hệ thống phân cấp kế thừa (inheritance hierarchy)
#1,Trước hết nó tìm kiếm trong đối tượng,nó tìm kiếm trực tiếp thông qua thuộc tính __dict__ cảu đối tượng.
#Thuộc tính __dict__ cảu đối tượng chứa tất cả các thuộc tính có thể thay đổi được của một đối tượng
class ExamDictObj ():
    def __init__(self,a,b):
        self.a = a
        self.b = b
obj = ExamDictObj(5,10)
print(obj.__dict__)
#Class cũng có thuộc tính __Dict__ để lưu chữ các method và
print(ExamDictObj.__dict__)
#2.Sau khi tìm trong đối tượng không có nó sẽ tiến hành tìm trong lớp
#3.Nếu không tìm thấy trong class nó sẽ tìm kiếm theo MRO.Có 2 cách

class A():

    def show(self):
        print("A")
class B(A): # B kế thừa A

    def show(self):
        print("B")
class C(B): # C kế thừa B

    def show(self):
        print("C")
obj1 = A()
obj1.show()
obj2 = B()
obj2.show()
obj3 = C()
obj3.show()
#Phương thức Supper() là cách thức gọi trực tiếp phương thức kế thừa của lớp cha
class Cha():
    def show(self):
        print("method lop cha")

class Con(Cha):
    def show(self):
        super().show() # Goi phuowng thuc lop Cha
        print("Method lop con")
objcon = Con()
objcon.show()
