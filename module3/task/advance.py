from functools import reduce

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

def totalByGenre(genre, movies):
    lists = list(filter(lambda movie: movie["genre"] == genre, movies))
    return len(lists)

def averageByYear(year, movies):
    getYears = list(filter(lambda movie: movie["year"] == year, movies))
    ratings = list(map(lambda movie: movie["rating"], getYears))
    total = reduce(lambda a, b: a + b, ratings)
    return total / len(ratings)

def highestRating(movies):
    return max(movies, key=lambda movie: movie["rating"])

def getInfo(movie):
    print("Informasi Film:", movie["title"])
    print("Rating:", movie["rating"])
    print("Tahun rilis:", movie["year"])
    print("Genre:", movie["genre"])

def main():
    global movies
    while True:
        print("\nPilih tugas yang ingin dilakukan:\n1. Menghitung jumlah film berdasarkan genre\n2. Menghitung rata-rata rating film berdasarkan tahun rilis\n3. Menemukan film dengan rating tertinggi\n4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre\n5. Selesai")
        choose = input("Masukkan nomor tugas (1/2/3/4/5): ")

        if choose == '1':
            genres = set(movie["genre"] for movie in movies)
            total = {genre: totalByGenre(genre, movies) for genre in genres}
            print("Jumlah film berdasarkan genre:")
            print(total)
        elif choose == '2':
            years = set(movie["year"] for movie in movies)
            average = {year: averageByYear(year, movies) for year in years}
            print("Rata-rata Rating Film berdasarkan Tahun Rilis:")
            print(average)
        elif choose == '3':
            high = highestRating(movies)
            print("Film dengan Rating Tertinggi:")
            getInfo(high)
        elif choose == '4':
            title = input("Masukkan judul film yang ingin dicari: ")
            found = False
            for movie in movies:
                if movie["title"] == title:
                    getInfo(movie)
                    found = True
                    break
            if not found:
                print("Film dengan judul tersebut tidak ditemukan.")
        elif choose == '5':
            break
        else:
            print("Pilihan tugas tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()