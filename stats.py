
def get_num_words(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

def count_chars(str):
    lchar_counts = {}
    for lchar in str.lower():
        if lchar in lchar_counts:
            lchar_counts[lchar] += 1
        else:
            lchar_counts[lchar] = 1
    return lchar_counts

