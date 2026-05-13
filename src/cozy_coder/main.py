import os
import sys

os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
os.environ["QT_API"] = "pyside6"

from PySide6.QtWidgets import QApplication

from cozy_coder.ui.main_window import MainWindow
from cozy_coder.core.fonts import load_fonts


app = QApplication(sys.argv)

load_fonts()

window = MainWindow()
window.show()

sys.exit(app.exec())