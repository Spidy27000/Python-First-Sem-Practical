string = "ABCDEFGHI"

for i in range(len(string),0, -2):
    for _ in range(0,len(string) - i,2):
        print("  " ,end = "")
    for j in range(i):
        print(f"{string[j]} ", end = "")
    print ()
