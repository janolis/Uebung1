import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createLayout()

        
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        
        save = QAction("Save", self)
        save.triggered.connect(self.buttonSave_clicked) 
        quit = QAction("Quit", self)
        quit.triggered.connect(self.menu_quit)

        quit.setMenuRole(QAction.QuitRole)

        filemenu.addAction(save)
        filemenu.addAction(quit)

    def menu_quit(self):
        print("Quit")
        self.close()

    def createLayout(self):
        self.setWindowTitle("Personenformular")
        
        layout = QGridLayout()

        vornameLabel = QLabel("Vorname:")
        self.vornameLine = QLineEdit()
        self.vornameLine.setObjectName("vornameLine")

        nameLabel = QLabel("Name:")
        self.nameLine = QLineEdit()
        self.nameLine.setObjectName("nameLine")

        birthdateLabel = QLabel("Geburtsdatum:")
        self.birthdateEdit = QDateEdit()
        self.birthdateEdit.setCalendarPopup(True)
        self.birthdateEdit.setDisplayFormat("dd.MM.yyyy")
        self.birthdateEdit.setDate(QDate.currentDate())
        self.birthdateEdit.setObjectName("birthdateEdit")

        adressLabel = QLabel("Adresse:")
        self.adressLine = QLineEdit()
        self.adressLine.setObjectName("adressLine")

        plzLabel = QLabel("Postleitzahl:")
        self.plzLine = QLineEdit()
        self.plzLine.setObjectName("plzLine")

        ortLabel = QLabel("Ort:")
        self.ortLine = QLineEdit()
        self.ortLine.setObjectName("ortLine")

        countriesLabel = QLabel("Land:")
        self.countries = QComboBox() 
        self.countries.addItems(["Schweiz", "Liechtenstein", "Deutschland", "Österreich"])
        self.countries.setObjectName("countries")

        buttonSave = QPushButton("Save")
        buttonSave.clicked.connect(self.buttonSave_clicked)

       
        layout.addWidget(vornameLabel, 0, 0)
        layout.addWidget(self.vornameLine, 0, 1)
        layout.addWidget(nameLabel, 1, 0)
        layout.addWidget(self.nameLine, 1, 1)
        layout.addWidget(birthdateLabel, 2, 0)
        layout.addWidget(self.birthdateEdit, 2, 1)
        layout.addWidget(adressLabel, 3, 0)
        layout.addWidget(self.adressLine, 3, 1)
        layout.addWidget(plzLabel, 4, 0)
        layout.addWidget(self.plzLine, 4, 1)
        layout.addWidget(ortLabel, 5, 0)
        layout.addWidget(self.ortLine, 5, 1)
        layout.addWidget(countriesLabel, 6, 0)
        layout.addWidget(self.countries, 6, 1)
        layout.addWidget(buttonSave, 7, 1)

      
        center = QWidget()
        center.setLayout(layout)
        self.setCentralWidget(center)
       
        self.show()

    def buttonSave_clicked(self):
        
        vorname = self.vornameLine.text()
        name = self.nameLine.text()
        geburtsdatum = self.birthdateEdit.date().toString("dd.MM.yyyy")
        adresse = self.adressLine.text()
        plz = self.plzLine.text()
        ort = self.ortLine.text()
        land = self.countries.currentText()

        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(f"{vorname},")
            file.write(f"{name},")
            file.write(f"{geburtsdatum},")
            file.write(f"{adresse},")
            file.write(f"{plz},")
            file.write(f"{ort},")
            file.write(f"{land},")

        print("Daten wurden erfolgreich in 'output.txt' gespeichert!")

def main():
    app = QApplication(sys.argv)  
    mainwindow = Fenster()      
    mainwindow.raise_()          
    app.exec_()                  

if __name__ == '__main__':
    main()
