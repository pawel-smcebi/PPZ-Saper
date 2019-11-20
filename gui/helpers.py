def remove_all_widgets(layout):
    """
        This function removes all widgets from
        layout passed as an argument
    """
    while layout.count():
        child = layout.takeAt(0)
        child.widget().deleteLater()