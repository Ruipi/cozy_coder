from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QStackedWidget,
)

from cozy_coder.ui.pages.home_page import HomePage
from cozy_coder.ui.pages.brain_dump_page import BrainDumpPage


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cozy Coder")
        self.resize(900, 700)

        layout = QVBoxLayout(self)

        self.stack = QStackedWidget()

        layout.addWidget(self.stack)

        # Pages
        self.home_page = HomePage()
        self.brain_dump_page = BrainDumpPage()

        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.brain_dump_page)

        # Connections
        self.home_page.brain_dump_button.clicked.connect(
            lambda: self.switch_page(self.brain_dump_page)
        )

        self.brain_dump_page.back_button.clicked.connect(
            lambda: self.switch_page(self.home_page)
        )

    def switch_page(self, page):
        self.stack.setCurrentWidget(page)