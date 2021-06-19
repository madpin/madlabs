def return_valid_words(l, words_list):

    def is_valid(word):
        return str(word) in words_list

    lines = len(l)
    col = len(l[0])

    valid_words = []

    def word_from_0(x, y, previous_string='', used_xy=None):
        if(used_xy is None):
            used_xy = []
        
        if(x >= lines or x < 0):
            return
        if(y >= col or y < 0):
            return

        if (x, y) in used_xy:
            return

        new_used_xy = used_xy.copy()
        new_used_xy.append((x, y))

        current_string = previous_string+l[x][y]
        if(is_valid(current_string)):
            valid_words.append(current_string)

        word_from_0(x+1, y, current_string, new_used_xy)
        word_from_0(x+1, y+1, current_string, new_used_xy)
        word_from_0(x, y+1, current_string, new_used_xy)

        word_from_0(x-1, y, current_string, new_used_xy)
        word_from_0(x-1, y-1, current_string, new_used_xy)
        word_from_0(x, y-1, current_string, new_used_xy)

        word_from_0(x+1, y-1, current_string, new_used_xy)
        word_from_0(x-1, y+1, current_string, new_used_xy)
        return

    for x in range(lines):
        for y in range(col):
            print(x, y)
            word_from_0(x, y)

    return valid_words
