class employee:
    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age
    def display(self):
        print(self.name," ",self.salary,"",self.age,"")

jack=employee("Jack",30000,24)
jill=employee("Jill",40000,27)
jack.display()
jill.display()