#!/usr/bin/env python3
from itertools import product, permutations
from lists import leet_dict, separator_list, ending_list
import sys
import argparse
import os


def do_permutations(keywords):

    keywords = keywords.lower()

    for words in range(len(keywords)):
        for perm in permutations(keywords.split(), words + 1):
            for ending in ending_list:
                if len(perm) == 1:
                    yield ''.join(perm) + ending
                else:
                    for separator in separator_list:
                        yield separator.join(perm) + ending


def do_product():

    keyword_list = [ word for word in do_permutations(keywords) ]

    num = 0
    while num < len(keyword_list):
        product_list = []
        for letter in keyword_list[num]:
            if letter in leet_dict:
                product_list.append(leet_dict[letter])
            else:
                product_list.append(letter)
        num += 1
        yield map(str, [ ''.join(letter) for letter in product(*product_list) ])


def write_to_file(outputfile, keywords):


    with open(outputfile, 'w') as f:
        for passwords in do_product():
            f.write('\n'.join(passwords) + '\n')
    f.close()

    with open(outputfile, 'r') as f:
        print(f'{len(f.readlines())} passwords written to {outputfile}')
    f.close()

    file_size = os.stat(outputfile)
    print(f'{outputfile} is {file_size.st_size} bytes')


parser = argparse.ArgumentParser()

if __name__ == '__main__':
    parser.add_argument("-o", "--outputfile", required=True, help="The file that the password list will be written to.")
    parser.add_argument("keywords", type=str, nargs="*", help="Keywords are computed by permutations and product. Supply at least one")
    args = parser.parse_args()

    keywords = ' '.join(args.keywords[0:])

    if args.outputfile != None:
        write_to_file(args.outputfile, keywords)
