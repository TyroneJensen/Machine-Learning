y = [14, 27, 1, 4, 2, 50, 3, 1]
x = [2, 4, -4, 3, 1, 1, 14, 27, 50]

# x = [13, 5, 6, 2, 5]
# y = [5, 2, 5, 13]


def find(x, y):
    sum_x = sum(x)
    sum_y = sum(y)
    len_x = len(x)
    len_y = len(y)

    answer = sum_x - sum_y

    if sum_x > sum_y and len_y > len_x:
        answer = -abs(answer)

    return answer


def find2(x, y):
    list_difference = []
    for item in x:
        if item not in y:
            list_difference.append(item)

    print(list_difference)


print(find(x, y))
find2(x, y)
