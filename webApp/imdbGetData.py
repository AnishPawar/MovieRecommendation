
from cProfile import run


def returnMetaData(movieList,moviesDB):


    

    # movieRetData = []
    links = []
    titles = []
    years = []
    ratings = []

    genres = []
    runtimes = []

    for i in movieList:
        temp = []
        movies = moviesDB.search_movie(i)



        id = movies[0].getID()
        movie = moviesDB.get_movie(id)

        # print("Cover url: %s" % movie['full-size cover url'])

        # print(movie.keys())

        title = movie['title']
        year = movie['year']
        rating = movie['rating']
        genre = movie['genres']
        runtime = movie['runtimes']
        # directors = movie['directors']
        # casting = movie['cast']

        # temp.append([movie['cover url'],title,year])
        # movieRetData.append(temp)

        print(title,year,rating,genre,runtime)

        links.append(movie['full-size cover url'])
        titles.append(title)
        years.append(year)
        ratings.append(rating)
        genres.append(genre[0])
        runtimes.append(runtime[0])

    return links,titles,years,ratings,genres,runtimes
        
    # moviesDB.