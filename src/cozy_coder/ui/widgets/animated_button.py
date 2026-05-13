from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QPushButton, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor


class AnimatedButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)

        self.setMinimumHeight(60)

        self.setStyleSheet("""
            QPushButton {
                background-color: #F8B4C6;
                border: none;
                border-radius: 18px;
                padding: 14px;
                font-size: 18px;
                font-family: "Quicksand";
                color: #5B4B4B;
            }

            QPushButton:hover {
                background-color: #F6C7D5;
            }
        """)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 4)
        shadow.setColor(QColor(0, 0, 0, 40))

        self.setGraphicsEffect(shadow)

        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(120)
        self.anim.setEasingCurve(QEasingCurve.Type.OutCubic)

    def enterEvent(self, event):
        rect = self.geometry()

        self.anim.stop()
        self.anim.setStartValue(rect)
        self.anim.setEndValue(rect.adjusted(-2, -2, 2, 2))
        self.anim.start()

        super().enterEvent(event)

    def leaveEvent(self, event):
        rect = self.geometry()

        self.anim.stop()
        self.anim.setStartValue(rect)
        self.anim.setEndValue(rect.adjusted(2, 2, -2, -2))
        self.anim.start()

        super().leaveEvent(event)