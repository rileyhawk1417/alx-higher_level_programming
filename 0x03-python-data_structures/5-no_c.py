#!/usr/bin/python3


def no_c(my_string):
    wordList = list(my_string)
    wordCount = len(wordList)
    newWord = ""
    for letter in range(wordCount):
        if wordList[letter] != "c" and wordList[letter] != "C":
            newWord += wordList[letter]
    return newWord
