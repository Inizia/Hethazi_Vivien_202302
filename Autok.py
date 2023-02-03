class Autok:
    def __init__(self, sorok):
        self.nev = sorok[0]
        self.datum = int(sorok[1])

    def __str__(self):
        return f"{self.nev}, {self.datum}"