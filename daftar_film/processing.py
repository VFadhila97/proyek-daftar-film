from .fileio import baca_film
from .validasi import validasi_film


def hitung_rata_rata(*nilai):
    if not nilai:
        return 0

    assert all(0 <= n <= 10 for n in nilai)

    return sum(nilai) / len(nilai)

class Film:
    def __init__(self, judul, genre, tahun, rating):
        validasi_film(judul, genre, tahun, rating)

        self.judul = judul
        self.genre = genre
        self.tahun = tahun
        self.rating = rating


class FilmManager:
    def __init__(self):
        self.daftar = []

    def tambah_film(self, film):
        self.daftar.append(film)

    def tampilkan_film(self):
        for film in self.daftar:
            print(
                f"{film.judul} | {film.genre} | "
                f"{film.tahun} | {film.rating}"
            )

    def hitung_statistik(self):
        jumlah = len(self.daftar)
        rata_rata = hitung_rata_rata(
            *(film.rating for film in self.daftar)
        )

        return {
            "jumlah": jumlah,
            "rata_rata": rata_rata
        }

    def urutkan_film(self, terbalik=False):
        return sorted(
            self.daftar,
            key=lambda film: film.rating,
            reverse=terbalik
        )

    def buat_laporan(self):
        statistik = self.hitung_statistik()

        with open("laporan_film.txt", "w", encoding="utf-8") as file:
            file.write("LAPORAN DAFTAR FILM\n")
            file.write("===================\n")
            file.write(f"Jumlah film: {statistik['jumlah']}\n")
            file.write(
                f"Rata-rata rating: "
                f"{statistik['rata_rata']:.2f}\n"
            )

        print("Laporan berhasil dibuat: laporan_film.txt")

def buat_film(**kwargs):
    return Film(**kwargs)

if __name__ == "__main__":
    film = buat_film(
        judul="Interstellar",
        genre="Sci-Fi",
        tahun=2014,
        rating=9.0
    )

    pengelola = FilmManager()
    pengelola.tambah_film(film)
    pengelola.tampilkan_film()
