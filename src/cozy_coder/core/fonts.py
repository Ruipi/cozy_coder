from PySide6.QtGui import QFontDatabase


def load_fonts():
    QFontDatabase.addApplicationFont(
        "assets/fonts/Quicksand-Bold.ttf"
    )

    QFontDatabase.addApplicationFont(
        "assets/fonts/JetBrainsMono-Regular.ttf"
    )