#!/usr/bin/python3

from song_parser_helpers import *

# Reading the song from stdin and storing it
theSong = get_the_song()

print_out_song_nicely(theSong)

listOfWords = get_words_from_lines(theSong)

noDuplicates = remove_duplicates(listOfWords)

print(sorted(noDuplicates))
