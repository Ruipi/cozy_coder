from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)

from cozy_coder.ui.widgets.animated_button import AnimatedButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cozy Coder")
        self.resize(900, 700)

        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setContentsMargins(80, 60, 80, 60)

        title = QLabel("cozy coder ✨")
        title.setStyleSheet("""
            font-size: 38px;
            font-family: "Quicksand";
            font-weight: bold;
        """)

        layout.addWidget(title)

        buttons = [
            "Start Focus Session",
            "Brain Dump",
            "Tiny Tasks",
            "Notes",
            "Settings"
        ]

        for text in buttons:
            layout.addWidget(AnimatedButton(text))

        layout.addStretch()