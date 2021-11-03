import csv
from matplotlib import pyplot as plt
from allPackage.artistPackage import artist
from allPackage.musicPackage import music


class all_top10:
    def __init__(self, id, title, artist, top_genre, year):
        self.id = id
        self.title = title
        self.artist = artist
        self.top_genre = top_genre
        self.year = year


data = []
with open('top10s.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(all_top10(row[0], row[1], row[2], row[3], row[4]))


def stop():
    print('Program has been disabled.')
    exit()


def menu(programs):
    print('WELCOME\nMENU:')
    for key, program in programs.items():
        print(f'{key} - {program["name"]}')

    return input('Choose an option from the following list, \n'
                 'type a number and then press enter: ').upper()


programs = {
    '1': {'name': 'List of most popular artists on Spotify. ', 'function': artist.sorted_artist},
    '2': {'name': 'Top-10 artist on Spotify. ', 'function': artist.top_ten},
    '3': {'name': 'List of most popular music genres on Spotify.', 'function': music.sorted_music},
    '4': {'name': 'Top-10 genres on Spotify. ', 'function': music.top_ten_type},
    'X': {'name': 'Exit', 'function': stop},
}
choice = None

while choice != 'X':
    choice = menu(programs)
    try:
        if choice == 'X':
            programs[choice]['function']()
        else:
            print('=' * 20)
            programs[choice]['function'](data)
            print('=' * 20)
    except KeyError:
        print('Sorry, I did no understand that. Please, choose again.')

# x = []
# y = []
#
# for i in music.sorted_music(data)[:5]:
#     x.append(i[0])
#     y.append(i[1])
# plt.bar(x, y)
# plt.title('Top 5 genres of Music on Spotify 2010-2019')
# plt.xlabel('TYPE')
# plt.ylabel('VALUE')
# plt.xticks(rotation=45)
# plt.show()


# # artist.all_artist(data)
# artist.count_artist(data)
# # artist.print_key_value(data)
# artist.sorted_artist(data)
# artist.top_ten(data)
# music.count_type_of_music(data)
# music.sorted_music(data)
# music.sorted_music(data)
# music.top_ten_type(data)


# id
# title - song's title
# artist - song's artist
# top genren - the genre of the track
# year - Song's year in the Billboard
# bpm -Beats.Per.Minute - The tempo of the song.
# nrgy - Energy- The energy of a song - the higher the value, the more energtic. song
# dnce - Danceability - The higher the value, the easier it is to dance to this song.
# dB Loudness..dB.. - The higher the value, the louder the song
# live - Liveness - The higher the value, the more likely the song is a live recording
# Valence - The higher the value, the more positive mood for the song.
# Length - The duration of the song.
# Acousticness.. - The higher the value the more acoustic the song is.
# Speechiness - The higher the value the more spoken word the song contains.
# Popularity- The higher the value the more popular the song is.
