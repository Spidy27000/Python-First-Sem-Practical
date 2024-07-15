a = float(input("enter first number:"))
b = float(input("enter second number:"))
c = float(input("enter third number:"))


def max_of_three(a,b,c):
    max = 0
    if a>b:
        if a>c:
            max = a
        else:
            max = c
    else:
        if b>c:
            max = b
        else :
            max = c
    return max

print (f"the maximum in {a},{b} and {c} is {max_of_three(a,b,c)}")