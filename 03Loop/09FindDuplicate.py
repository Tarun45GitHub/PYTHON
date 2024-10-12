num=[1,3,4,5,2,4]

unique= set()

for i in num:
    if i in unique:
        print(i)
        break
    unique.add(i)