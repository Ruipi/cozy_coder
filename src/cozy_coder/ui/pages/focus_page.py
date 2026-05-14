from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QScrollArea,
)

from cozy_coder.ui.widgets.session_card import (
    SessionCard
)

from cozy_coder.services.focus_service import (
    get_focus_sessions
)

from cozy_coder.ui.pages.base_page import BasePage
from cozy_coder.ui.widgets.focus_timer import FocusTimer


class FocusPage(BasePage):

    def __init__(self):
        super().__init__("Focus Time")

        content = QWidget()

        content_layout = QHBoxLayout(content)

        content_layout.setSpacing(30)

        # LEFT SIDE
        left_layout = QVBoxLayout()

        self.timer = FocusTimer()

        self.timer.session_saved.connect(
            self.load_sessions
        )

        left_layout.addWidget(
            self.timer,
            alignment=Qt.AlignmentFlag.AlignTop
        )

        left_layout.addStretch()

        # RIGHT SIDE
        history_card = QWidget()

        history_card.setStyleSheet("""
            background-color: #342545;
            border-radius: 24px;
        """)

        history_card.setMinimumWidth(350)

        history_layout = QVBoxLayout(history_card)

        history_title = QLabel("Today's Sessions")

        history_title.setStyleSheet("""
            font-size: 24px;
            font-family: "Quicksand";
            font-weight: bold;
            color: white;
        """)

        history_layout.addWidget(history_title)

        # Scroll area
        self.history_scroll = QScrollArea()

        self.history_content = QWidget()

        self.history_layout = QVBoxLayout(
            self.history_content
        )

        self.history_layout.setSpacing(12)

        self.history_layout.addStretch()

        self.history_scroll.setWidget(
            self.history_content
        )

        self.history_scroll.setWidgetResizable(True)

        self.history_scroll.setStyleSheet("""
            border: none;
            background: transparent;
        """)

        history_layout.addWidget(self.history_scroll)

        # Add both sides
        content_layout.addLayout(left_layout, 2)

        content_layout.addWidget(history_card, 1)

        self.page_layout.addWidget(content)

        self.load_sessions()

    def load_sessions(self):

        while self.history_layout.count():

            item = self.history_layout.takeAt(0)
            
            if item is not None:
                widget = item.widget()

            if widget:

                widget.deleteLater()

        sessions = get_focus_sessions()

        for session in sessions:

            card = SessionCard(
                session,
                self.load_sessions
            )

            self.history_layout.addWidget(card)

        self.history_layout.addStretch()