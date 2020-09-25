# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# Si listamos los numeros naturales debajo de 10 que son multiplos de 3 o 5, tendriamos 3, 5, 6 y 9. La suma de estos multiplos es 23.
#Encuentra la suma de todos los multiplos de 3 y 5 debajo de 1000.

r = 0
for n in range(1000):
    if (n%3 == 0 or n%5 == 0):
        r = r + n
print(r)