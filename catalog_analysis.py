import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]

# Этап 1. Разминка: переменные, числа, math


def average_rating(movies):
    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)  # самый старый
    newest = min(ages)  # самый новый
    mean_age = math.ceil(sum(ages) / len(ages))  # средний возраст
    return (oldest, newest, mean_age)


def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


"""
#проверка:
print(average_rating(movies))        # 7.2
print(catalog_age_stats(movies))     # (15, 2, 8)
print(duration_in_hours(155))        # 2ч 35м
"""

# Этап 2. Условия и match


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _ if year < 2015:
            return "старые"


# Этап 3. Циклы

# 1. фильмы, которые не комедии
print("Этап 3. Фильмы, которые не комедии")
for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])
print("-----------------------")


# 2. первый фильм с рейтингом выше 9.0
def find_first_masterpiece(movies):
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print(f"Первый шедевр: {movies[i]['title']} ({movies[i]['rating']})")
            break
        i += 1
    else:
        print("Шедевров не найдено")


# 3. for с накопительной переменной
def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

# Этап 4. Строки


def normalize_title(title):
    words = title.split()
    result = []
    for word in words:
        result.append(word[0].upper() + word[1:].lower())
    return " ".join(result)


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    title = normalize_title(movie["title"])
    genres = ", ".join(sorted(movie["genres"]))
    duration = duration_in_hours(movie["duration_min"])
    return (
        f'"{title}" ({movie["year"]}) — '
        f"{movie['rating']}/10, {duration}, жанры: {genres}"
    )

# Этап 5. Списки


def titles_sorted_by_rating(movies):
    ordered = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [m["title"] for m in ordered]


def top_n_by_rating(movies, n=3):
    ordered = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(m["title"], m["rating"]) for m in ordered[:n]]


# Этап 6. Словари


def count_by_genre(movies):
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography.setdefault(actor, []).append(movie["title"])
    return filmography


def above_average_ratings(movies):
    avg = average_rating(movies)
    return {m["title"]: m["rating"] for m in movies if m["rating"] > avg}


# Этап 7. Множества


def all_genres(movies):
    result = set()
    for movie in movies:
        result |= movie["genres"]
    return result


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)


# Этап 8. Итераторы и генераторы


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


# демонстрация
print("Этап 8. Демонстрация работы цикла for с вызовом format_report_line:")
for movie in iter_high_rated(movies):
    print(format_report_line(movie))
print("-------------------------------")

# суммарная длительность фильмов с рейтингом выше 7
total_minutes = sum(m["duration_min"] for m in movies if m["rating"] > 7)
# print(total_minutes)

# Этап 9. Итоговый отчет


def build_report(movies):
    avg_rating = average_rating(movies)
    mean_age = catalog_age_stats(movies)[2]
    top3 = sorted(movies, key=lambda m: m["rating"], reverse=True)[:3]
    genre_counts = count_by_genre(movies)
    by_count = sorted(genre_counts.items(), key=lambda item: (-item[1], item[0]))

    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {avg_rating}")
    print(f"Средний возраст фильмов: {mean_age} лет")

    print("\nТоп-3 фильма:")
    for movie in top3:
        print(f"  {format_report_line(movie)}")

    print("\nФильмов по жанрам:")
    for genre, count in by_count:
        print(f"  {genre} — {count}")

    print(f"\nВсе жанры каталога: {', '.join(sorted(all_genres(movies)))}")


build_report(movies)