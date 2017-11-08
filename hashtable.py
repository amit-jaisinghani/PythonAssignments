def add_word(hash_map, word):
    '''
    adds new word to the hash_map
    if the word already exists in the hash_map,
    then its value is increased.
    :param hash_map: in which the words are to be added.
    :param word: which is to be added to the hash_map
    :return: None
    '''
    if word == '':
        return
    try:
        value = hash_map.get(word)
        hash_map.put(word, value + 1)
    except KeyError:
        hash_map.put(word, 1)


def find_max_repeating_word(hash_map):
    '''
    finds word in hash_map which has repeated maximum number of times.
    :param hash_map: from which maximum repeating word is to be found.
    :return: word and word_count
    '''
    word = None
    max = 0
    for entry in hash_map.table:
        if entry is not None:
            if entry.value > max:
                word = entry.key
                max = entry.value
    return word, max


def get_stats(file_name, max_load, hash_function_choice):
    '''

    :param file_name: in which the word with maximum frequency is to be found
    :param max_load: capacity of hashmap
    :param hash_function_choice: which hashing function is to be used
    :return: None
    '''
    try:
        file = open(file_name)
    except FileNotFoundError:
        print("File not found. Please check file name and path.")
        return
    hash_map = Hashmap(10000, max_load, hash_function_choice)
    for line in file:
        words = re.split('\W+', line)
        for word in words:
            word = word.lower()
            add_word(hash_map, word)
    word, max = find_max_repeating_word(hash_map)
    print("Word ", word, " has max occurrence of ", max)
    print("#Probe - ", hash_map.probe, "#Collision - ", hash_map.collision)
    return


def generate_stats(file_name):
    '''
    generates statistics for different hashing functions and load values
    :param file_name: on which statistics is to be performed
    :return: None
    '''
    loads = [0.7, 0.8, 0.9]

    for hash_algo in range(1, 4):
        for load in loads:
            print("File - ", file_name, " max load - ", load, " algo - ", hash_algo)
            get_stats(file_name, load, hash_algo)


def main():
    # generate_stats("The beginnings of nature control.txt")

    # generate_stats("The Family on Wheels.txt")

    generate_stats("dictionary.txt")
    pass


if __name__ == '__main__':
    main()
