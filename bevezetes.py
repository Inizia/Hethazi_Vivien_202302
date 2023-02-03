def adatbeker():
    i = 0
    nev = input(f"I/A: \n \t Autó neve: ")
    ev = int(input(f"\t Gyártási dátum: "))

    if ev >= 2023:
        print(f"I/B \n \t Ez az {nev} friss gyártás.")
    elif ev < 2000:
        print(f"I/B \n \t Ez az {nev} öreg autó.")
    else:
        print(f"I/B \n \t Ez az {nev} átlagos korú.")