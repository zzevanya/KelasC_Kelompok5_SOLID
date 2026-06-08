from KANDANG import Kandang
from HEWAN import HewanTerbang

class KebunBinatang:
    def _init_(self):
        self.daftar_kandang = []

    def tambah_kandang(self, kandang: Kandang):
        self.daftar_kandang.append(kandang)

    def rawat_semua_hewan(self):
        for kandang in self.daftar_kandang:
            for hewan in kandang.hewan_list:
                hewan.makan()
                if isinstance(hewan, HewanTerbang):
                    hewan.terbang()