# 翻转指定个数的元素
# 方法1
def leftRotateByOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def leftRotate(arr, d, n):
    for i in range(d):
        leftRotateByOne(arr, n)

arr = list(range(7))
print('方法1:')
print('before:', arr)
leftRotate(arr, 2, 7)
print('after:', arr)

# 方法2
print('\n\n方法2:')
def leftRotate2(arr, d, n):
    for i in range(d):
        temp = arr[0]
        arr.pop(0)
        arr.append(temp)
print('before:', arr)
leftRotate2(arr, 2, 7)
print('after:', arr)

# 方法3
def leftRotate3(arr, d):
    arr = arr[d:] + arr[:d]
    return arr
print('\n\n方法3:')
print('before:', arr)
print('after:', leftRotate3(arr, 2))