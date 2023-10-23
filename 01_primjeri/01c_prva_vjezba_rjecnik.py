## Stvaranje rječnika
student = {
    'ime': 'Ivan',
    'prezime': 'Antic',
    'ocjena': 4
}

# Pristupanje vrijednostima prema ključu
ime_studenta = student['ime']
ocjena_studenta = student['ocjena']

# Ispis imena i ocjene studenta
print("Ime studenta =", ime_studenta)
print("Ocjena studenta =", ocjena_studenta)

## Dodavanje novog para ključ-vrijednost
student['grad'] = 'Zagreb'

# Dodavanje više informacija u rječnik koristeći update metodu
student.update({'smjer': 'Informatika', 'status': 'redovni'})

print("Student =", student)

# Promjena ocjene studenta
student['ocjena'] = 5

# Ispis promijenjenog rječnika
print("After : student =", student)


# Brisanje ključa 'grad' i njegove vrijednosti
del student['grad']
print("After : student =", student)

# Brisanje ključa 'godine' i povrat uklonjene vrijednosti
popped = student.pop('ocjena')

print("Uklonjeno:", popped)
print(student)

# Uklanjanje i povrat zadnjeg para ključ-vrijednost
kljuc, vrijednost = student.popitem()

print("Uklonjeno:", kljuc, vrijednost)
#print(student)

## Slozeniji rjecnik

zapis_studenta = {
    '024333':{'ime':'Ivan','prezime':'Pantić','studij':'informatika'},
    '333555':{'ime':'Mate','prezime':'Mišo','studij':'ekonomija'}
}

print(zapis_studenta['024333']['ime'])

# Dodavanje

zapis_studenta['888999'] = {'ime':'Lea','prezime':'Lerko','studij':'računarstvo'}

print(zapis_studenta)

# Brisanje

del zapis_studenta['024333']

print(zapis_studenta)

## Provjera vrijednosti
# Koji je studij student s JMBAG 888999? 
studij = zapis_studenta['888999']['studij']
print("Studij =",studij)
