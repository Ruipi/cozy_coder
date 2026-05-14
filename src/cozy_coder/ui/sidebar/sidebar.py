from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
)

from cozy_coder.ui.widgets.animated_button import AnimatedButton


class Sidebar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedWidth(240)

        self.setStyleSheet("""
            background-color: #2B2039;
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 40, 20, 20)
        layout.setSpacing(12)

        self.focus_btn = AnimatedButton("Focus")
        self.tasks_btn = AnimatedButton("Tasks")
        self.poems_btn = AnimatedButton("Poems")
        self.reading_btn = AnimatedButton("Reading")
        self.tarot_btn = AnimatedButton("Tarot")
        self.meditation_btn = AnimatedButton("Meditation")
        self.calendar_btn = AnimatedButton("Calendar")

        buttons = [
            self.focus_btn,
            self.tasks_btn,
            self.poems_btn,
            self.reading_btn,
            self.tarot_btn,
            self.meditation_btn,
            self.calendar_btn,
        ]

        for btn in buttons:
            btn.setMinimumHeight(50)
            layout.addWidget(btn)

        layout.addStretch()