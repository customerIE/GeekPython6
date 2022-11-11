#5. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.
a = [1.04, 45.24, 2.12, 345.77, 21.15]
temp = 0
#b = []
#for i in range(len(a)):
#    temp = a[i] - int(a[i])
#    b.append(temp)
b = [a[i] - int(a[i]) for i in range(len(a))]
print(b)
max = b[0]
min = b[0]
for i in range(1, len(b)):
    if b[i]>max:
        max = b[i]
    if b[i]<min:
        min = b[i]
defference = max - min
print('Максимальное значение дробной части =', round(max, 3))
print('Минимальное значение дробной части =', round(min,3))
print('Разницу между max и min дробной части = ', round(defference, 3))