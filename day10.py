class Kendaraan:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun

    def deskripsi(self):
        return f"{self.tahun} {self.merk} {self.model}"

    def nyalakan_mesin(self):
        return f"Mesin {self.merk} {self.model} dinyalakan."

    def matikan_mesin(self):
        return f"Mesin {self.merk} {self.model} dimatikan."


class Mobil(Kendaraan):
    def __init__(self, merk, model, tahun, jumlah_pintu):
        super().__init__(merk, model, tahun)
        self.jumlah_pintu = jumlah_pintu

    def deskripsi(self):
        return f"{self.tahun} {self.merk} {self.model} dengan {self.jumlah_pintu} pintu"

    def buka_bagasi(self):
        return "Bagasi dibuka."

    def tutup_bagasi(self):
        return "Bagasi ditutup."


class Motor(Kendaraan):
    def __init__(self, merk, model, tahun, tipe_motor):
        super().__init__(merk, model, tahun)
        self.tipe_motor = tipe_motor

    def deskripsi(self):
        return f"{self.tahun} {self.merk} {self.model}, tipe {self.tipe_motor}"

    def standarkan_motor(self):
        return "Motor di standarkan."

    def lipat_standar(self):
        return "Standar motor dilipat."


mobil_saya = Mobil("Honda", "Civic", 2023, 4)
print(mobil_saya.deskripsi())
print(mobil_saya.nyalakan_mesin())
print(mobil_saya.buka_bagasi())
print(mobil_saya.tutup_bagasi())
print(mobil_saya.matikan_mesin())

print() 

motor_saya = Motor("Honda", "Scoopy", 2017, "Matic")
print(motor_saya.deskripsi())
print(motor_saya.nyalakan_mesin())
print(motor_saya.standarkan_motor())
print(motor_saya.lipat_standar())
print(motor_saya.matikan_mesin())
