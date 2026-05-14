from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)


class BasePage(QWidget):

    def __init__(self, title: str):
        super().__init__()

        layout = QVBoxLayout(self)

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

        layout.addWidget(title_label)