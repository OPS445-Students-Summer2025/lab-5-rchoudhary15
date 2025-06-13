#!/usr/bin/env python3
# Author ID: rchoudhary15

def read_file_string(file_name):
    # Opens the file and reads all contents as one string
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    # Opens the file and returns a list of lines with newlines stripped
    with open(file_name, 'r') as f:
        return [line.strip() for line in f]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))

