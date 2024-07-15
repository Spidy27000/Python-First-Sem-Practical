a = int(input("enter first number:"));
b = int(input("enter second number:"));
c = int(input("enter third number:"));

def min_of_three(a,b,c):
    min = 0
    if a>b:
        if a>c:
            min = c
        else:
            min = a
    else:
        if b>c:
            min = c
        else :
            min = b
    return min


print (f"the minimun in {a},{b} and {c} is {min_of_three(a,b,c)}")