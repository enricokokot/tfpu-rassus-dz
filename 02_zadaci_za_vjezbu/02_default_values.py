def pozdrav(ime, vrijeme_dana="jutro"):
    if vrijeme_dana == "jutro":
        poruka = f"Dobro jutro, {ime}!"
    elif vrijeme_dana == "popodne":
        poruka = f"Dobar dan, {ime}!"
    else:
        poruka = f"Pozdrav, {ime}!"

    return poruka

# Primjeri pozivanja funkcije
print(pozdrav("Ana"))  # Ispis: "Dobro jutro, Ana!"
print(pozdrav("Marko", "večer"))  # Ispis: "Pozdrav, Marko!"
print(pozdrav("Marko", "popodne"))  # Ispis: "Dobar dan, Marko!"

