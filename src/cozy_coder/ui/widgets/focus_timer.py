from PySide6.QtCore import QTimer, Qt

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QLineEdit,
)
from PySide6.QtWidgets import QSpinBox
from datetime import datetime
from PySide6.QtCore import Signal

from datetime import datetime

from cozy_coder.services.focus_service import (
    save_focus_session
)

class FocusTimer(QWidget):
    session_saved = Signal()

    def __init__(self):
        super().__init__()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.session_started_at = None

        layout = QVBoxLayout(self)

        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(24)

        self.minutes_input = QSpinBox()
    
        self.minutes_input.setRange(1, 180)

        self.minutes_input.setValue(25)

        self.minutes_input.setSuffix(" min")

        self.minutes_input.setStyleSheet("""
            padding: 10px;
            border-radius: 14px;
            background-color: #241B2F;
            color: white;
            font-size: 16px;
        """)

        layout.addWidget(self.minutes_input)

        self.setStyleSheet("""
            background-color: #342545;
            border-radius: 24px;
        """)

        # Timer display
        self.time_label = QLabel("25:00")

        self.time_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.time_label.setStyleSheet("""
            font-size: 72px;
            font-family: "JetBrains Mono";
            font-weight: bold;
            color: #F3EFFF;
        """)

        layout.addWidget(self.time_label)

        self.duration = (
            self.minutes_input.value() * 60
        )

        self.remaining = self.duration

        self.update_display()

        # Tag input
        self.tag_input = QLineEdit()

        self.tag_input.setPlaceholderText(
            "What are we focusing on?"
        )

        self.tag_input.setStyleSheet("""
            padding: 14px;
            border-radius: 16px;
            background-color: #342545;
            color: white;
            font-size: 16px;
        """)

        layout.addWidget(self.tag_input)

        # Buttons
        button_layout = QHBoxLayout()

        self.start_button = QPushButton("Start")
        self.pause_button = QPushButton("Pause")
        self.reset_button = QPushButton("Reset")
        self.stop_button = QPushButton("Stop")

        buttons = [
            self.start_button,
            self.pause_button,
            self.reset_button,
            self.stop_button,
        ]

        for btn in buttons:

            btn.setFixedHeight(50)

            btn.setStyleSheet("""
                QPushButton {
                    background-color: #C792EA;
                    border: none;
                    border-radius: 16px;

                    color: white;
                    font-size: 16px;
                    font-weight: bold;
                }

                QPushButton:hover {
                    background-color: #D7A9F2;
                }
            """)

            button_layout.addWidget(btn)

        layout.addLayout(button_layout)

        # Connections
        self.start_button.clicked.connect(
            self.start_timer
        )

        self.pause_button.clicked.connect(
            self.pause_timer
        )

        self.reset_button.clicked.connect(
            self.reset_timer
        )

        self.minutes_input.valueChanged.connect(
            self.update_duration_from_input
        )

        self.stop_button.clicked.connect(
            self.stop_session
        )


    def start_timer(self):

        if self.remaining <= 0:

            self.duration = (
                self.minutes_input.value() * 60
            )

            self.remaining = self.duration

        if not self.timer.isActive():

            self.session_started_at = datetime.now()

            self.timer.start(1000)

            self.update_display()

    def pause_timer(self):

        self.timer.stop()

    def reset_timer(self):

        self.timer.stop()

        self.duration = (
            self.minutes_input.value() * 60
        )

        self.remaining = self.duration

        self.update_display()

    def update_timer(self):

        self.remaining -= 1

        self.update_display()

        if self.remaining <= 0:

            self.timer.stop()

            ended_at = datetime.now()

            if self.session_started_at is not None:

                save_focus_session(
                    tag=self.tag_input.text(),
                    duration=self.duration,
                    started_at=self.session_started_at,
                    ended_at=ended_at,
                )

                self.session_saved.emit()

            print("Session saved!")

    def update_display(self):

        minutes = self.remaining // 60
        seconds = self.remaining % 60

        self.time_label.setText(
            f"{minutes:02}:{seconds:02}"
        )
    
    def update_duration_from_input(self):

        if not self.timer.isActive():

            self.duration = (
                self.minutes_input.value() * 60
            )

            self.remaining = self.duration

            self.update_display()

    def stop_session(self):

        self.timer.stop()

        elapsed = self.duration - self.remaining

        ended_at = datetime.now()

        if self.session_started_at is not None:

            save_focus_session(
                tag=self.tag_input.text(),
                duration=elapsed,
                started_at=self.session_started_at,
                ended_at=ended_at,
            )

            self.session_saved.emit()

        print("Partial session saved!")
        self.remaining = self.duration

        self.update_display()