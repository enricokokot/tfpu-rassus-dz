
# Python automatski prepoznaje tip podatka.

ime = "Ana"  # (string)
godine = 25  #  (integer)
visina = 1.75  # (float)
je_student = True  # boolean vrijednost (True/False)
lista_brojeva = [3, 7, 9]  # list
mixed_lista = [3,"pet",9,15.3]
osobni_podaci = {'ime': 'Ana', 'prezime': 'Horvat'}  # rječnik
osobni_podaci_student = {'ime': 'Ana', 'prezime': 'Horvat', 'JMBAG' : 1253339599}

print(osobni_podaci_student)
print(mixed_lista)
print("Ime",ime,"ima ",len(ime)," slova")

# Types

print("Ime je type =",type(ime))

# Ispis
ime = "Marko"
godina_studija = 3

print("Moj kolega se zove", ime, "i trenutno je na", godina_studija,"godini studija.")
# f-string za formatirani ispis:
print(f"Moj prijatelj se zove {ime} i trenutno je na {godina_studija} godini studija.")

# Ovo je jednolinijski komentar
ime = "Iva"  # Postavljanje imena

"""
Ovo je
višelinijski komentar.
Možete koristiti trostruke navodnike za više linija komentara.
"""

