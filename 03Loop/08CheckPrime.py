number=int(input("enter Number : "))

prime=True
if number>1:
    for i in range(2,number):
        if number%i==0: 
            prime=False
            break
else :
    prime=False

if prime:
    print(number ,"is prime")
else :
    print(number, "is not prime")




