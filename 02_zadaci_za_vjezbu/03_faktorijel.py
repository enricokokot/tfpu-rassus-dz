# isto moguce rijesiti rekurzijom
def faktorijel(n):
    if n == 0:
        return 1
    else:
        return n * faktorijel(n - 1)


def faktorijel_loop(n):
    fakt = 1
    for i in range(1, n + 1):
        fakt *= i
        # isto kao fakt = fakt * i
    return fakt

# Izračun faktorijela broja 5 ( rekurzija )
rezultat = faktorijel(5)
print("(REKURZIJA) Faktorijel broja 5 je:", rezultat)


# Izračun faktorijela broja 5 ( loop )
rezultat = faktorijel_loop(5)
print("(LOOP) Faktorijel broja 5 je:", rezultat)

