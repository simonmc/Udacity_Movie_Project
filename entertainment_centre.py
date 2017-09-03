import csv
import media
import fresh_tomatoes

#Initialising List to store movie data
Movies = []
inputfile = '80s_Movies.csv'
#Opening CSV file containing movie data
with open(inputfile) as moviescsv:
    readCSV = csv.reader(moviescsv, delimiter=',')
    for row in readCSV:
        movie_title = row[0]
        movie_trailer = row[1]
        #Instantiating Movie instances and add them to the movie List
        #THIS IS THE BIT I WAS STRUGGLING WITH BUT THEN I FOUND THIS
        #https://stackoverflow.com/questions/15769246/pythonic-way-to-print-list-items
        Movies.append(media.Movie(movie_title, movie_trailer))

#Renders and opens web page
fresh_tomatoes.open_movies_page(Movies)
