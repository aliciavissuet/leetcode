def word_ladder(start, end, word_list):
    word_dict = defaultdict(int)
    for word in word_list:
        word_dict[word] = 1
    return word_ladder_helper(start, end, word_dict, 0)


def word_ladder_helper(start, end, word_dict, count):

    alph = 'abcdefghijklmnopqrstuvwzyz'
    words_to_visit = []
    if start == end:
        return 1

    count_min = None
    for i in range(len(start)):
        for j in range(0, 26):
            temp_word = start[0:i]+alph[j]+start[i+1:]

            if word_dict[temp_word] is not 0:
                word_dict[temp_word] = 0
                words_to_visit.append(temp_word)

    for word in words_to_visit:
        next_count = word_ladder_helper(word, end, word_dict, count)
        if not count_min and next_count and next_count > 0:
            count_min = next_count
        elif count_min and next_count and next_count < count_min:
            count_min = next_count
    print(start)
    print(words_to_visit)
    if not count_min:
        return count_min
    else:
        return 1 + count_min
