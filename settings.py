TEXT_ON_BUTTONS = {
    "START_BUTTON": "START",
    "EXIT_BUTTON": "EXIT",
    "NEXT_BUTTON": "NEXT",
    "BACK_BUTTON": "BACK",
    "BACK_TO_MENU": "BACK TO MENU"
}

MAIN_WINDOW_STYLES = "background-color: brown;"
MIN_WIDTH_OF_VERTICAL_LAYOUT = "min-width: 300px;"
START_LOGO_IMAGE = "assets/sapper.jpg"
START_LOGO_IMAGE_STYLES = MIN_WIDTH_OF_VERTICAL_LAYOUT + \
                          "border-image: url(" + START_LOGO_IMAGE + ") 1 1 1 1 stretch stretch;" + \
                          "border-width: auto;"

BOARD_SIZE = {
    "HEIGHT_MIN": 3,
    "HEIGHT_MAX": 6,
    "WIDTH_MIN": 3,
    "WIDTH_MAX": 6
}

INFORMATIVE_TEXTS = {
    "ENTER_THE_HEIGHT": "PODAJ WYSOKOŚĆ: ",
    "ENTER_THE_WIDTH": "PODAJ SZEROKOŚĆ: ",
    "ENTER_THE_NUMBER_OF_MINES": "PODAJ LICZBĘ MIN: ",
    "INFORM_ABOUT_THE_SCORE": "TWÓJ WYNIK TO: "
}

DELAY_OF_THE_CONNECTION = 0.075

SIZE_LABEL_FONT_TYPE = 'Arial'

FONT_TO_LABEL_PROPORTION = 1/4

MINIMUM_AMOUNT_OF_MINES = 1

VALUES_OF_BOARD_FIELDS = {
    "INITIAL_VALUE_OF_THE_FIELD": "",
    "BOMB": "BOMB"
}

GAME_BUTTONS_COLORS = {
    "INITIAL_COLOR": "background-color: blue;",
    "BOMB_COLOR": "background-color: #FF1730;",
    "COLOR_OF_REVEALED_FIELD": "background-color: #C0C0C0;",
}

MESSAGES_WIT_THE_RESULTS_OF_THE_GAME ={
    "WIN": "WYGRAŁEŚ !",
    "LOSE": "PRZEGRAŁEŚ !"
}

MINIMUM_WIDTH_OF_LAYOUT = 300
MINIMUM_HEIGHT_OF_THE_WHOLE_APPLICATION = 350

IMAGES_WITH_THE_ICONS_OF_FIELDS = {
    "FIELD_WITH_BOMB": "assets/bomb.png",
    "EMPTY_FIELD": "assets/empty_field.png",
    "NOT_REVEALED":  "assets/not_revealed.png"
}
SETTINGS_OF_FIELDS_WITH_VALUES = {
    "PATH_TO_ICONS": "assets/numbers/",
    "ICON_FILE_FORMAT": "jpg"
}

GAME_BUTTONS_VERSUS_RIGHT_LAYOUT_RATIO = 0.9
ICON_VERSUS_GAME_BUTTON_RATIO = 0.8
WIDTH_OF_LABEL_TEXT_VERSUS_WIDTH_OF_WHOLE_LABEL_RATIO = 0.85

SIZE_OF_FONT_VERSUS_HEIGHT_OF_THE_SPIN_BOX_RATIO = 0.4
WIDTH_OF_TEXT_VERSUS_WIDTH_OF_THE_WHOLE_SPIN_BOX_RATIO = 0.75
STYLES_OF_FONT_INSIDE_SPIN_BOX = 'font-size: {font_size}px;' \
                                 'font-family: {font_family};' \
                                 'font-weight: bold;'
