import media
import csv
import fresh_tomatoes

#Initialising List to store movie data
movies=[]

#Opening CSV file containing movie data
with open('80s_Movies.csv') as moviescsv:
    readCSV = csv.reader(moviescsv, delimiter=',')
    for row in readCSV:
        movie_title = row[0]
        movie_trailer = row[1]
        
        #Instantiating Movie instances and add them to the movie List 
        #THIS IS THE BIT I WAS STRUGGLING WITH BUT THEN I FOUND THIS 
        #https://stackoverflow.com/questions/15769246/pythonic-way-to-print-list-items
        movies.append(media.Movie(movie_title, movie_trailer))

#Renders and opens web page
fresh_tomatoes.open_movies_page(movies)
