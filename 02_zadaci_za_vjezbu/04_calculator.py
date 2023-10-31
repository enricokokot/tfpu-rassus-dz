def kalkulator(broj1, broj2, operacija):
    if operacija == "+":
        rezultat = broj1 + broj2
    elif operacija == "-":
        rezultat = broj1 - broj2
    elif operacija == "*":
        rezultat = broj1 * broj2
    elif operacija == "/":
        # Dodajemo dodatni case ako dijelimo s nulom
        if broj2 != 0:
            rezultat = broj1 / broj2
        else:
            return "Dijeljenje s nulom nije dopušteno."
    else:
        return "Nepodržana operacija"

    return rezultat

# Primjeri pozivanja funkcije
rezultat = kalkulator(5, 3, "+")  # Rezultat zbrajanja: 8
print("Rezultat je:", rezultat)

rezultat = kalkulator(5, 3, "-")  # Rezultat oduzimanja: 2
print("Rezultat je:", rezultat)

rezultat = kalkulator(5, 3, "*")  # Rezultat množenja: 15
print("Rezultat je:", rezultat)

rezultat = kalkulator(5, 0, "/")  # Dijeljenje s nulom
print("Rezultat je:", rezultat)

rezultat = kalkulator(5, 3, "^")  # Nepodržana operacija
print("Rezultat je:", rezultat)
