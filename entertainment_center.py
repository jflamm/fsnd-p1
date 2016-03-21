import media
import fresh_tomatoes
import requests


def get_movie_info(title):
    url = 'http://www.omdbapi.com/'
    try:
        arg_dict = {'t': title, 'plot':'short', 'r':'json'}
        r = requests.get(url, params=arg_dict)
        return r.json()
    except Exception as e:
        print 'omdbapi exception', e
        return None

if __name__ == "__main__":

    # Create a list and add some movies
    movies = []

    info = get_movie_info('Ex Machina')
    movies.append(media.Movie('Ex Machina',
                              'http://www.impawards.com/2015/posters/ex_machina_ver5.jpg',
                              'https://youtu.be/XYGzRB4Pnq8',
                              info['Year'],
                              info['Plot']))

    info = get_movie_info('Lust, Caution')
    movies.append(media.Movie('Lust, Caution',
                              'https://upload.wikimedia.org/wikipedia/en/3/32/Lust_caution.jpg',
                              'https://youtu.be/4vdib9unQv8',
                              info['Year'],
                              info['Plot']))

    info = get_movie_info('Lone Star')
    movies.append(media.Movie('Lone Star',
                              'http://ia.media-imdb.com/images/M/MV5BMTI2NjUwODY0Nl5BMl5BanBnXkFtZTcwMjYyODcxMQ@@._V1_UY1200_CR113,0,630,1200_AL_.jpg',
                              'https://youtu.be/fhd8AHbp2c4',
                              info['Year'],
                              info['Plot']))

    # Generate HTML from list of movies and open web page in browser
    fresh_tomatoes.open_movies_page(movies)
