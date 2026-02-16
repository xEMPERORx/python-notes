def string_to_num(s, value=0):
    if not s:
        return value

    for word in WORD_DICT:   # Not a loop in logic (dictionary is fixed 10 items)
        if s.startswith(word):
            return string_to_num(s[len(word):], value * 10 + WORD_DICT[word])

    return -1  
