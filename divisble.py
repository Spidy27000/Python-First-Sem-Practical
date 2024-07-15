def is_divisble(n):
    return (n%3 ==0)

n = int(input("enter the number"))

if (is_divisble(n)):
    print(n,"is divisble by 3")
else:
    print(n,"is not divisble by 3")