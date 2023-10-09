import sys
from crono import Crono

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QTabWidget, QPushButton, QStackedLayout, \
    QProgressBar, QVBoxLayout, QLabel, QSizePolicy  # noqa: E501

from drinks import drinks
from mix_cocktails import pour_drink


class MainWindow(QMainWindow):
    POUR_TIME_STRING = "pour_time"
    INGREDIENT_STRING = "ingredients"

    def __init__(self):
        super(MainWindow, self).__init__()
        self.crono = Crono()

        self.setWindowTitle("Bartender")
        self.resize(1024, 600)

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

        rum_widget = self.define_button("Rum Sour", "Rum_Sour", self.rum_sour)  # noqa: E501
        mai_widget = self.define_button("Mai Tai", "Mai_Tai", self.mai_tai)  # noqa: E501
        daiquiri_widget = self.define_button("Daiquiri", "Daiquiri", self.daiquiri)  # noqa: E501
        hurricane_widget = self.define_button("Hurricane", "Hurricane", self.hurricane)  # noqa: E501
        mojito_widget = self.define_button("Mojito", "Mojito", self.mojito)  # noqa: E501

        layout.addWidget(rum_widget, 0, 0)
        layout.addWidget(mai_widget, 0, 1)
        layout.addWidget(daiquiri_widget, 1, 0)
        layout.addWidget(hurricane_widget, 1, 1)
        layout.addWidget(mojito_widget, 2, 0)

        rumTab.setLayout(layout)
        return rumTab

    def rum_sour(self):
        drink = drinks["rum_sour"]
        self.prep_pouring(drink)

    def mai_tai(self):
        drink = drinks["mai_tai"]
        self.prep_pouring(drink)

    def daiquiri(self):
        drink = drinks["daiquiri"]
        self.prep_pouring(drink)

    def hurricane(self):
        drink = drinks["hurricane"]
        self.prep_pouring(drink)

    def mojito(self):
        drink = drinks["mojito"]
        self.prep_pouring(drink)

    def vodka_tab(self):
        vodkaTab = QWidget()
        layout = QGridLayout()

        sex_widget = self.define_button("Sex on the Beach", "Sex_On_The_Beach", self.sex_on_the_beach)  # noqa: E501
        screwdriver_widget = self.define_button("Screwdriver", "Screwdriver", self.screwdriver)  # noqa: E501
        tequila_widget = self.define_button("Tequila Sunrise", "Tequila_Sunrise", self.tequila_sunrise)  # noqa: E501
        cosmopolitan_widget = self.define_button("Cosmopolitan", "Cosmopolitan", self.cosmopolitan)  # noqa: E501

        layout.addWidget(sex_widget, 0, 0)
        layout.addWidget(screwdriver_widget, 0, 1)
        layout.addWidget(tequila_widget, 1, 0)
        layout.addWidget(cosmopolitan_widget, 1, 1)

        vodkaTab.setLayout(layout)
        return vodkaTab

    def sex_on_the_beach(self):
        drink = drinks["sex_on_the_beach"]
        self.prep_pouring(drink)

    def screwdriver(self):
        drink = drinks["screwdriver"]
        self.prep_pouring(drink)

    def tequila_sunrise(self):
        drink = drinks["tequila_sunrise"]
        self.prep_pouring(drink)

    def cosmopolitan(self):
        drink = drinks["cosmopolitan"]
        self.prep_pouring(drink)

    def define_button(self, name, image, function):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setObjectName("ButtonCard")

        label = QLabel()
        label.setPixmap(QPixmap("pythonGUI/image/{}_128.png".format(image)))
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        button = QPushButton(name)
        button.clicked.connect(function)
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        button.setFont(QFont("Sans Serif", 10))
        layout.addWidget(button)

        widget = QWidget()
        widget.setObjectName("ButtonCard")
        widget.setLayout(layout)
        widget.resize(label.width(), label.height())

        return widget

    # Prepares everything and starts pouring the drink
    def prep_pouring(self, drink):
        self.stackedLayout.setCurrentIndex(1)

        pour_time = drink[self.POUR_TIME_STRING]

        self.crono.setMaxTime(pour_time)
        QTimer.singleShot(pour_time * 1000, lambda: self.stackedLayout.setCurrentIndex(0))  # noqa: E501
        self.crono.start()

        pour_drink(drink[self.INGREDIENT_STRING])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    File = open("pythonGUI/style/main.qss", 'r')

    with File:
        qss = File.read()
        app.setStyleSheet(qss)

    window.show()
    sys.exit(app.exec())
