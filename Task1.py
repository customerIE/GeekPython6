#1. Задайте список из n чисел последовательности (1 + 1/n)^n
# и выведите на экран их сумму.
from functools import reduce
n = int(input('Введите число n: '))
#a=[]
#sum = 0
#for i in range(1,n+1):
#    a.append((1+1/i)**i)
#print(a)
#for i in range(n):
#    sum = sum +a[i]
#print('Сумма чисел = ', sum)
a=[(1+1/i)**i for i in range(1,n+1)]
print('Список чисел: ',a)
b = reduce(lambda x,y: x+y, a)
print('Сумма чисел: ',b)