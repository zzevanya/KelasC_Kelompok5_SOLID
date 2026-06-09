from BINATANG import Burung, Ikan
from KANDANG import Kandang, BersihkanKandang
from KEBUN_BINATANG import KebunBinatang 

def main():
    ragunan = KebunBinatang()

    kandang_burung = Kandang("Kandang Avia")
    kandang_ikan = Kandang("Akuarium Besar")

    merpati = Burung("Merpati", "Aves")
    cupang = Ikan("Ikan Cupang", "Pisces")

    kandang_burung.tambah_hewan(merpati)
    kandang_ikan.tambah_hewan(cupang)

    ragunan.tambah_kandang(kandang_burung)
    ragunan.tambah_kandang(kandang_ikan)


    print("=== MERAWAT HEWAN ===")
    ragunan.rawat_semua_hewan()

    print("\n === MEMBERSIHKAN KANDANG ===")
    petugas = BersihkanKandang()
    petugas.bersihkan(kandang_burung)
    petugas.bersihkan(kandang_ikan)

if __name__ == "__main__":
    main()    
