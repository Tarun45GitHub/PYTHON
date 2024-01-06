#inheritance in python is 5 type
#1.single inheritance
class parent1:
    def __init__(self) :
        print("This is parent one class")
        self.name="Tarun"

class child1(parent1):
    def __init__(self):
        print("This is child one class that inheritant parent 1")
        parent1.__init__(self)
    def display(self):
        print(self.name)

obj1=child1()
obj1.display()
        
#2.multiple inheritance
class parent2:
    def __init__(self) :
        print("This is parent two class")
        self.age=21

class child2(parent1,parent2):
    def __init__(self):
        parent1.__init__(self)
        parent2.__init__(self)
        print("This is child two class inheritant from parent1 and parent2")
    def display(self):
        print(self.name)
        print(self.age)

obj2 =child2()
obj2.display()

#3.multilevel inheritance
class child3(child1):
    def __init__(self):
        child1.__init__(self)
        print("this is multilevel inheritance")
    
obj3=child3()
obj3.display()

#4.Hierarchical inheritance: More than one derived class can be created from a single base.
#5.Hybrid inheritance: This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.

