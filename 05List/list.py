marks=[98,96,95,"tarun"]
print(marks)
print(marks[3])
print(marks[-2])  #count from end
print(marks[1:3]) #1 to 3 ,not include 3,1and,2

print("for loop in List")
for i in marks:
    print(i)

marks.append(92)  #add at last
print(marks)

marks.insert(1,93)
print(marks)
print(len(marks))
print("while loop in List")
i=0
while i<len(marks):
    print(marks[i])
    i+=1

#marks.clear()  clear the list