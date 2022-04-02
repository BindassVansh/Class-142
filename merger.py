import csv
with open("movie_links.csv",encoding="utf8") as f :
    reader = csv.reader(f)
    data = list(reader)
    header_links = data[0]
    allmovies_link = data[1:]

with open("movies.csv",encoding="utf8") as f :
    reader = csv.reader(f)
    data = list(reader)
    header_movies = data[0]
    allmovies_details = data[1:]

movies  = []

for m in allmovies_link :
    for d in allmovies_details :
        if m[0] == d[8] :
            d.append(m[1])
            movies.append(d)
            break

header_movies.append("imdb_links")

with open("merged.csv","a+",encoding="utf8",newline='') as f :
    writer = csv.writer(f)
    writer.writerow(header_movies)
    writer.writerows(movies)







