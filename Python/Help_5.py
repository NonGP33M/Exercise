print(" *** odd integer summation from 1 to n ***")
x = int(input("Enter an integer(n) : "))
print("Summation => ",end='')
i = 1
a = 0
while(i <= x):
    if(i%2==1):
        if(i != x and i != x-1):
            print(str(i),end='+')
        else:
            print(str(i),end='')
        a += i
    i += 1
print(" =",str(a))