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