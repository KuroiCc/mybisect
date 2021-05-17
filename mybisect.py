def mybisect(data, searching_word, flag0=0):
    flag = len(data) // 2
    # t = data[flag]
    if data[flag] == searching_word:
        return flag + flag0
    elif flag == 0:
        return False
    elif data[flag] < searching_word:
        return mybisect(data[flag:], searching_word, flag + flag0)
    elif data[flag] > searching_word:
        return mybisect(data[:flag], searching_word, flag0)


if __name__ == "__main__":
    data = list(range(101))
    searching_word = 101
    t = mybisect(data, searching_word)
    print((data[searching_word]))
    print(t)
