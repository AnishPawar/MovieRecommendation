from flask import Flask, request, render_template, jsonify,json
from flask_cors import CORS
import pandas as pd
from imdbGetData import returnMetaData
import imdb
from movierecommendation import recommend

import datetime

app = Flask(__name__)
CORS(app)

movieNames = []

test = ['Spider-Man','Spider-Man 2','Spider-Man 3','The Amazing Spider-Man','The Amazing Spider-Man 2']
moviesDB = imdb.IMDb()

@app.route('/', methods= ['GET', 'POST'])
def lander():
    # print(returnMetaData(test))
    print("OK1")
    # print()
    links = ['']*5
    titles = ['NA']*5
    years = [0]*5
    ratings = [0]*5
    genres = ['NA']*5
    runtimes = [0]*5

    if request.form:
        # print(request.form)
        if request.form.getlist('movieName'):
                movieRet = request.form.getlist('movieName')[0]
                # print(f"Gooo: {n_future}")
                movie_name = movieRet[:-6].strip()
                # print(movie_name)
                movies = recommend(movie_name)[:5]
                names = [x['Title'] for x in movies]

                moviesx = [x[:-6].strip() for x in names]
                names_new = []
                for name in moviesx:
                    if name[-5:] == ", The":
                        name = "The " + name[:-5]
                    names_new.append(name)


                print(names_new)

                links,titles,years,ratings,genres,runtimes = returnMetaData(names_new,moviesDB)
    print("OK2")
    return render_template('index.html',movieNames = movieNames,links=links,titles=titles,years=years,ratings = ratings, genres= genres, runtimes = runtimes)

if __name__ == "__main__":
    k = pd.read_csv('assets/movies.csv')
    movieNames = k['title'].values.tolist()
    # movieNames = movieNames[:100]
    app.run()

    # SOCD report detected: (AP watchdog expired)