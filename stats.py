def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    text = text.lower()
    chars = {}
    for c in text:
        chars[c] = chars.get(c, 0) + 1
    return chars

def sort_characters(char_dict):
    # Convert dict → list of {"char": c, "num": n}
    char_list = []
    for c, n in char_dict.items():
        char_list.append({"char": c, "num": n})

    # Sort descending by "num"
    char_list.sort(reverse=True, key=lambda x: x["num"])
    return char_list
