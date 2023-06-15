#!/usr/bin/python3


def remove_char_at(str, n):
    word = list(str)
    wordLen = len(word)
    newWord = ""
    for letter in range(wordLen):
        if letter != n:
            newWord += word[letter]
    return newWord
