year=int(input("Enter year :"))

if year%100:
    if year%400:
        print(year, " is leap year ")
elif year%4:
   print(year, " is leap year ")
else :
    print(year, " is not  leap year ")