from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)


class BasePage(QWidget):

    def __init__(self, title: str):
        super().__init__()

        self.page_layout = QVBoxLayout(self)

        self.page_layout.setContentsMargins(
            50,
            40,
            50,
            40
        )

        self.page_layout.setSpacing(24)

        title_label = QLabel(title)

        title_label.setAlignment(
            Qt.AlignmentFlag.AlignLeft
        )

        title_label.setStyleSheet("""
            font-size: 32px;
            font-family: "Quicksand";
            font-weight: bold;
            color: #F3EFFF;
            margin-bottom: 20px;
        """)

        self.page_layout.addWidget(title_label)