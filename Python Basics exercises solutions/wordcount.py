#!/usr/bin/env python3 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# Python 3 version https://github.com/eladeyal-intel/python_exercise

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

from __future__ import print_function

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. Implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. Implement a print_top(filename) which is similar
to print_words() but which prints just the top 5 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

#### LAB(begin solution)

def word_count_dict(filename):
  """Returns a word/count dict for this filename."""
  # Utility used by count() and Topcount().
  word_count = {}  # Map each word to its count
  input_file = open(filename, 'r')
  for line in input_file:
    words = line.split()
    for word in words:
      word = word.lower()
      # Special case if we're seeing this word for the first time.
      if not word in word_count:
        word_count[word] = 1
      else:
        word_count[word] = word_count[word] + 1
  input_file.close()  # Not strictly required, but good form.
  return word_count


def print_words(filename):
  """Prints one per line '<word> <count>' sorted by word for the given file."""
  word_count = word_count_dict(filename)
  words = sorted(word_count.keys())
  for word in words:
    print(word, word_count[word])


def get_count(word_count_tuple):
  """Returns the count from a dict word/count tuple  -- used for custom sort."""
  return word_count_tuple[1]


def print_top(filename):
  """Prints the top count listing for the given file."""
  word_count = word_count_dict(filename)

  # Each item is a (word, count) tuple.
  # Sort them so the big counts are first using key=get_count() to extract count.
  items = sorted(word_count.items(), key=get_count, reverse=True)

  # Print the first 5
  for item in items[:5]:
    print(item[0], item[1])

##### LAB(end solution)


# This basic main function is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  print('print_words start')
  print_words('wordcount_input.txt')
  print('print_words end')
  print('print_top start')
  print_top('wordcount_input.txt')
  print('print_top end')

if __name__ == '__main__':
  main()
