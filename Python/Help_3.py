def triangleChecker(a,b,c):
    if a == 0 or b == 0 or c == 0 :
        print("Side of triangle must not be zero.")
    elif a < 0 or b < 0 or c < 0 :
        print("INPUTs cannot be negative.")
        
print(" *** Triangle Checker ***")
a,b,c = map(int,(input("Enter side1 side2 side3 : ").split()))
triangleChecker(a,b,c)