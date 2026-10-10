from daftar_film import Film, FilmManager

pengelola = FilmManager()

film1 = Film("Interstellar", "Sci-Fi", 2014, 9.0)
film2 = Film("Spirited Away", "Animation", 2001, 8.5)

pengelola.tambah_film(film1)
pengelola.tambah_film(film2)

pengelola.tampilkan_film()
