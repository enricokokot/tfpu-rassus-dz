def calculate(a, b):
    zbroj = a + b
    razlika = a - b
    return zbroj, razlika

# Primjer poziva funkcije
rezultat = calculate(5, 3)
# ili
zbroj,razlika = calculate(5,3)

# Ispis rezultata
print("Zbroj:", rezultat[0])
print("Razlika:", rezultat[1])

# Primjer2
print("VAR Zbroj:", zbroj)
print("VAR Razlika:", razlika)

