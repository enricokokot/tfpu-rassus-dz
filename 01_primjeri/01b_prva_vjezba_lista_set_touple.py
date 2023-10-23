## Stvaranje i pristupanje elementima lista:

# Stvaranje liste
brojevi = [1, 2, 3, 4, 5]
neki_stringovi = ['a','b','ccc','primjer']


# Pristupanje elementima niza prema indeksu
prvi_element = brojevi[0]  # Prvi element
drugi_element = brojevi[1]  # Drugi element

# Ispis prvog i drugog elementa
print("Prvi element =", prvi_element)
print("Drugi element =", drugi_element)

string_jedan = neki_stringovi[2]
string_dva = neki_stringovi[3]

print(f'String_jedan = {string_jedan}')
print(f'String_dva = {string_dva}')


## Dodavanje 

# append()
print('Before : brojevi = ', brojevi)
brojevi.append(6)
print('After : brojevi = ', brojevi)


# insert()
print('Before : brojevi = ', brojevi)
brojevi.insert(1, 100)
print('After : brojevi = ', brojevi)

print('Before : brojevi = ', brojevi)
brojevi.insert(0, 200)
print('After : brojevi = ', brojevi)

print('Before : brojevi = ', brojevi)
brojevi.insert(-1, 200)
print('After : brojevi = ', brojevi)

## Brisanja

# clear()

brojevi.clear()
print("Brojevi =",brojevi)

# pop() , remove by index and return it's value

brojevi = [1, 2, 3, 4, 5]

popped = brojevi.pop(0) # izbacujemo 1 i vracamo vrijednost u varijablu
print("Brojevi =",brojevi)
print("Popped =",popped)

popped = brojevi.pop(3)
print("Brojevi =",brojevi)
print("Popped =",popped)

# pop() , negative index

brojevi = [1, 2, 3, 4, 5]
popped = brojevi.pop(-1) # izbacujemo zadnji element
print("Brojevi =",brojevi)
print("Popped =",popped)

# remove(), delete item by "value"

lista_imena = ['Matej', 'Ivan', 'Teo', 'Ana', 'Lea', 'Teo']

print("Before : Lista imena =",lista_imena)
lista_imena.remove('Teo')   # miče samo pronađeni element u listi
print("After : Lista imena =",lista_imena)

brojevi = [2, 1, 3, 4, 5]
print("Before : Brojevi =",brojevi)
brojevi.remove(1)
print("After : Brojevi =",brojevi)


## Set

set_vrijednosti = {1,2,2,3,4,5,6}
print("Set_vrijednosti =",set_vrijednosti)
set_vrijednosti.add(6)
set_vrijednosti.add(7)
print("Set_vrijednosti =",set_vrijednosti)

# Touple

touple_vrijednost = (1,"pet",15.3,"rijec")
print("Touple_vrijednost =",touple_vrijednost)
touple_vrijednost.add(6)

