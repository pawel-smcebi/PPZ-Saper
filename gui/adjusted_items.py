from PyQt5.QtWidgets import QSizePolicy, QPushButton, QLabel
import settings

"""
    This file contains the adjusted element classes
"""

class StartSceneButton(QPushButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.setStyleSheet(settings.MIN_WIDTH_OF_VERTICAL_LAYOUT)

class LogoLabel(QLabel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(settings.START_LOGO_IMAGE_STYLES)
