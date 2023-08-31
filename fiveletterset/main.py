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
    addedwordsets = []
    for word in words:
        if len(word) == 5 and len(set(word)) == 5 and set(word) not in addedwordsets:
            fiveletterwords.append(word)
            addedwordsets.append(set(word))

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

def register_word(word, used):
    for letter in word:
        if letter in used:
            raise Exception(f"word {word} contains duplicate letter {letter}")
        used.add(letter)

def deregister_word(word, used):
    for letter in word:
        used.remove(letter)

def swap(arr, a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def depthprint(depth, *args):
    print("\t" * depth, *args, sep=" ", end="\n")

def get_letter_distinct_word(used_letters, allowable_words, current_word_list, depth_limit=5, depth=0):
    if depth_limit == len(word_list):
        depthprint(depth,"Depth limit reached")
        return current_word_list
    temp_allowable_words = allowable_words.copy()
    iteration_num = 0
    discard_ptr = len(temp_allowable_words)
    current_word = ""
    while discard_ptr >= len(temp_allowable_words) - 1 and iteration_num < len(temp_allowable_words):
        current_word = temp_allowable_words[iteration_num]
        current_word_set = set(current_word)
        discard_ptr = iteration_num + 1
        for i in range(discard_ptr, len(temp_allowable_words)):
            word = temp_allowable_words[i]
            for letter in word:
                if letter in current_word_set:
                    swap(temp_allowable_words, i, discard_ptr)
                    discard_ptr += 1
                    break
        iteration_num += 1
    if iteration_num >= len(temp_allowable_words) or discard_ptr >= len(temp_allowable_words):
        return None
    else:
        temp_allowable_words = temp_allowable_words[discard_ptr:]
        add_word(current_word, current_word_list, used_letters)
        depthprint(depth, current_word_list)
        depthprint(depth, f"words left: {len(temp_allowable_words)}")
        output = get_letter_distinct_word(used_letters, temp_allowable_words, current_word_list, depth_limit, depth + 1)
        while output is None and len(temp_allowable_words) > 0:
            depthprint(depth,f"No solution given {current_word}. Current word list: {current_word_list}")
            discard_words, current_word_list = current_word_list[depth:], current_word_list[:depth]
            for word in discard_words:
                print(f"removing {word}")
                deregister_word(word, used_letters)
            current_word = temp_allowable_words[0]
            add_word(current_word, current_word_list, used_letters)
            temp_allowable_words = temp_allowable_words[1:]
            output = get_letter_distinct_word(used_letters, temp_allowable_words, current_word_list, depth_limit, depth)
        if len(temp_allowable_words) == 0:
            return None
        depthprint(depth,"Found a word")
        depthprint(depth, current_word_list)
        return get_letter_distinct_word(used_letters, temp_allowable_words, current_word_list, depth_limit, depth + 1)


def remove_word(current_word, current_word_list, used_letters):
    depthprint(0, f"removing {current_word}. Current word list: {current_word_list}")
    current_word_list.remove(current_word)
    deregister_word(current_word, used_letters)


def add_word(current_word, current_word_list, used_letters):
    depthprint(0, f"adding {current_word}. Current word list: {current_word_list}")
    current_word_list.append(current_word)
    register_word(current_word, used_letters)


print(get_letter_distinct_word(used, fiveletterwords, word_list))

