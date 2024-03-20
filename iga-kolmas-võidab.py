from random import randint
limonaad = int(input("Sisesta, mitu limonaadipudelit ostad: "))
võit = ("Osteti limonaad, millega võideti uus limonaad!")
tõenäosus = 67
võidetud = 0
i = 0
while i < limonaad:
    if randint(1, 100) <= tõenäosus:
        print("Osteti limonaad")
    else:
        print(võit)
        võidetud += 1 
    i += 1
print("Kokku võideti " + str(võidetud) + " limonaadi!")