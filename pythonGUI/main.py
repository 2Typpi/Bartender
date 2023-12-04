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

        rum_widget = self.define_button("Rum Sour", "rum_sour")
        mai_widget = self.define_button("Mai Tai", "mai_tai")
        daiquiri_widget = self.define_button("Daiquiri", "daiquiri")
        hurricane_widget = self.define_button("Hurricane", "hurricane")
        mojito_widget = self.define_button("Mojito", "mojito")

        layout.addWidget(rum_widget, 0, 0)
        layout.addWidget(mai_widget, 0, 1)
        layout.addWidget(daiquiri_widget, 1, 0)
        layout.addWidget(hurricane_widget, 1, 1)
        layout.addWidget(mojito_widget, 2, 0)

        rumTab.setLayout(layout)
        return rumTab

    def vodka_tab(self):
        vodkaTab = QWidget()
        layout = QGridLayout()

        sex_widget = self.define_button("Sex on the Beach", "sex_on_the_beach")  # noqa: E501
        screwdriver_widget = self.define_button("Screwdriver", "screwdriver")  # noqa: E501
        tequila_widget = self.define_button("Tequila Sunrise", "tequila_sunrise")  # noqa: E501
        cosmopolitan_widget = self.define_button("Cosmopolitan", "cosmopolitan")  # noqa: E501

        layout.addWidget(sex_widget, 0, 0)
        layout.addWidget(screwdriver_widget, 0, 1)
        layout.addWidget(tequila_widget, 1, 0)
        layout.addWidget(cosmopolitan_widget, 1, 1)

        vodkaTab.setLayout(layout)
        return vodkaTab

    def maintenance_tab(self):
        maintenanceTab = QWidget()
        layout = QGridLayout()

        refuel_widget = self.define_button("Ansaugen", "refuel")
        clean_widget = self.define_button("Säubern", "mop")

        layout.addWidget(refuel_widget, 0, 0)
        layout.addWidget(clean_widget, 0, 1)

        maintenanceTab.setLayout(layout)
        return maintenanceTab

    def single_tab(self):
        singleTab = QWidget()
        layout = QGridLayout()

        vodka_widget = self.define_button("Vodka", "vodka")
        rum_widget = self.define_button("Rum", "rum")
        tequila_widget = self.define_button("Tequila", "tequila")
        cranberry_widget = self.define_button("Cranberry", "cranberry")
        grenadine_widget = self.define_button("Grenadine", "grenadine")
        lime_widget = self.define_button("Limette", "lime")
        orange_widget = self.define_button("Orange", "orange")
        sugar_widget = self.define_button("Zucker", "sugar")

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

    def define_button(self, name, drink_name):
        layout = QGridLayout()
        layout.setObjectName("ButtonCard")

        # Create a reference of a function to pass into connect function
        def pour(): return self.prep_pouring(drink_name)
        def show_ingredients(x): return self.show_ingredients(drink_name)

        label = QLabel()
        label.setPixmap(QPixmap("{0}/image/{1}_128.png".format(self.__location__, drink_name)))
        label.setAlignment(Qt.AlignCenter)
        label.mousePressEvent = show_ingredients
        layout.addWidget(label, 0, 0)

        button = QPushButton(name)

        button.clicked.connect(pour)
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
    def prep_pouring(self, drink_name):
        self.stackedLayout.setCurrentIndex(1)

        drink = drinks[drink_name]

        pour_time = drink[self.POUR_TIME_STRING]

        self.crono.setMaxTime(pour_time)
        QTimer.singleShot(pour_time * 1000, lambda: self.stackedLayout.setCurrentIndex(0))  # noqa: E501
        self.crono.start()

        pour_drink(drink[self.INGREDIENT_STRING])

    def show_ingredients(self, drink_name):
        return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    File = open("{}/style/main.qss".format(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))), 'r')

    with File:
        qss = File.read()
        app.setStyleSheet(qss + qdarkstyle.load_stylesheet_pyqt5())

    window.show()
    sys.exit(app.exec())
