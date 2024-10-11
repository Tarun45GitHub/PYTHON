pet= str(input("Enter type of pet : "))
age= int(input("Enter your pet age : "))

if pet=="Dog":
    if age<2:
        print ("Puppy food ")
    else :
        print("Dog food")
elif pet=="Cat" :
    if age>5:
        print(" Senior cat food ")
    else :
        print("junior cat food")
