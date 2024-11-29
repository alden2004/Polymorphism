from abc import ABC, abstractmethod
from typing import List, Union

class AlatElektronik(ABC):
    def __init__(self, nama: str, daya: int = 100):
        """
        Konstruktor dasar untuk alat elektronik

        :param nama: Nama alat elektronik
        :param daya: Konsumsi daya dalam watt (default 100)
        """
        self.nama = nama
        self.daya = daya
        self.fitur = []

    @abstractmethod
    def aktifkan(self):
        """
        Metode abstrak untuk mengaktifkan alat
        Setiap jenis alat harus mengimplementasikan metode ini
        """
        pass

    def hitung_konsumsi_daya(self, jam: int) -> int:
        """
        Metode default untuk menghitung konsumsi daya

        :param jam: Jumlah jam penggunaan
        :return: Total konsumsi daya berdasarkan jam penggunaan
        """
        return self.daya * jam

    def tambah_fitur(self, fitur: Union[str, List[str]] = None):
        """
        Metode untuk menambah fitur dengan overloading sederhana

        :param fitur: Fitur tambahan (bisa string tunggal atau list)
        """
        if fitur is None:
            print("Tidak ada fitur tambahan")
            return

        if isinstance(fitur, str):
            self.fitur.append(fitur)
        elif isinstance(fitur, list):
            self.fitur.extend(fitur)

    def __str__(self):
        """
        Representasi string dari alat elektronik

        :return: Deskripsi alat
        """
        return f"{self.nama} (Daya: {self.daya}W)"


class Televisi(AlatElektronik):
    def __init__(self, daya: int = 100, ukuran: str = "32 inch"):
        """
        Konstruktor Televisi dengan overloading

        :param daya: Konsumsi daya
        :param ukuran: Ukuran layar televisi
        """
        super().__init__("Televisi", daya)
        self.ukuran = ukuran

    def aktifkan(self):
        """
        Implementasi metode aktifkan untuk Televisi
        Overriding metode abstrak dari kelas induk
        """
        print(f"{self.nama} ukuran {self.ukuran} telah dihidupkan.")

    def hitung_konsumsi_daya(self, jam: int) -> int:
        """
        Override metode hitung_konsumsi_daya
        Menambahkan faktor penggunaan TV

        :return: Total konsumsi daya yang disesuaikan
        """
        return super().hitung_konsumsi_daya(jam) + (20 * jam)  # Tambahan daya untuk speaker


class Kulkas(AlatElektronik):
    def __init__(self, daya: int = 150, tipe: str = "2 Pintu"):
        """
        Konstruktor Kulkas dengan overloading

        :param daya: Konsumsi daya
        :param tipe: Tipe kulkas
        """
        super().__init__("Kulkas", daya)
        self.tipe = tipe

    def aktifkan(self):
        """
        Implementasi metode aktifkan untuk Kulkas
        Overriding metode abstrak dari kelas induk
        """
        print(f"{self.nama} tipe {self.tipe} telah dihidupkan.")


# Demonstrasi Polymorfisme
def operasikan_alat(alat: List[AlatElektronik], jam: int):
    """
    Fungsi yang menunjukkan polymorfisme
    Dapat menerima berbagai jenis alat elektronik

    :param alat: Daftar alat elektronik
    :param jam: Jumlah jam penggunaan
    """
    for perangkat in alat:
        print(f"\n--- Mengoperasikan {perangkat.nama} ---")
        perangkat.aktifkan()
        print(f"Fitur: {perangkat.fitur}")
        print(f"Total Konsumsi Daya: {perangkat.hitung_konsumsi_daya(jam)} watt-jam")


# Contoh penggunaan
def main():
    # Membuat berbagai alat elektronik
    tv = Televisi()
    kulkas = Kulkas()

    # Menambah fitur
    tv.tambah_fitur(["Smart TV", "4K Resolution"])
    kulkas.tambah_fitur(["Ice Maker", "Energy Efficient"])

    # Operasikan alat dengan polymorfisme
    operasikan_alat([tv, kulkas], jam=5)

if __name__ == "__main__":
    main()