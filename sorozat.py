import random
lotto = []
def lottoszamok():
    i = 0
    lista = ""

    while i <= 4:
        vel = int(random.random() * 90) + 1
        lotto.append(vel)
        if i == 4:
            lista += str(vel) + ""
        else:
            lista += str(vel) + ";"
        i += 1
    return lista


def egyjegyuek_szama():
    i = 0
    darab = 0
    while i < len(lotto):
        if lotto[i] < 10:
            darab += 1
        i += 1
    file_kiir(darab)
    return darab


def file_kiir(darab):
    fajl = open("szamok.txt", "w", encoding="utf-8")
    beir = darab
    fajl.write(f"II/F: \n \t Az egyjegyűek száma: {beir} ")
    fajl.close()

