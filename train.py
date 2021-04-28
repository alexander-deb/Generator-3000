import argparse
import os
import re
import shelve
import sys

from collections import Counter, defaultdict


class Train:
    def __init__(self):
        pass

    def read_args(self):
        '''
        Function that reads command line arguments
        '''
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--input-dir',
            type=str,
            default=sys.path[0],
            help='Directory, with documents for training models'
        )
        parser.add_argument(
            '--model',
            type=str,
            default='model.py',
            help='Name for trained model file'
        )
        parser.add_argument(
            '--lc',
            required=False,
            const=True,
            nargs='?',
            default=False,
            help='Makes lowercase text for model')
        arguments = parser.parse_args()
        self.lc = arguments.lc
        self.input_dir = arguments.input_dir
        self.model = arguments.model

    def run_trainer(self):
        '''
        Function that trains model and writes it into a file.
        '''
        # returns the names of the files in the directory data as a list
        list_of_files = os.listdir(self.input_dir)

        # opening database for saving model
        BIG_DICT = defaultdict(Counter)
        # reading text from all files
        for filename in list_of_files:
            with open(f"{self.input_dir}/{filename}", "r") as current_file:
                lines = current_file.readlines()
                for line in lines:
                    if self.lc:
                        line = line.lower()
                    line = re.sub(r"\d+", '', line)  # remove all numbers
                    line = re.findall(r"\w+", line)  # splitting line
                    # saving model
                    for i in range(len(line)-1):
                        BIG_DICT[line[i]][line[i+1]] += 1
        with shelve.open(self.model) as file:
            for i in BIG_DICT.keys():
                file[i] = BIG_DICT[i]


def main():
    model = Train()
    model.read_args()
    model.run_trainer()


if __name__ == "__main__":
    main()
