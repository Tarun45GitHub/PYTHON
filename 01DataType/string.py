name="Tarun Dalbera"
print(name[0]) # T
print(name.upper())
print(name.lower())
print(name) # All string methods return new values. They do not change the original string.
print(name.strip()) # remove unnessary space
print (name.find("a"))  #return index strting from 0
print(name.find("arun"))
print(name.replace("Dalbera","kumar"))
print(name.count('a')) # count of a
print(name)
print ('T'in name)   #return true or false
for t in name:
    print(t)


print(5*" tarun ")

num="0123456789"
print(num[:])  # first ot last
print(num[0:])  # 0 to last
print(num[:8])  # first to 8
print(num[0:8:2])  # 0 to 8 by hopping 2

number="1,2,3,4"
print(number.split(",")) # return list

l1=["1","2","3","4"]
print("".join(l1)) #1234
print(", ".join(l1)) #"1, 2, 3, 4"

sentense=" my name is {} and age is {}"
age=21

print(sentense.format(name,age))

st1="he said \"my name is Tarun\" "
print(st1)
st2= "tarun\nkumar"
print(st2)
str3= r"tarun\nkumar"
print(str3)






