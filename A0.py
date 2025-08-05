# -*- coding: utf-8 -*-
"""
Assignment 0 template

For submission, rename this file to "A0.py"

Answer each question in the corresponding method definition stub below
"""


def Q1(A, B):
    union = set(A) | set(B)
    intersection = set(A) & set(B)
    return union, intersection


def Q2(A, B):
    union, intersection = Q1(A, B)
    if intersection:
        return "INTERSECTING"
    return "DISJOINT"


def Q3(a, b):
    X = set(range(a))
    Y = set(range(b))
    G = set([(x, y) for x in X for y in Y])
    return X, Y, G


def Q4(E, n):
    n_successors = set()
    for edge in E.values():
        if edge[0] == n:
            n_successors.add(edge[1])
            n_successors.update(Q4(E, edge[1]))
    return n_successors


def Q5(inFile, outFile, remove):
    with open(inFile, "r") as f:
        content = f.read()
    content = content.replace(remove, "")
    with open(outFile, "w") as f:
        f.write(content)
    print("Character " + remove + " removed from " + inFile)
    print("Output written to " + outFile)


def Q6(state1, state2):
    if len(state1) != 9 or len(state2) != 9:
        print("IMPOSSIBLE")
        return
    try:
        empty = state1.index('_')
        new_empty = state2.index('_')
    except ValueError:
        print("IMPOSSIBLE")
        return
    row = empty // 3
    col = empty % 3
    new_row = new_empty // 3
    new_col = new_empty % 3
    if (new_row == row) and (new_col < col):
        print("L")
        return
    elif (new_row == row) and (new_col > col):
        print('R')
        return
    elif (new_col == col) and (new_row > row):
        print('D')
        return
    elif (new_col == col) and (new_row < row):
        print('U')
        return
    else:
        print("IMPOSSIBLE")
