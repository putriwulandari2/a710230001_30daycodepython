class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def deskripsi(self):
        return f"Hewan ini adalah seekor {self.jenis} bernama {self.nama}."

hewan1 = Hewan("Kucing", "Mamalia")
hewan2 = Hewan("Burung", "Aves")

print(hewan1.deskripsi())
print(hewan2.deskripsi())
