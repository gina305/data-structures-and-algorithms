#from data_structures.hashtable import Hashtable


def first_repeated_word(string=" Oh laa laa"):

    words = string.split(" ")

    found_words = []

    for word in words:
        if word in found_words:
            return word
        else:
            found_words.append(word)


# x = first_repeated_word()
#
# print(x)
