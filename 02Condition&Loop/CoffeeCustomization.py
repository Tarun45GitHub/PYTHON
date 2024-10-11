size=str(input("which size you want : "))
extra_shot=bool(input("Are like to take extra_shot : "))

if extra_shot :
    coffee= size + " coffie with an extra shot"  
else :
    coffee= size +" coffee"

print("order : ",coffee)