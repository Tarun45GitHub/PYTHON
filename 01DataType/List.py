l1=["A","B","C","D"]
print(l1)
print(l1[0])
print(l1[-1]) # first element from right side
print(l1[2:4]) # element 2 to 4 ,but not 4
print(l1[-4:4]) # allaways print left to right
print(l1[1:1]) # empty list

l1[2]="E"
print(l1) # list is mutable

l1[1:2]="efg"
print(l1) # [A,e,f,g,E,D]
l1[1:2]=["bcd"]
print(l1)
l1[1:4]=["B","C","D"]
print(l1)

print(l1.pop())   #pop and return last element
print(l1)
l1.append("F")
print(l1)
l1.remove("B")  # remove the  value
print(l1)
l1.insert(1,"B")
print(l1)

l2=l1 #give same memory reference
l1.pop()
print(l1)
print(l2)

l3=l1.copy() # give copy of value
l1.append("F")
print(l1)
print(l3)

l4=[x**3 for x in range(10)]
print(l4)

