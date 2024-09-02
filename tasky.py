# Create a function that takes a string and returns a string in which each character is repeated

# once.

# Examples

# doubleChar("String") → "ssttrriinngg"

# doubleChar("Hello World!") → "HHeelllloo WWoorrlldd!!"

# doubleChar("1234!_") → "11223344!!



# def doubleChar(s):
#     result = ''
#     for char in s:
#         result += char * 2
#     return result

# print(doubleChar("String"))
# print(doubleChar("Hello World!"))
# print(doubleChar("1234!_"))


# _____________________________________________________________________________________

# 4. Write a function in Python to read lines from a text file "notes.txt". Your function should find and display the occurrence of the word "the".

# For example: If the content of the file is:

# "India is the fastest-growing economy. India is looking for more investments around the globe. The whole world is looking at India as a great market. Most of the Indians can foresee the heights that India is capable of reaching."


# def count_the_word():
#     count = 0
#     with open("notes.txt", "r") as file:
#         for line in file:
#             words = line.lower().split()
#             count += words.count("the")
#     return count

# print("Amount of the repeated words is ---> ", count_the_word(), "times the words - the - ")

# _____________________________________________________________________________________________

# - Write a function in Python to count words in a text file those are ending with alphabet "e". 


# def words_with_e(filename):
#     count = 0
#     with open(filename, "r") as file:
#         for line in file:
#             words = line.split()
#             for word in words:
#                 if word.endswith('e'):
#                     count += 1
#     return count

# print(words_with_e("notes.txt"))


# _______________________________________________________________________________________________

# 6. Write a function in Python to count the words "this" and "these" present in a text file "article.txt". [Note that the words "this" and "these" are complete words] Solution

# def count_this_these():
#     count_this = 0
#     count_these = 0
#     with open("article.txt", "r") as file:
#         for line in file:
#             words = line.lower().split()
#             count_this += words.count("this")
#             count_these += words.count("these")
#     return count_this, count_these

# this_count, these_count = count_this_these()
# print(f'"this ---> ": {this_count}, "these ---> ": {these_count}')

# __________________________________________________________________________________________________

# The Full Length of a Google

# Google's logo can be stretched depending on how many pages it lets you skip forward to.

# <Goooooooooogle>

# Previous 1 2 3 4 5 6 7 8 9 10 Next

# Let's say we wanted to change the number of pages that Google could skip to. Create a function where given a number of pages n, return the word "Google" but with the correct number of "o"s.

# Examples

# googlify(10) → "G0000000ooogle"

# googlify(23) → "G000000000000000000000oogle"

# googlify(2) → "Google"

# googlify(-2) → "invalid"



# def googlify(n):
#     if n <= 1:
#         return "invalid"
#     return f"G{"0" * (n - 1)}oogle"

# print(googlify(10))
# print(googlify(23))
# print(googlify(2))
# print(googlify(-2))


# ________________________________________________________________________________________________

# 119. Write a Python program to check if a substring appears in a given list of string values.

# Original list:

# ['red', 'black', 'white', 'green', 'orange']

# Substring to search:

# ack

# Check if a substring presents in the said list of string values:

# True

# Substring to search:

# abc

# Check if a substring presents in the said list of string values:

# False



# def substring_in_list(strings, substring):
#     return any(substring in s for s in strings)

# original_list = ['red', 'black', 'white', 'green', 'orange']

# substring1 = 'ack'
# print(f"Substring to search: {substring1}")
# print("Check if a substring presents in the said list of string values:")
# print(substring_in_list(original_list, substring1))

# substring2 = 'abc'
# print(f"\nSubstring to search: {substring2}")
# print("Check if a substring presents in the said list of string values:")
# print(substring_in_list(original_list, substring2))

# ________________________________________________________________________________

# Free Coffee Cups


# For each of the 6 coffee cups I buy, I get a 7th cup free. In total, I get 7 cups. Create a function that takes in cups bought and return the total number of cups I would get.

# Examples

# TotalCups (6) →7

# TotalCups (12) →14

# TotalCups (213) - 248



# def total_cups(cups_bought):
#     free_cups = cups_bought // 6
#     total = cups_bought + free_cups
#     return total

# print(total_cups(6))
# print(total_cups(12))
# print(total_cups(213)) 


# ____________________________________________________________________________

# Concatenating First and Last Character of a String


# Create a function that takes a string and returns the concatenated first and last character.

# Examples

# first_last("ganesh") "gh"

# first_last("kali") → "ki"

# first_last("shiva") → "sa"

# first_last("vishnu") → "vu"

# first_last("durga") → "da"



# def first_last(s):
#     if len(s) < 1:
#         return ""
#     return s[0] + s[-1]

# print(first_last("ganesh"))
# print(first_last("kali"))
# print(first_last("shiva"))
# print(first_last("vishnu"))
# print(first_last("durga"))

# _____________________________________________________________________________


# Is the Word Singular or Plural?


# Create a function that takes in a word and determines whether or not it is plural. A plural word is one that ends in "s".

# Examples

# is_plural("changes") → True

# is_plural("change") False

# is_plural("dudes") → True

# is_plural("magic") False

# Notes

# Don't forget to return the result.

# Remember that return True (boolean) is not the same as return "True" (string).

# This is an oversimplification of the English language. We are ignoring edge cases like "goose" and "geese", "fungus" and "fungi", etc.


# def is_plural(word):
#     return word.endswith('s')

# print(is_plural("changes"))
# print(is_plural("change"))
# print(is_plural("dudes"))
# print(is_plural("magic"))
