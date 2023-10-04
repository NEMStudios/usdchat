from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class HomeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        label = QLabel("🏠 Home UI")
        layout.addWidget(label)
        self.setLayout(layout)
