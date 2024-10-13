import math
def circle(radious):
    circum=2*math.pi*radious
    area=math.pi*radious**2
    return circum,area

circum,area=circle(5)
print(round(circum,3),round(area,3))