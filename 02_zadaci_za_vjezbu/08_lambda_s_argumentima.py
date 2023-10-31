def primjena_lambde(lambda_funkciju, lista_brojeva):
    rezultati = []
    for broj in lista_brojeva:
        rezultat = lambda_funkciju(broj)
        rezultati.append(rezultat)
    return rezultati

# Primjer lambda funkcije: kvadriranje broja
kvadriraj = lambda x: x**2

# Ili recimo podijeli s 3
div_by_3 = lambda x: x/3

# Primjer liste brojeva
brojevi = [1, 2, 3, 4, 5]

# Primjena funkcije na listu brojeva koristeći lambda funkciju kvadriraj
rezultati = primjena_lambde(kvadriraj, brojevi)

print(rezultati)  # Ispis: [1, 4, 9, 16, 25]

# Primjena funkcije na listu brojeva koristeći lambda funkciju div_by_3
rezultati = primjena_lambde(div_by_3, brojevi)

for broj in rezultati:
    print(round(broj,2))

# Primjena funkcije na listu brojeva koristeći lambda funkciju definiranu u pozivu
rezultati = primjena_lambde(lambda x: x+10, brojevi)

print(rezultati)  # Ispis: [11, 12, 13, 14, 15]


### Dodatni primjeri za lambde

lista_stringova = ["1", "2", "9", "0", "-1", "-2"]
# sorted() prima 2 argumenta, listu i ključ za sortiranje
# pod " key = " dajemo lambda izraz jer prvo moramo naše stringove pretvoriti u brojese s funkcijom int()

print("Sorted numerically:",
	sorted(lista_stringova, key=lambda x: int(x)))

### Filtriranje liste pomoću lambda izraza
# Koristimo funkciju filter()
#   - prvi argument koji dajemo je LAMBDA izraz po kojem ćemo filtrirati vrijednosti
#   - drugi argument je lista koju filtriramo (lista_stringova)
#   - s obzirom da smo stavili keyword "not" ispred izraza "(int(x) % 2 == 0 and int(x) > 0)"
#     izbacujemo sve brojeve koji su parni i veći od nule
filtered_numbers = list(
    filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0)
           , lista_stringova)
        )

print("Filtered positive even numbers:", filtered_numbers)

### Editiranje liste pomocu lambde
# keyword "map" izvršava neku operaciju nad svim elementima dane liste
#   - " lambda x: str(int(x) + 10) " , ovim izrazom svakom broju dodajemo +10 i onda ga vraćamo nazad u tip string s str()

print("Operation on each item using lambda and map()",
	list(map(lambda x: str(int(x) + 10), lista_stringova)))

