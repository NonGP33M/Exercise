n = int(input())
a = []
b = 0
c = 0

for i in range(n):
    for j in input().split():
        a.append(int(j))
    b = a[0]
    c = a[n-1]

for k in range(1,n):
    b = b+a[k*n+k]
for l in range(2,n+1):
    c = c+ a[(n-1)*l]

if(sum(a[:n]) == sum(a[n:n+n]) and sum(a[:n]) == b and sum(a[:n]) == c):
    if(sum(a)/n**2 == 1):
        print("MUGGLE")
    else:
        print("MAGIC")

else:
    print("MUGGLE")

