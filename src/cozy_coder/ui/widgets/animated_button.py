from PySide6.QtWidgets import (
    QPushButton,
    QGraphicsDropShadowEffect,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class AnimatedButton(QPushButton):

    def __init__(self, text):
        super().__init__(text)

        self.setMinimumHeight(50)
        self.setStyleSheet("""
            QPushButton {
                background-color: #F8B4C6;
                border: none;
                border-radius: 18px;

                font-size: 18px;
                font-family: "Quicksand";
                font-weight: bold;

                color: #5B4B4B;

                padding: 12px;
            }

            QPushButton:hover {
                background-color: #F6C7D5;
            }

            QPushButton:pressed {
                background-color: #E89AAF;
            }
        """)

        shadow = QGraphicsDropShadowEffect(self)

        shadow.setBlurRadius(25)
        shadow.setOffset(0, 4)

        shadow.setColor(
            QColor(248, 180, 198, 120)
        )

        self.setGraphicsEffect(shadow)
        self.setCursor(Qt.CursorShape.PointingHandCursor)