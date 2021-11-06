h = int(input("Enter a number of : "))
for i in range(h):
    print(" "*(h-i-1),end="")
    for j in range(i+1):
        print("* ",end="")
    print()