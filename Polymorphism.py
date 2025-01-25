class Hewan:
    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        return "Meow"

class Anjing(Hewan):
    def suara(self):
        return "Guk"

# Polymorphism
hewan1 = Kucing()
hewan2 = Anjing()

for hewan in (hewan1, hewan2):
    print(hewan.suara())
