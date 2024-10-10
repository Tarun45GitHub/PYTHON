d1={"one":1,"two":2,"three":3,"four":4}
print(d1["one"]) #1
# print(d1["five"])  key error

for x in d1:
    print(x) # print only keys
    print(d1[x]) 

for key,value in d1.items():
    print(key,value)

if "two" in d1:   # find key 
    print("two is present")

print(len(d1))  #4

d1["five"]=5  # add new item
print(d1)

d1.pop("five")
print(d1)

print(d1.popitem())  # return and pop last added items

squar={x:x**2 for x in range(10)}
print(squar)

squar.clear()
print(squar)

keys=["one","two","three"]
d2=dict.fromkeys(keys,"num")
print(d2)