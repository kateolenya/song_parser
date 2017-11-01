def get_the_song():
    """
    Reads the song from stdin and gently stores it in the_song
    :return: the_song, list of strings, each string is a song line
    """
    print("Hello! I'm starting to read your file\n")
    the_song = []
    while True:
        try:
            song_line = input()
            the_song.append(song_line)
        except EOFError:
            print("I've reached the end of file\n")
            break
    return the_song


def print_out_song_nicely(the_song):
    """
    Takes the song and prints it out nicely
    :param the_song: list of strings, each string is a song line
    :return: None
    """
    print("_________________________________________________________________________\n")
    print("Here is your song, sweetheart")
    for line in the_song:
        print('\t', line)
    print("_________________________________________________________________________\n")
    return None


def get_words_from_lines(the_song):
    """
    Takes the song and returns list of words used in the song
    :param the_song: list of strings, each string is a song line
    :return: list_of_words, list that contains words
    """
    list_of_words = []
    for line in the_song:
        words_in_line = line.split()
        for word in words_in_line:
            list_of_words.append(word.lower())
    return list_of_words


def remove_duplicates(list_of_words):
    """
    Takes list of words, returns list of unique words
    :param list_of_words: list containing words
    :return: no_duplicates, list of unique words
    """
    no_duplicates = []
    for word in list_of_words:
        if word not in no_duplicates:
            no_duplicates.append(word)
    return no_duplicates
