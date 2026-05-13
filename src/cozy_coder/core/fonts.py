from PySide6.QtGui import QFontDatabase


def load_fonts():
    QFontDatabase.addApplicationFont(
        "assets/fonts/Quicksand-Regular.ttf"
    )

    QFontDatabase.addApplicationFont(
        "assets/fonts/JetBrainsMono-Regular.ttf"
    )