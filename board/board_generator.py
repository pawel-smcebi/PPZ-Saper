from random import choice
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

    indexes_of_fields = []

    for i in range(1, height + 1):
        for j in range(1, width + 1):
            indexes_of_fields.append((i, j))

    # Adding mines, coordinates of the mines are random.
    for i in range(mine_amount):
        coordinates = choice(indexes_of_fields)
        row_index, column_index = coordinates
        indexes_of_fields.remove(coordinates)

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
    for row_index in range(1, height + 1):
        for column_index in range(1, width + 1):
            if board[row_index][column_index].nearby_mines > 0:
                if board[row_index][column_index].value != VALUES_OF_BOARD_FIELDS["BOMB"]:
                    board[row_index][column_index].value = str(board[row_index][column_index].nearby_mines)

    return board
