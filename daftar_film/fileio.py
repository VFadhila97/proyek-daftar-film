from .validasi import validasi_film, FilmTidakValidError

FILE_DATA = "data_film.txt"

def siapkan_file():
    try:
        with open(FILE_DATA, "x", encoding="utf-8") as file:
            pass
    except FileExistsError:
        pass
    
def simpan_film(film):
    validasi_film(
        film.judul, film.genre, film.tahun, film.rating
    )

    with open(FILE_DATA, "a", encoding="utf-8") as file:
        file.write(
            f"{film.judul}|{film.genre}|"
            f"{film.tahun}|{film.rating}\n"
        )

def baca_film():
    daftar = []

    try:
        with open(FILE_DATA, "r", encoding="utf-8") as file:
            for baris in file:
                try:
                    bagian = baris.strip().split("|")

                    if len(bagian) != 4:
                        raise ValueError("Format data tidak sesuai.")

                    judul, genre, tahun, rating = bagian

                    tahun = int(tahun)
                    rating = float(rating)

                    validasi_film(judul, genre, tahun, rating)

                    daftar.append({
                        "judul": judul,
                        "genre": genre,
                        "tahun": tahun,
                        "rating": rating
                    })

                except (ValueError, FilmTidakValidError) as error:
                    print(f"Data dilewati: {error}")

    except FileNotFoundError:
        print("File data film belum ditemukan.")

    return daftar