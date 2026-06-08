from HEWAN import Hewan, HewanTerbang

class Burung(HewanTerbang):
    def __init__(self, nama, jenis):
        super().__init__()
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan biji-bijian.")

    def terbang(self):
        print(f"{self.nama} sedang terbang di udara.")

class Ikan(Hewan):
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan pelet ikan.")