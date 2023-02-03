from Autok import Autok
auto_lista = []

def file_beolvas():
    f = open("auto.txt", "r", encoding="utf-8")
    f.readline()
    lista = f.readlines()
    f.close()

    print(lista)

    i = 0
    while i < len(lista):
        sor = lista[i].strip().split("$")
        print(sor)
        auto_lista.append(Autok(sor))
        i += 1


def autok_szama():
    i = 0
    darab = 0
    while i < len(auto_lista):
        ev = auto_lista[i].datum
        if (ev[0]) > 0:
            darab += 1
        i += 0
    return darab

