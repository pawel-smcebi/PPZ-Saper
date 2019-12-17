import settings
from gui.helpers import prepare_icon

class RevealFields:
    def __init__(self, board_array=None,
                 board_height=None,
                 board_width=None,
                 matrix_of_buttons=None,
                 score=0,
                 score_label=None,
                 path_to_icons_with_values=None,
                 file_format_of_icons_with_values=None,
                 number_of_reveal_fields=0
                 ):

        self._board_array = board_array
        self._board_height = board_height
        self._board_width = board_width
        self._matrix_of_buttons = matrix_of_buttons
        self._score = score
        self._score_label = score_label
        self._path_to_icons_with_values = path_to_icons_with_values
        self._file_format_of_icons_with_values = file_format_of_icons_with_values
        self._number_of_reveal_fields = number_of_reveal_fields
        self._rev_all = False

    def _is_pos_correct(self, x, y):
        if x >= 0 and x < self._board_height:
            if y >= 0 and y < self._board_width:
                return True
        return False

    def _reveal_neighbours(self, x, y):
        if self._is_pos_correct(x, y) is True:
            if self._board_array[x][y].revealed is False and self._board_array[x][y].flagged is False:
                if self._board_array[x][y].value in map(str, range(1, 9)):
                    self._reveal_specyfied_field(x, y)
                    return

                if self._board_array[x][y].value == settings.VALUES_OF_BOARD_FIELDS["INITIAL_VALUE_OF_THE_FIELD"]:
                    self._reveal_specyfied_field(x, y)

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
        return

    def _reveal_specyfied_field(self, x, y):
        if self._rev_all is True:
            self._board_array[x][y].flagged = False

        if self._board_array[x][y].flagged is False:
            field_value = self._board_array[x][y].value
            if field_value == settings.VALUES_OF_BOARD_FIELDS["BOMB"]:
                path_to_icon_image = settings.IMAGES_WITH_THE_ICONS_OF_FIELDS["FIELD_WITH_BOMB"]
            elif field_value.isdigit():
                self._number_of_reveal_fields += 1
                path_to_icon_image = self._path_to_icons_with_values + \
                                          field_value + "." + self._file_format_of_icons_with_values
            else:
                self._number_of_reveal_fields += 1
                path_to_icon_image = settings.IMAGES_WITH_THE_ICONS_OF_FIELDS["EMPTY_FIELD"]

            icon = prepare_icon(path_to_icon_image=path_to_icon_image)
            self._matrix_of_buttons[x][y].setIcon(icon)
            self._matrix_of_buttons[x][y].adjust_icon()
            self._matrix_of_buttons[x][y].setEnabled(False)
            self._board_array[x][y].revealed = True
        else:
            return

    def update_score(self, field_value):
        self._score += int(field_value)
        self._score_label.setText(str(self._score))

    def _reveal_all(self):
        self._rev_all = True
        for row_idx in range(self._board_height):
            for column_idx in range(self._board_width):
                if self._board_array[row_idx][column_idx].flagged is True:
                    self._board_array[row_idx][column_idx].flagged = False
                if not self._board_array[row_idx][column_idx].revealed:
                    self._reveal_specyfied_field(x=row_idx,
                                                 y=column_idx,)

    def _is_mine(self, x, y):
        if self._board_array [x][y].value == settings.VALUES_OF_BOARD_FIELDS["BOMB"]:
            return True
        return False

    def _is_flagged(self, x, y):
        if self._board_array [x][y].flagged is True:
            return True
        return False
