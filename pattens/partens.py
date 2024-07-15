'''
n = 5

    *
   ***
  *****
 *******
*********

 *******
  *****
   ***
    * 
'''

def printPattren(n):
    for i in range(n):
        for j in range(n-1,i,-1):
            print(' ',end='')
        for j in range(1,2*i):
            print('*' ,end= "")
        print()    

printPattren(5)