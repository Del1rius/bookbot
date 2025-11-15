def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    text = text.lower()
    counts = {}

    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts