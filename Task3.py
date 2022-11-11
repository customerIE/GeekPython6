#3. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
import random
from functools import reduce
#a = [2, 4, 6, 10, 7, 3, -3, 1]
#length = len(a)
#sum = 0
#for i in range(1, length, 2):
#    sum += a[i]
#print('Сумма элементов на нечетной позиции =', sum)
n= int(input('Введите кол-во эл-ов: '))
b = [random.randint(0, n) for i in range(n)]
print('Список чисел: ',b)    
c = reduce(lambda x,y: x+y ,b[1::2])
print('Сумма элем-ов на нечетных позициях: ', c)