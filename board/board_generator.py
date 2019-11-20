from random import randint
from settings import VALUES_OF_BOARD_FIELDS
from board.helpers import InitialValuesOfField


def generate_board(height, width, mine_amount):
    # Array will have dimensions increased by 1 in order to
    # avoid collisions resulting from exceeding the range of an array
    # while updating the neighbours.
    board = []

    for i in range(height + 2):
        tmp = [InitialValuesOfField() for j in range(width + 2)]
        board.append(tmp)

    # Adding mines, coordinates of the mines are random.
    for i in range(mine_amount):
        row_index = randint(1, height - 1)
        column_index = randint(1, width - 1)
        while board[row_index][column_index].value == VALUES_OF_BOARD_FIELDS["BOMB"]:
            row_index = randint(1, height - 1)
            column_index = randint(1, width - 1)

        board[row_index][column_index].value = VALUES_OF_BOARD_FIELDS["BOMB"]

        board[row_index - 1][column_index].nearby_mines += 1
        board[row_index - 1][column_index - 1].nearby_mines += 1
        board[row_index][column_index - 1].nearby_mines += 1
        board[row_index + 1][column_index - 1].nearby_mines += 1
        board[row_index + 1][column_index].nearby_mines += 1
        board[row_index + 1][column_index + 1].nearby_mines += 1
        board[row_index][column_index + 1].nearby_mines += 1
        board[row_index - 1][column_index + 1].nearby_mines += 1

    # Change of particular fields values depending on
    # the number of mines near the specified field.
    for x in range(1, height + 1):
        for y in range(1, width + 1):
            if board[x][y].nearby_mines > 0 and board[x][y].value != VALUES_OF_BOARD_FIELDS["BOMB"]:
                board[x][y].value = str(board[x][y].nearby_mines)

    return board
