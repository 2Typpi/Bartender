import os
import sys

import qdarkstyle

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
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def __init__(self):
        super(MainWindow, self).__init__()
        self.crono = Crono()

        self.setWindowTitle("Bartender")
        self.resize(1024, 500)

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)

        self.tabs.addTab(self.vodka_tab(), "Vodka")
        self.tabs.addTab(self.rum_tab(), "Rum")
        self.tabs.addTab(self.maintenance_tab(), "Wartung")
        self.tabs.addTab(self.single_tab(), "Single")

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

    def maintenance_tab(self):
        maintenanceTab = QWidget()
        layout = QGridLayout()

        refuel_widget = self.define_button("Ansaugen", "refuel", self.refuel)  # noqa: E501
        clean_widget = self.define_button("Säubern", "mop", self.clean)  # noqa: E501

        layout.addWidget(refuel_widget, 0, 0)
        layout.addWidget(clean_widget, 0, 1)

        maintenanceTab.setLayout(layout)
        return maintenanceTab

    def clean(self):
        drink = drinks["clean"]
        self.prep_pouring(drink)

    def refuel(self):
        drink = drinks["fill_up"]
        self.prep_pouring(drink)

    def single_tab(self):
        singleTab = QWidget()
        layout = QGridLayout()

        vodka_widget = self.define_button("Vodka", None, self.vodka)  # noqa: E501
        rum_widget = self.define_button("Rum", None, self.rum)  # noqa: E501
        tequila_widget = self.define_button("Tequila", None, self.tequila)  # noqa: E501
        cranberry_widget = self.define_button("Cranberry", None, self.cranberry)  # noqa: E501
        grenadine_widget = self.define_button("Grenadine", None, self.grenadine)  # noqa: E501
        lime_widget = self.define_button("Limette", None, self.lime)  # noqa: E501
        orange_widget = self.define_button("Orange", None, self.orange)  # noqa: E501
        sugar_widget = self.define_button("Zucker", None, self.sugar)  # noqa: E501

        layout.addWidget(vodka_widget, 0, 0)
        layout.addWidget(rum_widget, 0, 1)
        layout.addWidget(tequila_widget, 1, 0)
        layout.addWidget(cranberry_widget, 1, 1)
        layout.addWidget(grenadine_widget, 2, 0)
        layout.addWidget(lime_widget, 2, 1)
        layout.addWidget(orange_widget, 3, 0)
        layout.addWidget(sugar_widget, 3, 1)

        singleTab.setLayout(layout)
        return singleTab

    def vodka(self):
        drink = drinks["vodka"]
        self.prep_pouring(drink)

    def rum(self):
        drink = drinks["rum"]
        self.prep_pouring(drink)

    def tequila(self):
        drink = drinks["tequila"]
        self.prep_pouring(drink)

    def cranberry(self):
        drink = drinks["cranberry"]
        self.prep_pouring(drink)

    def grenadine(self):
        drink = drinks["grenadine"]
        self.prep_pouring(drink)

    def lime(self):
        drink = drinks["lime"]
        self.prep_pouring(drink)

    def orange(self):
        drink = drinks["orange"]
        self.prep_pouring(drink)

    def sugar(self):
        drink = drinks["sugar"]
        self.prep_pouring(drink)

    def define_button(self, name, image, function):
        layout = QGridLayout()
        layout.setObjectName("ButtonCard")

        label = QLabel()
        label.setPixmap(QPixmap("{0}/image/{1}_128.png".format(self.__location__, image)))
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label, 0, 0)

        button = QPushButton(name)
        button.clicked.connect(function)
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        button.setFixedHeight(100)
        button.setFont(QFont("Sans Serif", 10))
        layout.addWidget(button, 0, 1)

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

    File = open("{}/style/main.qss".format(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))), 'r')

    with File:
        qss = File.read()
        app.setStyleSheet(qss + qdarkstyle.load_stylesheet_pyqt5())

    window.show()
    sys.exit(app.exec())
