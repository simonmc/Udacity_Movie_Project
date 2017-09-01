import media
import csv
#import fresh_tomatoes

movies={}

with open('80s_Movies.csv') as moviescsv:
    readCSV = csv.reader(moviescsv, delimiter=',')
    for row in readCSV:
        movie_title = row[0]
        movie_poster = row[1]
        movies[row] = media.Movie(movie_title, movie_poster)



