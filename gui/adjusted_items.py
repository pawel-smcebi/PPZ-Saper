import threading
import time
from math import floor

from PyQt5.Qt import QSize
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QSizePolicy, QPushButton, QLabel, QSpinBox

import settings
from gui.helpers import prepare_icon

"""
    This file contains the adjusted element classes
"""

class StartSceneButton(QPushButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.setMinimumWidth(settings.MINIMUM_WIDTH_OF_LAYOUT)

class LogoLabel(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(settings.START_LOGO_IMAGE_STYLES)

class SizeLabel(QLabel):
    resized = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._resizing_enabled = False
        self._text = None
        threading.Thread(target=self._set_resizing).start()
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)

    def _set_resizing(self):
        self._text = self.text()
        self.setText("")
        self.resized.connect(self._adjust_font)
        time.sleep(settings.DELAY_OF_THE_CONNECTION)
        self._resizing_enabled = True
        self._adjust_font()
        self.setText(self._text)

    def resizeEvent(self, evt):
        self.resized.emit()

    def _adjust_font(self):
        if self._resizing_enabled:
            font_type = settings.SIZE_LABEL_FONT_TYPE
            qlabel_sizes = self.size()
            qlabel_sizes_height = qlabel_sizes.height()
            qlabel_sizes_width = qlabel_sizes.width()
            font_size = qlabel_sizes_height * settings.FONT_TO_LABEL_PROPORTION
            length_of_the_label_text = len(self.text())
            if font_size * length_of_the_label_text > \
                    qlabel_sizes_width * settings.WIDTH_OF_LABEL_TEXT_VERSUS_WIDTH_OF_WHOLE_LABEL_RATIO:
                font_size = (qlabel_sizes_width * settings.WIDTH_OF_LABEL_TEXT_VERSUS_WIDTH_OF_WHOLE_LABEL_RATIO)\
                            //length_of_the_label_text

            self.setFont(QFont(font_type, font_size, QFont.Bold))

class SizeSpinBox(QSpinBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

class GameButton(QPushButton):
    resized = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._resizing_enabled = False
        threading.Thread(target=self._set_resizing).start()
        self._initial_config()


    def _set_resizing(self):
        self.resized.connect(self.adjust_icon)
        time.sleep(settings.DELAY_OF_THE_CONNECTION)
        self._resizing_enabled = True
        self.adjust_icon()

    def _initial_config(self):
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        initial_icon = prepare_icon(
            path_to_icon_image=settings.IMAGES_WITH_THE_ICONS_OF_FIELDS["NOT_REVEALED"])
        initial_icon.addPixmap(QPixmap(settings.IMAGES_WITH_THE_ICONS_OF_FIELDS["NOT_REVEALED"]),
                               QIcon.Disabled, QIcon.On)
        self.setIcon(initial_icon)

    def resizeEvent(self, evt):
        self.resized.emit()

    def adjust_icon(self):
        if self._resizing_enabled:
            qlabel_sizes = self.size()
            qlabel_sizes_height = qlabel_sizes.height()
            qlabel_sizes_width = qlabel_sizes.width()
            self.setIconSize(QSize(floor(qlabel_sizes_height * settings.ICON_VERSUS_GAME_BUTTON_RATIO),
                                   floor(qlabel_sizes_width * settings.ICON_VERSUS_GAME_BUTTON_RATIO)))
