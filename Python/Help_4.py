print(" *** integer summation from 1 to n ***")
x = int(input("Enter an integer(n) : "))
print("Summation => ",end='')
i = 1
a = 0
while(i <= x):
    a += i
    if(i != x):
        print(str(i),end='+')
    else:
        print(str(i),end='')
    i += 1
print(" =",str(a))