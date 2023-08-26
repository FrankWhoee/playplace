def file_exists(file_path):
    try:
        with open(file_path, "r") as f:
            return True
    except FileNotFoundError:
        return False

if not file_exists("fiveletterset.txt"):
    filename = "words_alpha.txt"
    # load filename as a list
    words = []
    with open(filename, "r") as f:
        words.extend(f.read().split("\n"))
    fiveletterwords = []
    for word in words:
        if len(word) == 5 and len(set(word)) == 5:
            fiveletterwords.append(word)

    # write the list to a file
    with open("fiveletterset.txt", "w") as f:
        f.write("\n".join(fiveletterwords))
else:
    with open("fiveletterset.txt", "r") as f:
        fiveletterwords = f.read().split("\n")

letters = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"}
used = set()
word_list = []

def add_word(word, used):
    for letter in word:
        used.add(letter)

def remove_word(word, used):
    for letter in word:
        used.remove(letter)

def depthprint(depth, *args):
    print("\t" * depth, *args, sep=" ", end="\n")

def get_letter_distinct_word(used_letters, allowable_words, current_word_list, depth=0):
    depthprint(depth, current_word_list)
    depthprint(depth, used_letters)
    current_word = allowable_words[0]
    add_word(current_word, used_letters)
    current_word_list.append(current_word)
    depthprint(depth,"Add word:", current_word)
    for word in allowable_words[::-1]:
        for letter in word:
            if letter in used_letters:
                allowable_words.remove(word)
                break
    depthprint(depth, "allowable words:", len(allowable_words))
    if len(allowable_words) == 0:
        return None
    else:
        prev_size = len(current_word_list)
        output = get_letter_distinct_word(used_letters, allowable_words.copy(), current_word_list, depth=depth+1)
        depthprint(depth, current_word_list)
        depthprint(depth, output is None, prev_size)
        while output is None and len(current_word_list) < 5:
            depthprint(depth, "backtrack")
            depthprint(depth, current_word_list)
            current_word_list = current_word_list.remove(current_word)
            depthprint(depth, current_word_list)
            remove_word(current_word, used_letters)
            allowable_words = allowable_words[1:]
            output = get_letter_distinct_word(used_letters, allowable_words.copy(), current_word_list,depth=depth+1)
        return output

print(get_letter_distinct_word(used, fiveletterwords, word_list))