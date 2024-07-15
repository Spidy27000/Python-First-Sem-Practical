
def isPrime(n:int)-> bool:
    for i in range(2,(n//2)+1):
        if n % i == 0:
            return False    
    else:
        return True
    
n = int (input("Enter the number: "))
print(f"the number {n} is {'prime' if isPrime(n) else 'not prime'}")

