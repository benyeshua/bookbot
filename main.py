from re import findall
from collections import Counter

path_to_book = 'books/frankenstein.txt'

with open(path_to_book) as f:
    file_contents = f.read()

def count(string):
    return len(string.split())

def char_frequency(string):
    join_words_in_lowercase = ''.join([word.lower() for word in string.split()])
    alphabeth_chars_only = ''.join([letter for letter in join_words_in_lowercase if letter.isalpha()])
    letter_frequency_dict = Counter(alphabeth_chars_only)
    letter_frequency_dict = dict(sorted(letter_frequency_dict.items(), \
        key=lambda key_value_arg: key_value_arg[1], reverse=True))
    return letter_frequency_dict

def generate_report(string):
    print(f'--- Begin report of {path_to_book} ---\n')
    print(f'{count(file_contents)} words found in the document\n\n')
    word_frequency_dictionary = char_frequency(file_contents)
    for char, frequency in word_frequency_dictionary.items():
        print(f"The '{char}' character was found {frequency} times\n")
    print('--- End report ---')

def main():
    generate_report(file_contents)

main()