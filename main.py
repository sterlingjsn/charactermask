from operator import itemgetter
import re


def main():
    Name_of_file = input("Enter a file name: ")

    # open file
    try:
        file = open(Name_of_file, "r")

    except FileNotFoundError:
        print("The file name " + Name_of_file + " does not exist")
        exit()

    # process list of words from file
    words = get_the_words(file)

    # get frequency of each word
    dictionary = get_frequent_word(words)

    find_most(dictionary)

    find_less(dictionary)

    words_unique = find_unique(dictionary)
    print("++ Number of Unique Words ++")
    print(words_unique)

    return


def get_frequent_word(words):
    dictionary = {}

    # for all the words in given list
    for word in words:
        # if word present in dictionary increment count
        if word in dictionary:
            dictionary[word] += 1
        else:
            # else put it in dictionary
            dictionary[word] = 1

    return dictionary


def get_the_words(file):
    # this is the pattern that make a word, a-z letters and A-Z letters, + here denotes
    # 1 or more than one occurence of these characters
    words_pattern = '[a-zA-Z]{2,}'
    words = []

    # get one line at a time
    for line in file:
        # using regex pattern above separate all the words from this line, ignoring the case
        list_of_words = re.findall(words_pattern, line, flags=re.IGNORECASE)

        # for all the words extracted above append words with more than 1 letter in list
        for word in list_of_words:
            if len(word) > 1:
                words.append(word.lower())


    return words


def find_most(dictionary):
    # make a list of all key, value tuple from dictionary
    dictionary_words = list(dictionary.items())

    # sort by value in descending order, so that most frequent words would be placed first
    dictionary_words.sort(key=itemgetter(1,0), reverse=True)

    # get either 10 or the minimum number of words present
    numberofwords = min(10, len(dictionary_words))
    Frequent_most = dictionary_words[0:numberofwords]

    print("++ Most Frequent Words ++")

    # print
    for i in range(numberofwords):
        (word, dictionary) = Frequent_most[i]

        if i == 0:
            print("Most frequent word: ", end='')
        elif i == 1:
            print("2nd most frequent word: ", end='')
        elif i == 2:
            print("3rd most frequent word: ", end='')
        else:
            print(str(i + 1) + "th most frequent word: ", end='')

        print(word + ", " + str(dictionary))

    return


def find_less(dictionary):
    words_unique = 0

    # sort key value tuple-list by value in ascending order
    dictionary_words = list(dictionary.items())
    dictionary_words.sort(key=itemgetter(1,0))

    number_of_words = min(10, len(dictionary_words))
    frequent_less = dictionary_words[words_unique:words_unique + number_of_words]

    print(" ++ Least frequent words ++")

    # print
    for i in range(number_of_words):
        (word, dictionary) = frequent_less[i]
        if i == 0:
            print("Most infrequent word: ", end='')
        elif i == 1:
            print("2nd most infrequent word: ", end='')
        elif i == 2:
            print("3rd most infrequent word: ", end='')
        else:
            print(str(i + 1) + "th most infrequent word: ", end='')

        print(word + ", " + str(dictionary))

    return


def find_unique(dictionary):
    return len(dictionary.keys())


main()