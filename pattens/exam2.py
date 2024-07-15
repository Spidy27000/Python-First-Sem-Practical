# n = int(input("enter the input : "))
n = 9
'''
print
    1
   1 2
  1   2
 1     2
123456789  

''' 
for i in range((n//2)+1):
    for _ in range(n//2 - i,0,-1):
        print(" ",end="")
    for j in range(1,(2*i)+2):
        if i != n//2: 
            if j == 1 or j == (2*i)+1:
                print(2, end = "")
            else:
                print(" " ,end = "")
        else :
            print(j, end = "")

    print()