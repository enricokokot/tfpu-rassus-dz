# Napišite lambda funkciju koja računa umnožak dva broj

# Lambdu spremimo u varijablu koju cemo onda kasnije pozivati
umnozak = lambda x, y: x * y
# Vrijednost spremimo u rezultat prije ispisa u terminal
rezultat= umnozak(5,3)
print("Verzija 1 : rezultat =" , rezultat)

# Rezultat računamo prilikom poziva ispisa
print("Verzija 2 : rezultat =" ,umnozak(3,3))

# Samu LAMBDU definiramo prilikom ispisa
print("Verzija 3 : rezultat =",(lambda x,y:x*y)(9,3))
