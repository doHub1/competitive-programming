# 数字複数
x, y,z = map(int, input().split())

arr = [x,y,z]

arr.sort()
arr.reverse()

#print(arr)

print(arr[0]*10+arr[1]+arr[2])


