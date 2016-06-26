import media
import fresh_tomatoes

toy_story = media.Movie(
    'Toy story',
    'A story of a boy and his toys that come to life',
    'http://goo.gl/Nyxnis',
    'https://goo.gl/edM1nn')

avatar = media.Movie(
    'Avatar',
    'A marine on an alien planet',
    'https://goo.gl/4zpb2O',
    'https://goo.gl/3veMzO')

zootopia = media.Movie(
    'Zootopia',
    'Judy Hopps fulfills her childhood dream of becoming the first rabbit \
    police officer in Zootopia',
    'https://goo.gl/bKHPKS',
    'https://www.youtube.com/watch?v=G5_TpW2prTM')

fightclub = media.Movie(
    'Fightclub',
    'An insomniac office worker, looking for a way to change his life',
    'https://goo.gl/GqBX9a',
    'https://goo.gl/f42cyU')

movie_21 = media.Movie(
    '21',
    '"21" is the fact-based story about six MIT students who were trained to \
    become experts in card counting',
    'https://goo.gl/dbHd61',
    'https://goo.gl/R46KKA')


# avatar.show_trailer()
# zootopia.show_trailer()

# the below code describes the function itself
movies = [zootopia, fightclub, movie_21]

fresh_tomatoes.open_movies_page(movies)
