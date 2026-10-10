class Film:
    def __init__(self, judul, genre, tahun, rating):
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