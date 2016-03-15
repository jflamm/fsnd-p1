import media
import fresh_tomatoes

if __name__ == "__main__":
    movies = []

    movies.append(media.Movie('Ex Machina', 'http://www.impawards.com/2015/posters/ex_machina_ver5.jpg',
                              'https://youtu.be/XYGzRB4Pnq8')
                  )
    movies.append(media.Movie('Lust, Caution', 'https://upload.wikimedia.org/wikipedia/en/3/32/Lust_caution.jpg',
                              'https://youtu.be/4vdib9unQv8')
                  )
    movies.append(media.Movie('Lone Star', 'http://ia.media-imdb.com/images/M/MV5BMTI2NjUwODY0Nl5BMl5BanBnXkFtZTcwMjYyODcxMQ@@._V1_UY1200_CR113,0,630,1200_AL_.jpg',
                              'https://youtu.be/fhd8AHbp2c4')
                  )

    fresh_tomatoes.open_movies_page(movies)