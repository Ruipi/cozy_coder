from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QSizePolicy,
    QSpacerItem,
)

from cozy_coder.ui.widgets.animated_button import AnimatedButton


class HomePage(QWidget):

    def __init__(self):
        super().__init__()

        self.brain_dump_button = AnimatedButton("Brain Dump")
        self.tasks_button = AnimatedButton("Tiny Tasks")
        self.notes_button = AnimatedButton("Notes")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        outer = QVBoxLayout()
        outer.setSpacing(16)
        outer.setContentsMargins(120, 60, 120, 60)

        outer.addSpacerItem(
            QSpacerItem(
                20,
                40,
                QSizePolicy.Policy.Minimum,
                QSizePolicy.Policy.Expanding
            )
        )

        title = QLabel("cozy coder ✨")

        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setStyleSheet("""
            QLabel {
                font-size: 40px;
                font-family: "Quicksand";
                font-weight: bold;
                color: #5B4B4B;
            }
        """)

        outer.addWidget(title)

        buttons = [
            AnimatedButton("Start Focus Session"),
            self.brain_dump_button,
            self.tasks_button,
            self.notes_button,
            AnimatedButton("Settings"),
        ]

        for btn in buttons:
            btn.setFixedSize(320, 60)

            outer.addWidget(
                btn,
                alignment=Qt.AlignmentFlag.AlignHCenter
            )

        outer.addSpacerItem(
            QSpacerItem(
                20,
                40,
                QSizePolicy.Policy.Minimum,
                QSizePolicy.Policy.Expanding
            )
        )

        layout.addLayout(outer)