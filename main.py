from daftar_film import Film, FilmManager
from daftar_film.fileio import siapkan_file, simpan_film, baca_film
from daftar_film.validasi import validasi_film, FilmTidakValidError

siapkan_file()
pengelola = FilmManager()

for data in baca_film():
    film = Film(
        data["judul"],
        data["genre"],
        data["tahun"],
        data["rating"]
    )
    pengelola.tambah_film(film)

while True:
    print("\n=== DAFTAR FILM ===")
    print("1. Tambah film")
    print("2. Tampilkan film")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        try:
            judul = input("Judul film: ")
            genre = input("Genre: ")
            tahun = int(input("Tahun rilis: "))
            rating = float(input("Rating (0-10): "))

            validasi_film(judul, genre, tahun, rating)

            film = Film(judul, genre, tahun, rating)
            simpan_film(film)
            pengelola.tambah_film(film)

            print("Film berhasil ditambahkan.")

        except ValueError:
            print("Tahun harus berupa bilangan bulat dan rating harus angka.")

        except FilmTidakValidError as error:
            print(f"Data tidak valid: {error}")

    elif pilihan == "2":
        pengelola.tampilkan_film()

    elif pilihan == "3":
        print("Program selesai.")
        break