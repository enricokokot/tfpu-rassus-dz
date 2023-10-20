def funkcija_bez_parametara():
    print("Dobrodošli u Python!")

# funkcija_bez_parametara()


def pozdrav(ime, vrijeme_dana="jutro"):
    if vrijeme_dana in ["podne", "popodne"]:
        print(f"Dobar dan, {ime}")
    elif vrijeme_dana == "večer":
        print(f"Dobro večer, {ime}")
    else:
        print(f"Dobro jutro, {ime}")

# pozdrav(12)
# pozdrav("Mia")
# pozdrav(13, "sječanj")
# pozdrav(15, "popodne")


def faktorijel(n):
    baza = 1
    for broj in range(1, n+1):
        baza = baza * broj
    return baza

# for i in range(11):
#     print(f"{i}! = {faktorijel(i)}")


def kalkulator(broj_1, broj_2, operacija):
    rezultat = eval(f"{broj_1} {operacija} {broj_2}")
    return rezultat

# print(kalkulator("1", "2", "/"))


def calculate(varijabla_1, varijabla_2):
    return (varijabla_1 + varijabla_2, varijabla_1 - varijabla_2)

# x = 12
# y = 14
# print(calculate(x, y))


umnozak = (lambda broj_1, broj_2: broj_1 * broj_2)

# print(umnozak(10, 33))


izracunavanje_vrijednosti_kvadratne_funkcije = (lambda x: 2 * x**2 + 3*x + 1)

# print(izracunavanje_vrijednosti_kvadratne_funkcije(3))


def primjena_lambde(lambda_funkcija, lista_brojeva):
    nova_lista = [lambda_funkcija(broj) for broj in lista_brojeva]
    return nova_lista

# print(primjena_lambde(
#     izracunavanje_vrijednosti_kvadratne_funkcije, [0, 1, 2, 3, 4, 5]))
