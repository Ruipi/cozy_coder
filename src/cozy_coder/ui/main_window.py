from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QStackedWidget,
    QVBoxLayout
)
from PySide6.QtWidgets import (
    QPushButton,
    QLabel,
    QFrame,
)

from cozy_coder.ui.sidebar.sidebar import Sidebar

from cozy_coder.ui.pages.focus_page import FocusPage
from cozy_coder.ui.pages.tasks_page import TasksPage
from cozy_coder.ui.pages.poems_page import PoemsPage
from cozy_coder.ui.pages.reading_page import ReadingPage
from cozy_coder.ui.pages.tarot_page import TarotPage
from cozy_coder.ui.pages.meditation_page import MeditationPage
from cozy_coder.ui.pages.calendar_page import CalendarPage
from PySide6.QtCore import Qt, QPoint

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowFlags(
        Qt.WindowType.FramelessWindowHint
        )

        self.setAttribute(
        Qt.WidgetAttribute.WA_TranslucentBackground
        )

        root_layout = QHBoxLayout(self)
        root_layout.setContentsMargins(20, 20, 20, 20)

        self.container = QWidget()

        self.container.setStyleSheet("""
            background-color: #241B2F;
            border-radius: 24px;
        """)

        root_layout.addWidget(self.container)

        container_layout = QVBoxLayout(self.container)
        container_layout.setContentsMargins(0, 0, 0, 0)

        self.setWindowTitle("Cozy Coder")
        self.resize(1400, 900)
        # Sidebar
        self.sidebar = Sidebar()

        # Topbar
        topbar = QFrame()

        topbar.setFixedHeight(60)

        topbar.setStyleSheet("""
            background-color: #342545;
            border-top-left-radius: 24px;
            border-top-right-radius: 24px;
        """)
        topbar_layout = QHBoxLayout(topbar)

        topbar_layout.setContentsMargins(20, 0, 20, 0)

        title = QLabel("cozy coder ✨")

        title.setStyleSheet("""
            color: white;
            font-size: 20px;
            font-family: "Quicksand";
            font-weight: bold;
        """)

        # Close Button
        close_button = QPushButton("✕")

        close_button.setFixedSize(36, 36)

        close_button.setStyleSheet("""
            QPushButton {
                background-color: #F38BA8;
                border: none;
                border-radius: 18px;

                color: white;
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #F06A92;
            }
        """)

        close_button.clicked.connect(self.close)

        # Assemble Topbar
        topbar_layout.addWidget(title)

        topbar_layout.addStretch()

        topbar_layout.addWidget(close_button)

        # Stack
        self.stack = QStackedWidget()

        # Create Body Layout
        body = QWidget()

        body_layout = QHBoxLayout(body)

        body_layout.setContentsMargins(0, 0, 0, 0)

        body_layout.addWidget(self.sidebar)
        body_layout.addWidget(self.stack)

        container_layout.addWidget(topbar)
        container_layout.addWidget(body)
        
        self.drag_pos = QPoint()

        body_layout.setSpacing(0)
        root_layout.setSpacing(0)
        container_layout.setSpacing(0)
        # Pages

        self.focus_page = FocusPage()
        self.tasks_page = TasksPage()
        self.poems_page = PoemsPage()
        self.reading_page = ReadingPage()
        self.tarot_page = TarotPage()
        self.meditation_page = MeditationPage()
        self.calendar_page = CalendarPage()

        self.stack.addWidget(self.focus_page)
        self.stack.addWidget(self.tasks_page)
        self.stack.addWidget(self.poems_page)
        self.stack.addWidget(self.reading_page)
        self.stack.addWidget(self.tarot_page)
        self.stack.addWidget(self.meditation_page)
        self.stack.addWidget(self.calendar_page)

        # Navigation
        self.sidebar.focus_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.focus_page)
        )

        self.sidebar.tasks_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.tasks_page)
        )

        self.sidebar.poems_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.poems_page)
        )

        self.sidebar.reading_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.reading_page)
        )

        self.sidebar.tarot_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.tarot_page)
        )

        self.sidebar.meditation_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.meditation_page)
        )

        self.sidebar.calendar_btn.clicked.connect(
            lambda: self.stack.setCurrentWidget(self.calendar_page)
        )

    def mousePressEvent(self, event):

        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = (
                event.globalPosition().toPoint()
                - self.frameGeometry().topLeft()
            )

        event.accept()


    def mouseMoveEvent(self, event):

        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(
                event.globalPosition().toPoint()
                - self.drag_pos
            )

        event.accept()