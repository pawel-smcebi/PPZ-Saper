from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLabel

import settings
from gui.adjusted_items import StartSceneButton, LogoLabel

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._main_horizontal_layout = QHBoxLayout(self)
        self._left_layout = QVBoxLayout()
        self._right_layout = QVBoxLayout()
        self._initial_widget_config()
        self.start_scene()


    def _initial_widget_config(self):
        """
            The function contains settings for the whole window
        """
        self.setStyleSheet(settings.MAIN_WINDOW_STYLES)

    def start_scene(self):

        """
            We call this function to displays the start scene
        """

        # Creating "start" and "exit" buttons
        start_button = StartSceneButton(settings.START_BUTTON_TEXT)
        self._left_layout.addWidget(start_button)
        exit_button = StartSceneButton(settings.EXIT_BUTTON_TEXT)
        self._left_layout.addWidget(exit_button)

        # There is a logo on the right side of the starting scene
        logo_label = LogoLabel()
        self._right_layout.addWidget(logo_label)

        self._main_horizontal_layout.addLayout(self._left_layout)
        self._main_horizontal_layout.addLayout(self._right_layout)
