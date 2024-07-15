from math import pi as PI
def area_and_circumfernce(r):
    return (r*r*PI),(2*r*PI)

r = float(input("enter the radius: "))
area ,curumfrence = area_and_circumfernce(r)
print("the area of cirles is " ,area ," and ", curumfrence)

