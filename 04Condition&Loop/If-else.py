age=int(input("Enter your age "))

if age>=21:
    print("you are can vote")
    print("now you can marry")
elif age>=18 and age<=21:
    print("now you can vote")
else:
    print("you are child")