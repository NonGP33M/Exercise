s = int(input())
a = s-2
for i in range(s):
    print('-'*(s-i),end='')
    print('*'*(2*i+1),end='')
    print()
for i in range(1,s):
    print('-'*(i+1),end='')
    print('*'*(2*a+1),end='')
    print()
    a -= 1