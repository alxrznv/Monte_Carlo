import math
import random
size = int(input("Введите количество точек: "))
m = 0
n = 0
for i in range(size):
    x = random.random()
    y = random.random()
    if ((x ** 2 + y ** 2) <= 1):
        n += 1
pi = 4*n/size
print(pi, math.pi, size)