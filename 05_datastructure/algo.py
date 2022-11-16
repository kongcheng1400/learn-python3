# insertion sort

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
    
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print('after sorting: ')
for i in range(len(arr)):
    print("%d" %arr[i], end=' ')

# fibonaci 
def recur_fibo(n):
   """递归函数
   输出斐波那契数列"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
 
 
# 获取用户输入
nterms = int(input("您要输出几项? "))
 
# 检查输入的数字是否正确
if nterms <= 0:
   print("输入正数")
else:
   print("斐波那契数列:")
   for i in range(nterms):
       print(recur_fibo(i), end = ' ')
print()
