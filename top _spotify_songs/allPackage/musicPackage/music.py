def type_of_music(data):
    lst_type = []
    for i in data[1:]:
        lst_type.append(i.top_genre)
    return lst_type


def count_type_of_music(data):
    counts = dict()
    for word in type_of_music(data):
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def sorted_music(data):
    sort_orders = sorted(count_type_of_music(data).items(), key=lambda x: x[1], reverse=True)
    for i in sort_orders:
        print(i[0], i[1])
    print('----------------')
    return sort_orders


def top_ten_type(data):
    for i in sorted_music(data)[:10]:
        return i[0], i[1]
