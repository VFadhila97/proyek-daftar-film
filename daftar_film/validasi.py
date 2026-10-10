class FilmTidakValidError(Exception):
    pass

def validasi_film(judul, genre, tahun, rating):
    if not judul.strip() or not genre.strip():
        raise FilmTidakValidError("Judul dan genre tidak boleh kosong.")
    if tahun <= 0:
        raise FilmTidakValidError("Tahun harus lebih dari 0.")
    if not 0 <= rating <= 10:
        raise FilmTidakValidError("Rating harus antara 0 dan 10.")

    return True
