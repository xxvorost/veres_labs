def boyer_moore(haystack, needle):
    if not needle:
        return []

    shift_table = {}
    for i in range(len(needle) - 1):
        shift_table[needle[i]] = len(needle) - i - 1

    indices = []
    i = len(needle) - 1
    while i < len(haystack):
        match = True
        for j in range(len(needle)):
            if haystack[i - j] != needle[-1 - j]:
                match = False
                break
        if match:
            indices.append(i - len(needle) + 1)
            i += 1
        else:
            if haystack[i] in shift_table:
                i += shift_table[haystack[i]]
            else:
                i += len(needle)

    return indices
