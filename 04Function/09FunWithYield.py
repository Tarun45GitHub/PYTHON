# def even_generator(limit):
#     li=[]
#     for i in range(2,limit+1,2):
#         li.append(i)
#     return li


def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i

for i in even_generator(10):
    print(i)