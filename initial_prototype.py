__author__ = 'justin and raphey'

import numpy as np

blank_board = np.zeros([11, 11], dtype=int)

blue_wins_1 = np.copy(blank_board)
blue_wins_1[0] = [2] * 11

red_wins_1 = np.copy(blank_board)
red_wins_1[:, 0] = [1] * 11


def test_blue_wins_1():
    assert(check_blue_wins(blue_wins_1))


def test_red_wins_1():
    assert(not check_blue_wins(red_wins_1))


def test_neighbors():
    assert(neighbors(0, 0) == {(0, 1), (1, 0)})
    assert(neighbors(5, 5) == {(5, 6), (5, 4), (6, 5), (4, 5), (4, 6), (6, 4)})
    assert(neighbors(15, 15) == set())


def neighbors(i, j):
    neighbor_list = [(i - 1, j), (i + 1, j), (i - 1, j + 1), (i, j + 1), (i, j - 1), (i + 1, j - 1)]
    return set((x, y) for (x, y) in neighbor_list if 0 <= x < 11 and 0 <= y < 11)


def check_blue_wins(board):
    left_side = [(x, 0) for x in range(11) if board[x][0] == 2]
    explored = set(left_side) # set of coords we've visited
    frontier = left_side[:]
    while frontier:
        print(frontier)
        curr_x, curr_y = frontier.pop(0)
        if curr_y == 10:
            return True
        for i, j in neighbors(curr_x, curr_y):
            if board[i][j] == 2 and (i, j) not in explored:
                frontier.append((i, j))
            explored.add((i, j))
    return False

test_blue_wins_1()
test_red_wins_1()
