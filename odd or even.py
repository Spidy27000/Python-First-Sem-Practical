n = int(input("enter thr number"))
def is_even(n):
    return not (n%2)

if is_even(n):
    print(f"{n} is even")
else:
    print(f"{n} is odd")