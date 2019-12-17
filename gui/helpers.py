from PyQt5.QtGui import QIcon, QPixmap
from math import floor

def remove_all_widgets(layout):
    """
        This function removes all widgets from
        layout passed as an argument.
    """
    while layout.count():
        child = layout.takeAt(0)
        if child.layout():
            remove_all_widgets(child)
        else:
            child.widget().deleteLater()


def prepare_icon(path_to_icon_image):
    """
        This function prepares QIcon with
        an image whose path was passed as an argument ('path_to_icon_image')
        Icon images should be the same no matter a button is disabled or not.
    """

    icon = QIcon()
    pixmap = QPixmap(path_to_icon_image)
    icon.addPixmap(pixmap, QIcon.Disabled, QIcon.On)

    return icon


class AdjustItems:
    def _calculate_font_size(self, height_ratio, width_ratio):
        item_sizes = self.size()
        item_height = item_sizes.height()
        item_width = item_sizes.width()
        font_size = item_height * height_ratio
        length_of_text = len(self.text())
        if font_size * length_of_text > item_width * width_ratio:
            font_size = (item_width * width_ratio) // length_of_text

        font_size = floor(font_size)
        return font_size
