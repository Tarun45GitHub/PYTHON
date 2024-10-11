score= int(input("Enter your markes : "))

# if score>101:
#     print("please verify your score")
#     exit()

if score>101:
      grade="please veryfy your score"
elif score>=90:
    grade="A"
elif score>=80:
    grade="B"
elif score>=70:
    grade="C"
elif score>=60:
    grade="D"
else :
    grade="F"

print(grade)