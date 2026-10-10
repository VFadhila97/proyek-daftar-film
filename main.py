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
    print("3. Statistik film")
    print("4. Urutkan film berdasarkan rating")
    print("5. Buat laporan")
    print("6. Keluar")

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
            print("Tahun harus bilangan bulat dan rating harus angka.")

        except FilmTidakValidError as error:
            print(f"Data tidak valid: {error}")

    elif pilihan == "2":
        pengelola.tampilkan_film()

    elif pilihan == "3":
        statistik = pengelola.hitung_statistik()
        print(f"Jumlah film: {statistik['jumlah']}")
        print(f"Rata-rata rating: {statistik['rata_rata']:.2f}")

    elif pilihan == "4":
        daftar_urut = pengelola.urutkan_film(terbalik=True)

        for film in daftar_urut:
            print(f"{film.judul} - Rating: {film.rating}")

    elif pilihan == "5":
        pengelola.buat_laporan()

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")