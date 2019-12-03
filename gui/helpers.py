from PyQt5.QtGui import QIcon, QPixmap


def remove_all_widgets(layout):
    """
        This function removes all widgets from
        layout passed as an argument
    """
    while layout.count():
        child = layout.takeAt(0)
        if child.layout():
            remove_all_widgets(child)
        else:
            child.widget().deleteLater()


def prepare_icon(path_to_icon_image):
    icon = QIcon()
    pixmap = QPixmap(path_to_icon_image)
    icon.addPixmap(pixmap, QIcon.Disabled, QIcon.On)

    return icon
