import csv
from matplotlib import pyplot as plt


class all_top10:
    def __init__(self, id, title, artist, top_genre, year, bpm, nrgy):
        self.id = id
        self.title = title
        self.artist = artist
        self.top_genre = top_genre
        self.year = year
        self.bmp = bpm
        self.nrgy = nrgy


data = []
with open('top10s.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(all_top10(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))


def artist_number(data):
    word = []
    for x in data[1:]:
        word.append(x.artist)
    return word


def count_artist():
    counts = dict()
    for word in artist_number(data):
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


# def print_key_value(counts):
#     for k, v in counts.items():
#         print(k, v)
#
# print_key_value(count_artist())


def sorted_artist(counts):
    sort_orders = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    for i in sort_orders:
        print(i[0], i[1])
    return sort_orders


sorted_artist(count_artist())


def top_ten(sort_orders):
    for i in sort_orders[:10]:
        print(i[0], i[1])


top_ten(sorted_artist(count_artist()))

# def type_music():
#     type = []
#     for i in data:
#         type.append(i.top_genre)
#     return type


#
# data = open('top10s.csv', encoding='utf-8')
# data = csv.reader(data)
# data_lines = list(data)
# for lin in data_lines[:5]:
#     print(lin)


# for i in data:
#     data_line.append(all_top10('id', 'title', 'artist'))


# all = []
# for line in data_lines[1:15]:
#     all.append(line[3])
# print(all)

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
