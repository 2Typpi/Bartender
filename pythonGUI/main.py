import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QTabWidget, QPushButton
from PyQt6.QtGui import QPalette, QColor


class Color(QWidget):

  def __init__(self, color):
    super(Color, self).__init__()
    self.setAutoFillBackground(True)

    palette = self.palette()
    palette.setColor(QPalette.ColorRole.Window, QColor(color))
    self.setPalette(palette)

class MainWindow(QMainWindow):
    
  def __init__(self):
    super(MainWindow, self).__init__()
    self.setWindowTitle("Bartender")
    self.resize(600, 500)

    tabs = QTabWidget()
    tabs.setTabPosition(QTabWidget.TabPosition.North)
    tabs.setMovable(True)

    tabs.addTab(self.rum_tab(), "Vodka")
    tabs.addTab(self.vodka_tab(), "Rum")

    self.setCentralWidget(tabs)

  def rum_tab(self):
    rumTab = QWidget()
    layout = QGridLayout()

    layout.addWidget(QPushButton("Rum Sour"), 0, 0)
    layout.addWidget(QPushButton("Mai Tai"), 0, 1)
    layout.addWidget(QPushButton("Daiquiri"), 1, 0)
    layout.addWidget(QPushButton("Hurricane Cocktail"), 1, 1)
    layout.addWidget(QPushButton("Mojito"), 2, 0)

    rumTab.setLayout(layout)
    return rumTab
  
  def vodka_tab(self):
    vodkaTab = QWidget()
    layout = QGridLayout()

    layout.addWidget(QPushButton("Sex on the Beach"), 0, 0)
    layout.addWidget(QPushButton("Screwdriver"), 0, 1)
    layout.addWidget(QPushButton("Tequila Sunrise"), 1, 0)
    layout.addWidget(QPushButton("Cosmopolitan"), 1, 1)

    vodkaTab.setLayout(layout)
    return vodkaTab


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())