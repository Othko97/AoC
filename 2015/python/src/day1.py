#!/usr/bin/python3

import sys

def follow_parens(parens, start=0):
    """
    Follows instructions given in the form of
        `(` - go up one
        `)` - go down one

    Inputs:
        * parens - string to be followed
        * start  - position at start
    Outputs:
        * end    - final position
    """
    end = start
    for i in parens:
        if i == '(':
            end += 1
        if i == ')':
            end -= 1

    return end

def find_basement(parens, start=0):
    """
    Finds point where the pointer is at -1

    Inputs:
        * parens - string to be followed
        * start  - position at start
    Outputs:
        * pos    - position when pointer at -1
    """
    end = start
    for i in range(len(parens)):
        if parens[i] == '(':
            end += 1
        if parens[i] == ')':
            end -= 1
        if end == -1:
            return i + 1
    return 0


def follow_input(filename):
    """
    Wrapper for `follow_parens()` to be used on a file
    """
    with open(filename, 'r') as f:
        parens = f.read()

    return follow_parens(parens)

def input_find_basement(filename):
    """
    Wrapper for `find_basement()` to be used on a file
    """
    with open(filename, 'r') as f:
        parens = f.read()

    return find_basement(parens)

#########
# TESTS #
#########

def test_parens():
    """
    Tests for `follow_parens()`
    """
    tests = ['(())', '()()', '(((', '(()(()(', '))(((((', '())', '))(', ')))', ')())())']
    return [follow_parens(x) for x in tests]

def test_basement():
    """
    Tests for `find_basement()`
    """
    tests = [')', '()())']
    return [find_basement(x) for x in tests]


########
# MAIN #
########

if __name__ == '__main__':

    args = sys.argv

    filename = args[1]

    print(test_parens())
    print(test_basement())

    print(follow_input(filename))
    print(input_find_basement(filename))
