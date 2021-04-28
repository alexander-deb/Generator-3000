import argparse
import getopt
import os
import re
import shelve
import sys

from collections import OrderedDict
from random import choices, choice


class Generator3000:

    def __init__(self):
        pass

    def read_args(self):
        '''
        Function that reads command line arguments
        '''
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--seed',
            type=str,
            default='NULL_WRD',
            help='Beginning word'
        )
        parser.add_argument(
            '--model',
            type=str,
            default='model.py',
            help='Path to the trained model file'
        )
        parser.add_argument(
            '--length',
            type=int,
            default='5',
            help='Length of generated sequence'
        )
        parser.add_argument(
            '--output',
            type=str,
            default=sys.stdout,
            help='File which will be used to put generated sequence'
        )

        arguments = parser.parse_args()
        self.seed = arguments.seed
        self.length = arguments.length - 1
        self.model = arguments.model
        self.output = arguments.output

    def generate(self):
        '''
        Function that generates sequence of words from trained model
        '''
        with shelve.open(self.model) as BIG_DICT:
            self.seed = self.seed if self.seed != 'NULL_WRD' else choice(
                list(BIG_DICT.keys()))
            output = self.seed + " "
            while self.length > 0:
                try:
                    vals = BIG_DICT[self.seed].values()
                    self.seed = choices(list(BIG_DICT[self.seed].keys()), weights=[
                                        item / sum(list(vals)) for item in list(vals)])[0]
                    output += self.seed + " "
                    self.length -= 1
                except KeyError:
                    self.seed = choice(list(BIG_DICT.keys()))
        if not self.output == sys.stdout:
            with open(self.output, "w") as file:
                print(output, file=file)
        else:
            print(output)


def main():
    generator = Generator3000()
    generator.read_args()
    generator.generate()


if __name__ == "__main__":
    main()
