from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama, jenis):
        self.nama=nama
        self.jenis=jenis
        
    @abstractmethod    
    def makan(self):
        pass
    
class HewanTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass