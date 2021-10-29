def all_artist(data):
    word = []
    for x in data[1:]:
        word.append(x.artist)
    return word


def count_artist(data):
    counts = dict()
    for word in all_artist(data):
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


# def print_key_value(data):
#     for k, v in count_artist(data).items():
#         print(k, v)

def sorted_artist(data):
    sort_orders = sorted(count_artist(data).items(), key=lambda x: x[1], reverse=True)
    for i in sort_orders:
        print(i[0], i[1])
    print('----------------')
    return sort_orders


def top_ten(data):
    for i in sorted_artist(data)[:10]:
        print(i[0], i[1])


