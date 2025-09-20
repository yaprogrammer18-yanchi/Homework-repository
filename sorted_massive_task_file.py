def bubble(users_list):
    length = len(users_list)
    for i in range(length):
        for j in range(0, length - i - 1):
            if users_list[j] > users_list[j+1]:
                users_list[j], users_list[j+1] = users_list[j+1], users_list[j]

    return users_list
