import unittest

from .processing import Film, FilmManager
from .validasi import FilmTidakValidError

class TestDaftarFilm(unittest.TestCase):
    def setUp(self):
        self.pengelola = FilmManager()
        self.film1 = Film("Interstellar", "Sci-Fi", 2014, 9.0)
        self.film2 = Film("Spirited Away", "Animation", 2001, 8.0)

    def test_tambah_film(self):
        self.pengelola.tambah_film(self.film1)
        self.assertEqual(len(self.pengelola.daftar), 1)

    def test_judul_kosong(self):
        with self.assertRaises(FilmTidakValidError):
            Film("", "Sci-Fi", 2014, 9.0)

    def test_rating_tidak_valid(self):
        with self.assertRaises(FilmTidakValidError):
            Film("Film Uji", "Drama", 2020, 15.0)

    def test_hitung_statistik(self):
        self.pengelola.tambah_film(self.film1)
        self.pengelola.tambah_film(self.film2)

        statistik = self.pengelola.hitung_statistik()

        self.assertEqual(statistik["jumlah"], 2)
        self.assertEqual(statistik["rata_rata"], 8.5)

    def test_urutkan_film(self):
        self.pengelola.tambah_film(self.film2)
        self.pengelola.tambah_film(self.film1)

        hasil = self.pengelola.urutkan_film(terbalik=True)

        self.assertEqual(hasil[0].judul, "Interstellar")
        self.assertEqual(hasil[1].judul, "Spirited Away")

if __name__ == "__main__":
    unittest.main()