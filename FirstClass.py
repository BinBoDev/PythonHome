#Example first
class mauClass:
    def setdata(self,value):
        self.data = value
    def displayData(self):
        print(self.data)

x = mauClass()
y = mauClass()
x.setdata("Bian")
y.setdata(3.14)
x.displayData()
y.displayData()
x.setdata("Bin")
x.displayData()
