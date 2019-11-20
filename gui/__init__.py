from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLabel

import settings
from gui.adjusted_items import StartSceneButton, LogoLabel, SizeLabel, SizeSpinBox
from gui.helpers import remove_all_widgets

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._main_horizontal_layout = QHBoxLayout(self)
        self._left_layout = QVBoxLayout()
        self._right_layout = QVBoxLayout()
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

        scene_function()

    def _mine_amount_scene(self):
        print("_mine_amount_scene")
        pass

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


        next_button = StartSceneButton(settings.TEXT_ON_BUTTONS["NEXT_BUTTON"])
        next_button_click_function = lambda: self._go_to_scene(scene_function=self._mine_amount_scene,
                                                               remove_items_left_layout=True,
                                                               remove_items_right_layout=False)
        next_button.clicked.connect(next_button_click_function)
        self._left_layout.addWidget(next_button)

        back_button = StartSceneButton(settings.TEXT_ON_BUTTONS["BACK_BUTTON"])
        back_button_click_function = lambda: self._go_to_scene(scene_function=self.start_scene)
        back_button.clicked.connect(back_button_click_function)
        self._left_layout.addWidget(back_button)

    def _initial_widget_config(self):
        """
            The function contains settings for the whole window
        """
        self.setStyleSheet(settings.MAIN_WINDOW_STYLES)
        self._main_horizontal_layout.addLayout(self._left_layout)
        self._main_horizontal_layout.addLayout(self._right_layout)

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

        exit_button = StartSceneButton(settings.TEXT_ON_BUTTONS["EXIT_BUTTON"])
        exit_button_click_function = self.close
        exit_button.clicked.connect(exit_button_click_function)
        self._left_layout.addWidget(exit_button)

        # There is a logo on the right side of the starting scene
        logo_label = LogoLabel()
        self._right_layout.addWidget(logo_label)

