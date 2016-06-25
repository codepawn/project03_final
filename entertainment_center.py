import media
import fresh_tomatoes

zootopia = media.Movie(
    'Zootopia',
    'Judy Hopps fulfills her childhood dream of becoming the first rabbit police officer in Zootopia',
    'https://goo.gl/bKHPKS',
    'https://www.youtube.com/watch?v=G5_TpW2prTM')

fightclub = media.Movie(
    'Fightclub',
    'An insomniac office worker, looking for a way to change his life',
    'https://goo.gl/GqBX9a',
    'https://www.youtube.com/watch?v=SUXWAEX2jlg')

movie_21 = media.Movie(
    '21',
    '"21" is the fact-based story about six MIT students who were trained to become experts in card counting',
    'https://goo.gl/dbHd61',
    'https://www.youtube.com/watch?v=0rx_fBD7ZKQ')


movies = [zootopia, fightclub, movie_21]

fresh_tomatoes.open_movies_page(movies)
