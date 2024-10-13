def sum_all(*args):
    sum=0
    cnt=0
    for i in args:
        sum+=i
        cnt+=1
    return sum,cnt
    # return sum(args)

print(sum_all(1,2,3,4))
print(sum_all(1,2,3,4,6,7,8))

