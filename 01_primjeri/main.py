bodovi = [80, 73, 61, 95, 41, 31]

bodovi.append(100)
bodovi.append(22)

print(bodovi)

novi_bodovi = []
for bod in bodovi:
    if bod % 2 == 0:
        novi_bodovi.append(bod)

print(novi_bodovi)

for bod in bodovi:
    if bod < 40:
        bodovi.remove(bod)

print(bodovi)

for bod in bodovi:
    if bod >= 90 and bod <= 100:
        print(bod, " = Odličan")
    elif bod >= 80:
        print(bod, " = Vrlo dobar")
    elif bod >= 65:
        print(bod, " = Dobar")
    elif bod >= 50:
        print(bod, " = Dovoljan")
    else:
        print(bod, " = Nedovoljan")


knjiznica = {
    'Harry Potter': {'autor': 'J.K. Rowling', 'godina': 2001, 'dostupno': 5},
    'Lord of the Rings': {'autor': 'J.R.R. Tolkien', 'godina': 1954, 'dostupno': 3}
}

knjiznica["Witcher"] = {'autor': "Andrzej Sapkowski", 'godina': 1994, 'dostupno': 0}

for naslov, knjiga in knjiznica.items():
    print(f"Naslov: {naslov}, Autor: {knjiga['autor']}, Godina: {knjiga['godina']}, Dostupno: {knjiga['dostupno']} primjeraka")

# del knjiznica['Witcher']

# for naslov, knjiga in knjiznica.items():
#     print(f"Naslov: {naslov}, Autor: {knjiga['autor']}, Godina: {knjiga['godina']}, Dostupno: {knjiga['dostupno']} primjeraka")

for naslov, knjiga in knjiznica.items():
    if knjiga['dostupno'] > 0:
        print(f"Naslov {naslov} je dostupan!")
    else:
        print(f"Naslov {naslov} nije dostupan!")

lista_brojeva = [x for x in range(1, 101)]
print(lista_brojeva)

filtrirani_brojevi = [broj for broj in lista_brojeva if broj >= 49 and broj <= 80]
print(filtrirani_brojevi)

studenti = {
    "Ana": 100,
    "Marko": 25,
    "Petra": 49,
    "Ivan": 56,
    "Mia": 89,
    "Lovro": 80,
    "Stipe":73,
    "Lea":60,
    "Tomislav":51,
    "Leo":99
}
filtrirani_studenti = {ime: student for ime, student in studenti.items() if len(ime) > 3 and student >= 50}
print(filtrirani_studenti)
