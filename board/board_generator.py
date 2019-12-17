from random import choice
from settings import VALUES_OF_BOARD_FIELDS
from board.helpers import InitialValuesOfField


def pos_correct(height, width, x, y):
    if x >= 0 and x < height:
        if y >= 0 and y < width:
            return True
    return False

def generate_board(height, width, mine_amount):
    # Array will have dimensions increased by 1 in order to
    # avoid collisions resulting from exceeding the range of an array
    # while updating the neighbours.
    board = []

    for i in range(0, height):
        tmp = [InitialValuesOfField() for j in range(0, width)]
        board.append(tmp)

    indexes_of_fields = []

    for i in range(0, height):
        for j in range(0, width):
            indexes_of_fields.append((i, j))

    # Adding mines, coordinates of the mines are random.
    for i in range(mine_amount):
        coordinates = choice(indexes_of_fields)
        x, y = coordinates
        indexes_of_fields.remove(coordinates)
        board[x][y].value = VALUES_OF_BOARD_FIELDS["BOMB"]

    for x in range(0, height):
        for y in range(0, width):
            mines_around = 0
            if (pos_correct(height, width, x-1, y) is True) and (board[x-1][y].value == VALUES_OF_BOARD_FIELDS["BOMB"]):
                mines_around += 1
            if (pos_correct(height, width, x-1, y-1) is True) and (board[x-1][y-1].value == VALUES_OF_BOARD_FIELDS["BOMB"]):
                mines_around += 1
            if (pos_correct(height, width, x, y-1) is True) and (board[x][y-1].value == VALUES_OF_BOARD_FIELDS["BOMB"]):
                mines_around += 1
            if (pos_correct(height, width, x+1, y-1) is True) and (board[x+1][y-1].value == VALUES_OF_BOARD_FIELDS["BOMB"]):
                mines_around += 1
            if (pos_correct(height, width, x+1, y) is True) and (board[x+1][y].value == VALUES_OF_BOARD_FIELDS["BOMB"]):
                mines_around += 1
            if (pos_correct(height, width, x+1, y+1) is True) and (board[x+1][y+1].value == VALUES_OF_BOARD_FIELDS["BOMB"]):
                mines_around += 1
            if (pos_correct(height, width, x, y+1) is True) and (board[x][y+1].value == VALUES_OF_BOARD_FIELDS["BOMB"]):
                mines_around += 1
            if (pos_correct(height, width, x-1, y+1) is True) and (board[x-1][y+1].value == VALUES_OF_BOARD_FIELDS["BOMB"]):
                mines_around += 1

            board[x][y].nearby_mines = mines_around

    # Change of particular fields values depending on
    # the number of mines near the specified field.
    for x in range(0, height):
        for y in range(0, width):
            if board[x][y].nearby_mines > 0:
                if board[x][y].value != VALUES_OF_BOARD_FIELDS["BOMB"]:
                    board[x][y].value = str(board[x][y].nearby_mines)

    return board
