# Napišite lambda funkciju za izračunavanje vrijednosti kvadratne funkcije za zadane ulaze. 
# Program treba koristiti lambda funkciju kako bi izračunao vrijednost funkcije za zadani 
# ulaz x prema formuli f(x) = 2x^2 + 3x + 1

# Lambdu spremimo u varijablu koju cemo onda kasnije pozivati
funkcija = lambda x: 2*(x*x)+3*x+1
# Vrijednost spremimo u rezultat prije ispisa u terminal
rezultat= funkcija(3)
print("Verzija 1 : rezultat =" , rezultat)

# Rezultat računamo prilikom poziva ispisa
print("Verzija 2 : rezultat =" ,funkcija(3))

# Samu LAMBDU definiramo prilikom ispisa
print("Verzija 3 : rezultat =",(lambda x:2*(x*x)+3*x+1)(3))
