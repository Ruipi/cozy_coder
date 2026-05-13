from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)

from cozy_coder.ui.widgets.animated_button import AnimatedButton


class BrainDumpPage(QWidget):

    def __init__(self):
        super().__init__()

        self.back_button = AnimatedButton("← Back")

        layout = QVBoxLayout(self)

        title = QLabel("Brain Dump")

        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setStyleSheet("""
            font-size: 36px;
            font-family: "Quicksand";
        """)

        layout.addWidget(title)

        layout.addStretch()

        layout.addWidget(
            self.back_button,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout.addStretch()