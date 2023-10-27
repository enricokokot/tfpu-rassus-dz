def pozdrav(a, b="default"):
    return a * 2, b * 2


pozdrav2 = lambda a, b=0: (a * 2, b * 2)

print(pozdrav2(1, 2))
print(pozdrav2(1))


f_x = lambda x: 2 * x**2 + 3 * x + 1


primjer = [2 * x for x in range(10)]
primjer4 = [4 * x for x in primjer]

print(primjer)
print(primjer4)
