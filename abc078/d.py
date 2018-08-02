###
n, z, w = map(int, input().split())

a = [int(x) for x in input().split()]


if n == 1:
    print(abs(a[0]) - w)

else:
    print(max( abs(a[n-1]-w), abs(a[n-2]-a[n-1])))
###

n, z, w = map(int, input().split())
a = [int(x) for x in input().split()]
 
if n == 1:
    print(abs(a[0]) - w)
else:
    print(max(abs(a[n-2]-a[n-1]), abs(a[n-1]-w)))

