import random

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QFrame, QLabel, QPushButton, QSpacerItem,
                               QVBoxLayout, QWidget)

from usdchat.views.chromadb_collections_ui import collections_frame
from usdchat.views.mode_switcher import ModeSwitcher
from usdchat.views.rag_frame import rag_frame


def init_welcome_screen(self):
    self.mode_switcher = ModeSwitcher(rag_mode=self.rag_mode)
    self.mode_switcher.signalRagModeChanged.connect(
        self.handle_rag_mode_change)
    self.welcome_widget = QWidget(self.scroll_area_widget_contents)
    self.welcome_layout = QVBoxLayout(self.welcome_widget)
    welcome_text = (
        "<html><head/><body>"
        '<p align="center" style=" font-size:28pt; font-weight: bold;">USD Chat ✨</p>'
        "</body></html>")

    self.welcome_label = QLabel(welcome_text, self.scroll_area_widget_contents)
    self.welcome_label.setAlignment(Qt.AlignTop | Qt.AlignCenter)
    self.welcome_label.setStyleSheet("background:transparent;")
    self.welcome_label.adjustSize()

    self.welcome_layout.addWidget(self.welcome_label)

    self.vertical_spacer2 = QSpacerItem(20, 100)
    self.vertical_spacer4 = QSpacerItem(20, 50)

    self.welcome_layout.addItem(self.vertical_spacer4)
    self.welcome_layout.addWidget(self.mode_switcher)
    if self.rag_mode:
        self.vertical_spacer3 = QSpacerItem(20, 40)
        self.vertical_spacer5 = QSpacerItem(20, 40)

        self.mode_switcher.button_rag.setChecked(True)
        rag_frame_inst = rag_frame(self, self.welcome_widget)
        self.welcome_layout.addItem(self.vertical_spacer3)
        self.welcome_layout.addWidget(rag_frame_inst)

        collections_frame_inst = collections_frame(self, self.welcome_widget)
        self.welcome_layout.addItem(self.vertical_spacer5)
        self.welcome_layout.addWidget(collections_frame_inst)

        self.browse_button.clicked.connect(self.browse_directory)
        self.working_dir_line_edit.textChanged.connect(
            self.check_if_embed_ready)
        self.embed_stage_button.clicked.connect(self.embed_stage)
        self.collection_combo_box.currentTextChanged.connect(
            self.handle_collection_change
        )
    else:
        self.vertical_spacer3 = QSpacerItem(20, 280)
        self.welcome_layout.addItem(self.vertical_spacer3)
        self.mode_switcher.button_chat.setChecked(True)

    example_prompts = self.config.EXAMPLE_PROMPTS

    selected_prompts = random.sample(example_prompts, 4)

    button_frame = QFrame(self.welcome_widget)

    frame_layout = QVBoxLayout(button_frame)
    frame_layout.setContentsMargins(0, 0, 0, 0)
    frame_label = QLabel("Try it yourself", button_frame)
    frame_label.setStyleSheet("color: #AAAAAA; font-weight: bold;")
    frame_layout.addWidget(frame_label)

    self.button1 = QPushButton(selected_prompts[0])
    self.button2 = QPushButton(selected_prompts[1])
    self.button3 = QPushButton(selected_prompts[2])
    self.button4 = QPushButton(selected_prompts[3])

    frame_layout.addWidget(self.button1)
    frame_layout.addWidget(self.button2)
    frame_layout.addWidget(self.button3)
    frame_layout.addWidget(self.button4)

    self.vertical_spacer1 = QSpacerItem(20, 140)
    self.welcome_layout.addItem(self.vertical_spacer1)
    self.welcome_layout.addWidget(button_frame)
    self.welcome_layout.addItem(self.vertical_spacer2)
    self.welcome_layout.setContentsMargins(0, 0, 0, 0)

    self.button1.setFixedHeight(40)
    self.button2.setFixedHeight(40)
    self.button3.setFixedHeight(40)
    self.button4.setFixedHeight(40)

    self.button1.clicked.connect(lambda: self.send_button_text(self.button1))
    self.button2.clicked.connect(lambda: self.send_button_text(self.button2))
    self.button3.clicked.connect(lambda: self.send_button_text(self.button3))
    self.button4.clicked.connect(lambda: self.send_button_text(self.button4))

    self.scroll_area_layout.addWidget(self.welcome_widget)
