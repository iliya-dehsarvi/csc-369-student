import time
from collections import defaultdict

def count_words_book(book):
    file = open(book).read()
    # YOUR SOLUTION HERE
    words = file.split()
    book_word_freq = defaultdict(int)
    for word in words:
        book_word_freq[word] += 1
    time.sleep(0.1)
    return book_word_freq

def count_words(book_files):
    book_word_freq = {}
    for book in book_files:
        book_word_freq[book] = count_words_book(book)
    return book_word_freq