import sys
import numpy
from typing import Tuple
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMessageBox, QPushButton, QVBoxLayout, QWidget)

__author__ = "Jacob Garrison"
__version__ = "1.0.0"
__github__ = "wayahlife"

class CoinFlipGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create widgets
        self.flip_button = QPushButton("Flip Coin", self)
        self.flip_button.clicked.connect(self.flip_coin)
        self.about_button = QPushButton("About", self)
        self.about_button.clicked.connect(self.show_about_message)
        self.about_button.setFixedSize(self.flip_button.sizeHint())  # Set size of about_button to that of flip_button
        self.result_label = QLabel(self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setWordWrap(True)
        self.num_heads_label = QLabel(self)
        self.num_tails_label = QLabel(self)
        self.winner_label = QLabel(self)
        self.winner_label.setAlignment(Qt.AlignCenter)
        self.winner_label.setWordWrap(True)

        # Create layouts
        button_hbox = QHBoxLayout()
        button_hbox.addWidget(self.flip_button)
        button_hbox.addWidget(self.about_button)  # Add about_button to horizontal layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.num_tails_label)
        hbox.addWidget(self.num_heads_label)
        vbox = QVBoxLayout()
        vbox.addLayout(button_hbox)  # Add button_hbox (which contains flip_button and about_button) to vertical layout
        vbox.addWidget(self.result_label)
        vbox.addLayout(hbox)
        vbox.addWidget(self.winner_label)

        # Set main layout
        self.setLayout(vbox)
        self.setWindowTitle("Coin Flip")
        self.resize(250, 100)  # Set window size
        self.show()

    def flip_coin(self):
        num_flips = 1000
        heads, tails = self.random_coin_flip(num_flips)
        self.result_label.setText(f"A coin was flipped {num_flips} times.")
        self.num_heads_label.setText(f"Number of heads: {heads}")
        self.num_tails_label.setText(f"Number of tails: {tails}")
        self.winner_label.setText(f"Winner: {self.display_winner(heads, tails)}")

    def random_coin_flip(self, num_flips: int) -> Tuple[int, int]:
        coin_flip = numpy.random.binomial(n=1, p=0.5, size=num_flips)
        heads = sum(coin_flip)
        tails = num_flips - heads
        return heads, tails

    def display_winner(self, heads: int, tails: int) -> str:
        return "Heads" if heads > tails else "Tails"
    
    def show_about_message(self):
        QMessageBox.about(self, "About Coin Flip", f"Author: {__author__}\nVersion: {__version__}\nGithub: {__github__}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = CoinFlipGame()
    sys.exit(app.exec_())
