import settings
from PyQt5.QtGui import QIcon

class Revealfields:
    def __init__(self, board_array=None,
                       board_height=None,
                       board_width=None,
                       matrix_of_buttons=None,
                       bomb_icon=None,
                       score=0,
                       score_label=None,
                       number_of_reveal_fields = 0
                 ):

        self._board_array = board_array
        self._board_height = board_height
        self._board_width = board_width
        self._matrix_of_buttons = matrix_of_buttons
        self._bomb_icon = QIcon(bomb_icon)
        self._score = score
        self._score_label = score_label
        self._number_of_reveal_fields = number_of_reveal_fields

    def _reveal_neighbours(self, x, y):
        if not self._board_array[x][y].revealed:
            if x not in [0, self._board_height + 1] and y not in [0, self._board_width + 1]:
                if self._board_array[x][y].value in ['1', '2', '3', '4', '5', '6', '7', '8']:
                    self._reveal_specyfied_field(x-1, y-1)
                    self._number_of_reveal_fields += 1

                    return
                if self._board_array[x][y].value == settings.VALUES_OF_BOARD_FIELDS["INITIAL_VALUE_OF_THE_FIELD"]:
                    self._reveal_specyfied_field(x-1, y-1)
                    self._number_of_reveal_fields += 1

                    self._reveal_neighbours(x - 1, y)
                    self._reveal_neighbours(x - 1, y - 1)
                    self._reveal_neighbours(x, y - 1)
                    self._reveal_neighbours(x + 1, y - 1)
                    self._reveal_neighbours(x + 1, y)
                    self._reveal_neighbours(x + 1, y + 1)
                    self._reveal_neighbours(x, y + 1)
                    self._reveal_neighbours(x - 1, y + 1)
                return
        return

    def _reveal_specyfied_field(self,x,y, sum_score=True):
        field_value = self._board_array [x+1][y+1].value
        if field_value == settings.VALUES_OF_BOARD_FIELDS["BOMB"]:
            self._matrix_of_buttons[x][y].setStyleSheet(settings.GAME_BUTTONS_COLORS["BOMB_COLOR"])
            self._matrix_of_buttons[x][y].setIcon(self._bomb_icon)

        elif field_value.isdigit():
            self._matrix_of_buttons[x][y].setStyleSheet("color: black; background-color: #C0C0C0; font: bold;")
            self._matrix_of_buttons[x][y].setText(field_value)
            if sum_score:
                self.update_score(field_value = field_value)
        else:
            self._matrix_of_buttons[x][y].setStyleSheet(settings.GAME_BUTTONS_COLORS["COLOR_OF_REVEALED_FIELD"])

        self._matrix_of_buttons[x][y].setEnabled(False)
        self._board_array[x + 1][y + 1].revealed = True

    def update_score(self, field_value):
        self._score += int(field_value)
        self._score_label.setText(str(self._score))

    def _reveal_all(self):
        for row_idx in range(self._board_height):
            for column_idx in range(self._board_width):
                if not self._board_array[row_idx+1][column_idx+1].revealed:
                    self._reveal_specyfied_field(x=row_idx,
                                                 y=column_idx,
                                                 sum_score=False)

    def _is_mine(self, x, y):

        if self._board_array [x][y].value == settings.VALUES_OF_BOARD_FIELDS["BOMB"]:
            return True
        return False
