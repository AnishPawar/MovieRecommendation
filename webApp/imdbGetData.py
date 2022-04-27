



def returnMetaData(movieList,moviesDB):


    

    # movieRetData = []
    links = []
    titles = []
    years = []
    ratings = []

    for i in movieList:
        temp = []
        movies = moviesDB.search_movie(i)



        id = movies[0].getID()
        movie = moviesDB.get_movie(id)

        print("Cover url: %s" % movie['cover url'])

        title = movie['title']
        year = movie['year']
        rating = movie['rating']
        # directors = movie['directors']
        # casting = movie['cast']

        # temp.append([movie['cover url'],title,year])
        # movieRetData.append(temp)
        links.append(movie['cover url'])
        titles.append(title)
        years.append(year)
        ratings.append(rating)

    return links,titles,years,ratings
        
    # moviesDB.