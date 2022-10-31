for string_a in s_d_n:
    # Hamming_dist_count
    h_d_c = 0
    # part of string
    part = 0
    # position of symbol in string
    pos = 0
    for symbol_a in string_a:
        if symbol_a[pos] == s_t[part][pos]:
            print("yes")
        else:
            print("no")