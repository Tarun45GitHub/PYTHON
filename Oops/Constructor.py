class student:
    def __init__(self,name,age): #constructor it use to asigned memory
        self.name=name
        self.age=age
    def print_name(self):
        print(self.name)
    def print_age(self):
        print(self.age)
    

s1=student("tarun",21)
s1.print_name()

       