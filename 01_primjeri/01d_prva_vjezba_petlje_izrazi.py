# Ispis brojeva od 1 do 5 koristeći for petlju
for broj in range(6):
    print("Broj =",broj)


print()
print("----Nova Petlja----")
for broj in range(1,6):
    print(broj, end=' ')

# Ispis stringova iz liste

popis_studenata =["Ivo","Vojko","Zoni","Krešo"]

for student in popis_studenata:
    print("Student =", student)

for slovo in 'student':
    print("Slovo =", slovo)

for pozicija,student in enumerate(popis_studenata):
    print("Student broj",pozicija," se zove ",student)

# Ispis iz rijecnika
print("----Ispis iz rijecnika----")
student = {
    'ime': 'Ivan',
    'prezime': 'Antic',
    'ocjena': 4
}

for kljuc in student:
    print("Ključ =", kljuc)





for kljuc,vrijednost in student.items():
    print(f'{kljuc}: {vrijednost}')

# Provjera je li broj paran ili neparan
broj = 7

if broj % 2 == 0:
    print(f"{broj} je paran broj.")
else:
    print(broj," je neparan broj.")

# Provjera tipa
ime = 'Vojko'
print("Je li Ime '",ime,"' IsInstance of Integer? =", isinstance(ime, int))
print("Je li Ime '",ime,"' IsInstance of String? =", isinstance(ime, str))

# Provjera vise uvjeta

ocjena = 85

if ocjena >= 90:
    print("Ocjena: A")
elif ocjena >= 80:
    print("Ocjena: B")
elif ocjena >= 70:
    print("Ocjena: C")
elif ocjena >= 60:
    print("Ocjena: D")
else:
    print("Ocjena: F")


# Kombinacija

for broj in range(1,20):
    if broj % 2 == 0:
        print("Broj je paran = " ,broj)
    else:
        print("Broj je neparan = ",broj)

for broj in range(1,20):
    if broj % 2 == 0 and broj < 15 :
        print("Broj je paran = " ,broj)
    else:
        print("Broj nam nije zanimljiv = ",broj)

## continue , pass , break

# Continue
print("-----Continue-----")
popis_voca = ["jabuka", "banana", "nektarina"]
for voce in popis_voca:
  if voce == "banana":
    continue
  print("Voce =",voce)

# Pass
print("-----Pass-----")
for voce in popis_voca:
  if voce == "banana":
    pass
  print("Voce =",voce)

# Break
print("-----Break-----")
for voce in popis_voca:
  if voce == "banana":
    break
  print("Voce =",voce)
print("Van loop-a sam")


