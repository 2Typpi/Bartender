import sys
from crono import Crono

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QTabWidget, QPushButton, QStackedLayout, QProgressBar, QVBoxLayout  # noqa: E501

from drinks import drinks
from mix_cocktails import pour_drink


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.crono = Crono()

        self.setWindowTitle("Bartender")
        self.resize(600, 500)

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)

        self.tabs.addTab(self.vodka_tab(), "Vodka")
        self.tabs.addTab(self.rum_tab(), "Rum")

        self.stackedLayout = QStackedLayout()

        self.prog_bar = QProgressBar()
        self.crono.tick.connect(self.prog_bar.setValue)

        layout = QVBoxLayout()
        layout.addWidget(self.prog_bar)

        prog_widget = QWidget()
        prog_widget.setLayout(layout)

        self.stackedLayout.addWidget(self.tabs)
        self.stackedLayout.addWidget(prog_widget)

        widget = QWidget()
        widget.setLayout(self.stackedLayout)
        self.setCentralWidget(widget)

    def rum_tab(self):
        rumTab = QWidget()
        layout = QGridLayout()

        rum_sour_button = QPushButton("Rum Sour")
        rum_sour_button.clicked.connect(self.rum_sour)

        mai_tai_button = QPushButton("Mai Tai")
        mai_tai_button.clicked.connect(self.mai_tai)

        daiquiri_button = QPushButton("Daiquiri")
        daiquiri_button.clicked.connect(self.daiquiri)

        hurricane_cocktail_button = QPushButton("Hurricane Cocktail")
        hurricane_cocktail_button.clicked.connect(self.hurricane)

        mojito_button = QPushButton("Mojito")
        mojito_button.clicked.connect(self.mojito)

        layout.addWidget(rum_sour_button, 0, 0)
        layout.addWidget(mai_tai_button, 0, 1)
        layout.addWidget(daiquiri_button, 1, 0)
        layout.addWidget(hurricane_cocktail_button, 1, 1)
        layout.addWidget(mojito_button, 2, 0)

        rumTab.setLayout(layout)
        return rumTab

    def rum_sour(self):
        print("sour")

    def mai_tai(self):
        print("mai")

    def daiquiri(self):
        print("daiquiri")

    def hurricane(self):
        print("hurricane")

    def mojito(self):
        print("mojito")

    def vodka_tab(self):
        vodkaTab = QWidget()
        layout = QGridLayout()

        sex_button = QPushButton("Sex on the Beach")
        sex_button.clicked.connect(self.sex_on_the_beach)

        screwdriver_button = QPushButton("Screwdriver")
        screwdriver_button.clicked.connect(self.screwdriver)

        tequila_button = QPushButton("Tequila Sunrise")
        tequila_button.clicked.connect(self.tequila_sunrise)

        cosmopolitan_button = QPushButton("Cosmopolitan")
        cosmopolitan_button.clicked.connect(self.cosmopolitan)

        layout.addWidget(sex_button, 0, 0)
        layout.addWidget(screwdriver_button, 0, 1)
        layout.addWidget(tequila_button, 1, 0)
        layout.addWidget(cosmopolitan_button, 1, 1)

        vodkaTab.setLayout(layout)
        return vodkaTab

    def sex_on_the_beach(self):
        print("Sex")

    def screwdriver(self):
        self.stackedLayout.setCurrentIndex(1)
        self.crono.setMaxTime(77)
        QTimer.singleShot(77000, lambda: self.stackedLayout.setCurrentIndex(0))
        self.crono.start()

    def tequila_sunrise(self):
        self.stackedLayout.setCurrentIndex(1)

        drink = drinks["tequila_sunrise"]
        pour_time = drink["pour_time"]

        self.crono.setMaxTime(pour_time)
        QTimer.singleShot(pour_time * 1000, lambda: self.stackedLayout.setCurrentIndex(0))  # noqa: E501
        self.crono.start()

        pour_drink(drink["ingredients"])

    def cosmopolitan(self):
        print("cosmo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
