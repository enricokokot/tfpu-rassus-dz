# List comprehensions

# Stvori listu s brojevima iz range()
lista = [x for x in range(10)]
# Ispis: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Stvori listu brojeva koji su parni iz range()

lista_parnih = [x for x in range(20) if x%2 == 0 ]
print("Lista parnih =",lista_parnih)

# Stvori listu brojeva koji su parni iz range() i manji od 13
lista_parnih_dodatno = [x for x in range(20) if x % 2 == 0 and x < 13]
print("lista_parnih_dodatno = ",lista_parnih_dodatno)

# Stvori listu brojeva koji su kvadrat parnih vrijednosti 

lista_kvadrata = [x*x for x in range(10) if x%2 == 0]
# ili 
lista_kvadrata = [x**2 for x in range(10) if x%2 == 1]
print(lista_kvadrata)

imena = ["Ana", "Marko", "Petra", "Ivan", "Mia"]

imena_vise_od_3_slova = [ime for ime in imena if len(ime) > 3]
print("Nova lista = ", imena_vise_od_3_slova)

## Rječnik

kvadrati_dict = {broj: broj ** 2 for broj in range(1, 6)}
print(kvadrati_dict)

kvadrati_dict = {broj: broj ** 2 for broj in range(1, 6) if broj%2 ==1}
print(kvadrati_dict)


studenti = {
    "Ana": 1,
    "Marko": 2,
    "Petra": 4,
    "Ivan": 5,
    "Mia": 5,
    "Lovro": 3
}

filtrirani_studenti = {ime: ocjena for ime, ocjena in studenti.items() if ocjena >= 3}

print("Filtrirani studenti =",filtrirani_studenti)
