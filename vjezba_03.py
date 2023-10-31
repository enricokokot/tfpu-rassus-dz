#1
def filtriranje_liste(lista_brojeva):
    filtrirani_brojevi = list(filter(lambda x: x % 2 == 0, lista_brojeva))
    kvadrirani_brojevi = list(map(lambda x: x*x, filtrirani_brojevi))
    sortirani_brojevi = sorted(kvadrirani_brojevi, key=lambda x: int(x))
    return sortirani_brojevi

ulazna_lista = [25, 22, 13, 44, 51, 36, 77, 18, 99, 16]
print(filtriranje_liste(ulazna_lista))

#2
def count_letter(rijec, slovo):
    lowercase_rijec = rijec.lower()
    brojac = 0
    for lowercase_slovo in lowercase_rijec:
        if lowercase_slovo == slovo.lower():
            brojac += 1
    return f"Slovo '{slovo}' pojavljuje se {brojac} puta u riječi ili frazi: '{rijec}'"

print(count_letter("Rano Raniti je Super", "R"))
print(count_letter("Riječ", "R"))

#3
stringovi = ["banana", "jabuka", "kruška", "naranča", "limun"]
trazeni_znak = 'a'

rezultat = list(filter(lambda x: trazeni_znak in x, stringovi))
print(rezultat)

#4
brojevi = [2,3,6,10,12,4,13,16,7]
kvadrirani_brojevi = list(map(lambda x: x*x, brojevi))
print(kvadrirani_brojevi)
filtrirani_brojevi = list(filter(lambda x: not x % 2 == 0 and x < 100, kvadrirani_brojevi))
print(filtrirani_brojevi)