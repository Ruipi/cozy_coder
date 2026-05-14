from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QPushButton,
)

from cozy_coder.services.focus_service import (
    delete_focus_session
)


class SessionCard(QWidget):

    def __init__(
        self,
        session,
        refresh_callback,
    ):
        super().__init__()

        self.session = session

        self.refresh_callback = refresh_callback

        self.setStyleSheet("""
            background-color: #241B2F;
            border-radius: 16px;
        """)

        layout = QHBoxLayout(self)

        # Session text
        duration_minutes = session.duration // 60

        text = QLabel(
            f"{session.tag or 'Untitled'} "
            f"• {duration_minutes}m"
        )

        text.setStyleSheet("""
            color: white;
            font-size: 16px;
            padding: 8px;
        """)

        layout.addWidget(text)

        layout.addStretch()

        # Delete button
        delete_btn = QPushButton("🗑")

        delete_btn.setFixedSize(36, 36)

        delete_btn.setStyleSheet("""
            QPushButton {
                background-color: #F38BA8;
                border: none;
                border-radius: 18px;
                font-size: 16px;
            }

            QPushButton:hover {
                background-color: #F06A92;
            }
        """)

        delete_btn.clicked.connect(
            self.delete_session
        )

        layout.addWidget(delete_btn)

    def delete_session(self):

        delete_focus_session(
            self.session.id
        )

        self.refresh_callback()