# Impordib randint funktsiooni moodulist random, et genereerida juhuslikke täisarve antud vahemikus
from random import randint
# Küsib kasutajalt, mitu limonaadipudelit ta soovib osta ja teisendab sisendi täisarvuks
limonaad = int(input("Sisesta, mitu limonaadipudelit ostad: "))
# Määratleb sõnumi, mida kuvada, kui võidetakse uus limonaad
võit = ("Osteti limonaad, millega võideti uus limonaad!")
# Määrab võidutõenäosuse protsentides
tõenäosus = 67
# Algväärtustab võidetud limonaadide loenduri nulliga
võidetud = 0
# Algväärtustab tsükli loenduri nulliga
i = 0
# Algab tsükkel, mis kestab kuni ostetud limonaadide arv on saavutatud
while i < limonaad:
    # Genereerib juhusliku arvu vahemikus 1 kuni 100 ja kontrollib, kas see on väiksem või võrdne võidutõenäosusega
    if randint(1, 100) <= tõenäosus:
        # Kui tingimus on tõene, prinditakse sõnum "Osteti limonaad"
        print("Osteti limonaad")
    else:
        # Kui tingimus on väär, prinditakse võidusõnum
        print(võit)
        # Suurendatakse võidetud limonaadide loendurit ühe võrra
        võidetud += 1
    # Suurendatakse tsükli loendurit ühe võrra
    i += 1
# Prinditakse lõppsõnum, mis näitab, mitu limonaadi kokku võideti
print("Kokku võideti " + str(võidetud) + " limonaadi!")
