from functools import partial

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QWIDGETSIZE_MAX#, QPushButton`
from PyQt5 import QtCore

# from PyQt5.QtWidgets import QSizePolicy
# from PyQt5.QtGui import QPixmap, QIcon
from gui.helpers import prepare_icon, AdjustItems
# from PyQt5.Qt import QSize
# from PyQt5.QtCore import pyqtSignal
# from math import floor
# from threading import Thread
# import time

import settings
from board.board_generator import generate_board
from gui.adjusted_items import StartSceneButton, LogoLabel, SizeLabel, SizeSpinBox, GameButton
from gui.helpers import remove_all_widgets
from gui.revealing_fields import RevealFields


# _board_array = None

# class GameButton2(QPushButton):
#     resized = pyqtSignal()
#
#     def __init__(self, row_idx, column_idx):
#         super().__init__()
#         self._resizing_enabled = False
#         Thread(target=self._set_resizing).start()
#         self._initial_config()
#         self._row_idx = row_idx
#         self._column_idx = column_idx
#
#
#     def _set_resizing(self):
#         self.resized.connect(self.adjust_icon)
#         time.sleep(settings.DELAY_OF_THE_CONNECTION)
#         self._resizing_enabled = True
#         self.adjust_icon()
#
#     def _initial_config(self):
#         self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
#
#         initial_icon = prepare_icon(
#             path_to_icon_image=settings.IMAGES_WITH_THE_ICONS_OF_FIELDS["NOT_REVEALED"])
#         initial_icon.addPixmap(QPixmap(settings.IMAGES_WITH_THE_ICONS_OF_FIELDS["NOT_REVEALED"]),
#                                QIcon.Disabled, QIcon.On)
#         self.setIcon(initial_icon)
#
#     def resizeEvent(self, evt):
#         self.resized.emit()
#
#     def adjust_icon(self):
#         if self._resizing_enabled:
#             qlabel_sizes = self.size()
#             qlabel_sizes_height = qlabel_sizes.height()
#             qlabel_sizes_width = qlabel_sizes.width()
#             self.setIconSize(QSize(floor(qlabel_sizes_height * settings.ICON_VERSUS_GAME_BUTTON_RATIO),
#                                    floor(qlabel_sizes_width * settings.ICON_VERSUS_GAME_BUTTON_RATIO)))
#
#     def mouseReleaseEvent(self, e):
#         global _board_array
#         if e.button() == QtCore.Qt.RightButton:
#             if _board_array[self._row_idx][self._column_idx].flagged == True:
#                 path_to_icon_image = settings.IMAGES_WITH_THE_ICONS_OF_FIELDS["NOT_REVEALED"]
#                 icon = prepare_icon(path_to_icon_image=path_to_icon_image)
#                 self.setIcon(icon)
#                 self.adjust_icon()
#                 _board_array[self._row_idx][self._column_idx].flagged = False
#             else:
#                 path_to_icon_image = settings.IMAGES_WITH_THE_ICONS_OF_FIELDS["FLAGGED"]
#                 icon = prepare_icon(path_to_icon_image=path_to_icon_image)
#                 self.setIcon(icon)
#                 self.adjust_icon()
#                 _board_array[self._row_idx][self._column_idx].flagged = True
#
#
#         elif e.button() == QtCore.Qt.LeftButton:
#             _board_array[self._row_idx][self._column_idx].flagged = False
#             global _game_button_click
#             _game_button_click(self._row_idx, self._column_idx)
#             self.setDown(False)



class MainWidget(QWidget, RevealFields):
    def __init__(self):
        QWidget.__init__(self)
        RevealFields.__init__(self,
                              path_to_icons_with_values=settings.SETTINGS_OF_FIELDS_WITH_VALUES["PATH_TO_ICONS"],
                              file_format_of_icons_with_values=settings.SETTINGS_OF_FIELDS_WITH_VALUES["ICON_FILE_FORMAT"])
        self._main_horizontal_layout = QHBoxLayout(self)
        self._left_layout = QVBoxLayout()
        self._widget_of_left_layout = QWidget()
        self._right_layout = QVBoxLayout()
        self._widget_of_right_layout = QWidget()
        self._board_height = None
        self._board_width = None
        self._number_of_mines = None
        self._board_array = None
        self._score = 0
        self._score_label = None
        self._matrix_of_buttons = []
        self._number_of_reveal_fields = 0
        self._initial_widget_config()
        self.start_scene()

    def _go_to_scene(self,
                     scene_function,
                     remove_items_left_layout=True,
                     remove_items_right_layout=True):

        """
            If 'remove_items_left_layout' is set as true
            '_go_to_scene' function removes all visible elements
            contained in self._left_layout

            If 'remove_items_right_layout' is set as true
            '_go_to_scene' function removes all visible elements
            contained in self._right_layout

            '_go_to_scene' function always execute
            a specific function for a given scene,
            which is passed as an argument('scene_function')
        """
        if remove_items_left_layout:
            remove_all_widgets(layout=self._left_layout)

        if remove_items_right_layout:
            remove_all_widgets(layout=self._right_layout)

        left_width_tmp = self._widget_of_left_layout.width()
        left_height_tmp = self._widget_of_left_layout.height()

        right_width_tmp = self._widget_of_right_layout.width()
        right_height_tmp = self._widget_of_right_layout.height()

        whole_width_tmp = self.width()
        whole_height_tmp = self.height()

        scene_function()

        self._widget_of_left_layout.setFixedWidth(left_width_tmp)
        self._widget_of_left_layout.setFixedHeight(left_height_tmp)
        self._widget_of_left_layout.setMaximumSize(QWIDGETSIZE_MAX, QWIDGETSIZE_MAX)
        self._widget_of_left_layout.setMinimumSize(0, 0)

        self._widget_of_right_layout.setFixedWidth(right_width_tmp)
        self._widget_of_right_layout.setFixedHeight(right_height_tmp)
        self._widget_of_right_layout.setMaximumSize(QWIDGETSIZE_MAX, QWIDGETSIZE_MAX)
        self._widget_of_right_layout.setMinimumSize(0, 0)


        self.setFixedWidth(whole_width_tmp)
        self.setFixedHeight(whole_height_tmp)
        self.setMaximumSize(QWIDGETSIZE_MAX, QWIDGETSIZE_MAX)


    def _game_scene(self):
        """
            We call this function to display the scene
            where we play minesweeper
        """
        self._matrix_of_buttons.clear()
        self._score = self._number_of_mines
        self._number_of_reveal_fields = 0
        self._create_game_board()

        label_with_text_about_score = SizeLabel(settings.INFORMATIVE_TEXTS["INFORM_ABOUT_THE_SCORE"])
        self._left_layout.addWidget(label_with_text_about_score)
        self._score_label = SizeLabel(str(self._score))
        self._left_layout.addWidget(self._score_label)

        end_game_button = StartSceneButton(settings.TEXT_ON_BUTTONS["BACK_TO_MENU"])
        end_game_button_click_function = lambda: self._go_to_scene(scene_function=self.start_scene)
        end_game_button.clicked.connect(end_game_button_click_function)
        self._left_layout.addWidget(end_game_button)

    def final_message_scene(self, message):
        """
            When the game is over we call this function
            to display scene with final message('message')
        """
        label_with_text_about_score = SizeLabel(message)
        self._left_layout.addWidget(label_with_text_about_score)

        end_game_button = StartSceneButton(settings.TEXT_ON_BUTTONS["BACK_TO_MENU"])
        end_game_button_click_function = lambda: self._go_to_scene(scene_function=self.start_scene)
        end_game_button.clicked.connect(end_game_button_click_function)
        self._left_layout.addWidget(end_game_button)


    def _game_button_click(self, row_idx, column_idx):
        """
           This function determines an action
           for particular button with specified indexes
           (row_idx, column_idx)
        """

        if self._is_flagged(row_idx, column_idx) is False:
            if self._is_mine(row_idx, column_idx):
                self._reveal_all()
                final_scene = lambda: self.final_message_scene(
                    message=settings.MESSAGES_WIT_THE_RESULTS_OF_THE_GAME["LOSE"])
                self._go_to_scene(scene_function=final_scene,
                                  remove_items_left_layout=True,
                                  remove_items_right_layout=False)

            else:
                self._reveal_neighbours(row_idx, column_idx)
                if self._number_of_reveal_fields == self._board_height * self._board_width - self._number_of_mines:
                    self._reveal_all()
                    final_scene = lambda: self.final_message_scene(
                        message=settings.MESSAGES_WIT_THE_RESULTS_OF_THE_GAME["WIN"])
                    self._go_to_scene(scene_function=final_scene,
                                      remove_items_left_layout=True,
                                      remove_items_right_layout=False)

    def _handle_right_click(self, row_idx, column_idx):
        if self._board_array[row_idx][column_idx].flagged == True:
            path_to_icon_image = settings.IMAGES_WITH_THE_ICONS_OF_FIELDS["NOT_REVEALED"]
            icon = prepare_icon(path_to_icon_image=path_to_icon_image)
            self._matrix_of_buttons[row_idx][column_idx].setIcon(icon)
            self._matrix_of_buttons[row_idx][column_idx].adjust_icon()
            self._board_array[row_idx][column_idx].flagged = False
            self._score += 1
            self._score_label.setText(str(self._score))

        else:
            path_to_icon_image = settings.IMAGES_WITH_THE_ICONS_OF_FIELDS["FLAGGED"]
            icon = prepare_icon(path_to_icon_image=path_to_icon_image)
            self._matrix_of_buttons[row_idx][column_idx].setIcon(icon)
            self._matrix_of_buttons[row_idx][column_idx].adjust_icon()
            self._board_array[row_idx][column_idx].flagged = True
            self._score -= 1
            self._score_label.setText(str(self._score))

    def _create_game_board(self):
        """
            This function creates the game board
            with previously given dimensions(self._board_height, self._board_width).
            The game board contains a specific number of mines(self._number_of_mines).
            The board consists of buttons (GameButton).
        """

        self._board_array = generate_board(height=self._board_height,
                                           width=self._board_width,
                                           mine_amount=self._number_of_mines)

        minimum_height_of_single_button = \
            (settings.GAME_BUTTONS_VERSUS_RIGHT_LAYOUT_RATIO *
             settings.MINIMUM_HEIGHT_OF_THE_WHOLE_APPLICATION) // self._board_height
        minimum_width_of_single_button =\
            (settings.GAME_BUTTONS_VERSUS_RIGHT_LAYOUT_RATIO *
             settings.MINIMUM_WIDTH_OF_LAYOUT) // self._board_width

        for row_idx in range(self._board_height):
            row_of_buttons_gui = QHBoxLayout()
            row_of_buttons_list = []
            for column_idx in range(self._board_width):
                game_button = GameButton()

                game_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                game_button_right_click = partial(self._handle_right_click,
                                                     row_idx=row_idx,
                                                     column_idx=column_idx)
                game_button.customContextMenuRequested.connect(game_button_right_click)

                game_button.setMinimumHeight(minimum_height_of_single_button)
                game_button.setMinimumWidth(minimum_width_of_single_button)
                game_button_click_function = partial(self._game_button_click,
                                                     row_idx=row_idx,
                                                     column_idx=column_idx)
                game_button.clicked.connect(game_button_click_function)
                row_of_buttons_list.append(game_button)
                row_of_buttons_gui.addWidget(game_button)

            self._matrix_of_buttons.append(row_of_buttons_list)
            self._right_layout.addLayout(row_of_buttons_gui)

    def _mine_amount_scene(self):
        """
            We call this function to display the scene
            with determining the number of mines
        """

        number_of_mines_label = SizeLabel(settings.INFORMATIVE_TEXTS["ENTER_THE_NUMBER_OF_MINES"])
        self._left_layout.addWidget(number_of_mines_label)

        minimum_number_of_mines = settings.MINIMUM_AMOUNT_OF_MINES
        maximum_number_of_mines = (self._board_height * self._board_width) - 1

        number_of_mines_spin_box = SizeSpinBox(minimum=minimum_number_of_mines,
                                               maximum=maximum_number_of_mines)
        self._left_layout.addWidget(number_of_mines_spin_box)
        default_number_of_mines = int((minimum_number_of_mines + maximum_number_of_mines) ** 0.5)
        number_of_mines_spin_box.setValue(default_number_of_mines)

        next_button = StartSceneButton(settings.TEXT_ON_BUTTONS["NEXT_BUTTON"])
        next_button_click_function = lambda: [
            self._get_number_of_mines(number_of_mines_spin_box=number_of_mines_spin_box),
            self._go_to_scene(scene_function=self._game_scene)]
        next_button.clicked.connect(next_button_click_function)
        self._left_layout.addWidget(next_button)

        back_button = StartSceneButton(settings.TEXT_ON_BUTTONS["BACK_BUTTON"])
        back_button_click_function = lambda: self._go_to_scene(scene_function=self._sapper_size_board_scene,
                                                               remove_items_left_layout=True,
                                                               remove_items_right_layout=False)
        back_button.clicked.connect(back_button_click_function)
        self._left_layout.addWidget(back_button)

    def _get_board_dimensions(self,
                              height_spin_box,
                              width_spin_box):
        """
            This function assigns height and width from spin boxes
            to 'self._board_height' and 'self._board_width' variables
        """
        self._board_height = height_spin_box.value()
        self._board_width = width_spin_box.value()

    def _get_number_of_mines(self, number_of_mines_spin_box):
        """
            This function assigns number of mines from spin box
            to 'self._number_of_mines' variable
        """
        self._number_of_mines = number_of_mines_spin_box.value()
        self._number_of_placed_flags = self._number_of_mines

    def _sapper_size_board_scene(self):

        """
            We call this function to display the scene
            with determining the height and length of the game board
        """

        height_label = SizeLabel(settings.INFORMATIVE_TEXTS["ENTER_THE_HEIGHT"])
        self._left_layout.addWidget(height_label)
        height_spin_box = SizeSpinBox(minimum=settings.BOARD_SIZE["HEIGHT_MIN"],
                                      maximum=settings.BOARD_SIZE["HEIGHT_MAX"])

        self._left_layout.addWidget(height_spin_box)

        width_label = SizeLabel(settings.INFORMATIVE_TEXTS["ENTER_THE_WIDTH"])
        self._left_layout.addWidget(width_label)
        width_spin_box = SizeSpinBox(minimum=settings.BOARD_SIZE["WIDTH_MIN"],
                                     maximum=settings.BOARD_SIZE["WIDTH_MAX"])
        self._left_layout.addWidget(width_spin_box)

        if self._board_height:
            height_spin_box.setValue(self._board_height)
            width_spin_box.setValue(self._board_width)

        next_button = StartSceneButton(settings.TEXT_ON_BUTTONS["NEXT_BUTTON"])
        next_button_click_function = lambda: [self._get_board_dimensions(height_spin_box=height_spin_box,
                                                                         width_spin_box=width_spin_box),
                                              self._go_to_scene(scene_function=self._mine_amount_scene,
                                                                remove_items_left_layout=True,
                                                                remove_items_right_layout=False)]
        next_button.clicked.connect(next_button_click_function)
        self._left_layout.addWidget(next_button)

        back_button = StartSceneButton(settings.TEXT_ON_BUTTONS["BACK_BUTTON"])
        back_button_click_function = lambda: [self._get_board_dimensions(height_spin_box=height_spin_box,
                                                                         width_spin_box=width_spin_box),
                                              self._go_to_scene(scene_function=self.start_scene)]
        back_button.clicked.connect(back_button_click_function)
        self._left_layout.addWidget(back_button)

    def _initial_widget_config(self):
        """
            The function contains settings for the whole window
        """
        self.setStyleSheet(settings.MAIN_WINDOW_STYLES)
        self.setMinimumHeight(settings.MINIMUM_HEIGHT_OF_THE_WHOLE_APPLICATION)
        self._widget_of_left_layout.setLayout(self._left_layout)
        self._widget_of_right_layout.setLayout(self._right_layout)
        self._main_horizontal_layout.addWidget(self._widget_of_left_layout)
        self._main_horizontal_layout.addWidget(self._widget_of_right_layout)

    def start_scene(self):

        """
            We call this function to display the start scene
        """

        # Creating "start" and "exit" buttons
        start_button = StartSceneButton(settings.TEXT_ON_BUTTONS["START_BUTTON"])
        start_button_click_function = lambda: self._go_to_scene(scene_function=self._sapper_size_board_scene,
                                                                remove_items_left_layout=True,
                                                                remove_items_right_layout=False)
        start_button.clicked.connect(start_button_click_function)
        self._left_layout.addWidget(start_button)

        # start_button = MyButton()
        # self._left_layout.addWidget(start_button)

        exit_button = StartSceneButton(settings.TEXT_ON_BUTTONS["EXIT_BUTTON"])
        exit_button_click_function = self.close
        exit_button.clicked.connect(exit_button_click_function)
        self._left_layout.addWidget(exit_button)

        # There is a logo on the right side of the starting scene
        logo_label = LogoLabel()
        self._right_layout.addWidget(logo_label)