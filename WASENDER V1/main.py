import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QFrame, QLineEdit, QHBoxLayout
import pandas as pd
from generator import PhoneNumberGeneratorApp

class PhoneApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Phone Number Manager")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        self.toolbar = self.addToolBar("Toolbar")

        self.upload_action = QAction("Upload File", self)
        self.upload_action.triggered.connect(self.openFileDialog)
        self.toolbar.addAction(self.upload_action)

        self.generator_action = QAction("Generator", self)
        self.generator_action.triggered.connect(self.openGenerator)
        self.toolbar.addAction(self.generator_action)

        self.splitter = QFrame(self)
        self.splitter.setFrameShape(QFrame.VLine)
        self.splitter.setFrameShadow(QFrame.Sunken)

        self.left_table = QTableWidget(self)
        self.left_table.setColumnCount(2)
        self.left_table.setHorizontalHeaderLabels(["Phone Number", "Actions"])
        self.left_table.setColumnWidth(0, 150)

        self.phone_input = QLineEdit(self)
        self.phone_input.setMaximumWidth(150)

        clear_button = QPushButton("Clear All")
        clear_button.setMaximumWidth(self.left_table.columnWidth(1))
        clear_button.clicked.connect(self.clearAll)

        add_button = QPushButton("Add")
        add_button.setMaximumWidth(self.left_table.columnWidth(1))
        add_button.clicked.connect(self.addPhone)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.phone_input)
        input_layout.addWidget(add_button)
        input_layout.addWidget(clear_button)

        left_layout = QVBoxLayout()
        left_layout.addLayout(input_layout)
        left_layout.addWidget(self.left_table)
        left_layout.addWidget(self.splitter)

        self.right_widget = QWidget(self)
        self.right_layout = QVBoxLayout()
        self.right_widget.setLayout(self.right_layout)

        self.main_layout = QHBoxLayout()
        self.main_layout.addLayout(left_layout)
        self.main_layout.addWidget(self.right_widget)

        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

    def openFileDialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.fileSelected.connect(self.readFile)
        file_dialog.exec_()

    def readFile(self, filename):
        if filename.endswith('.csv') or filename.endswith('.txt'):
            with open(filename, "r") as file:
                phone_numbers = file.read().splitlines()
        elif filename.endswith('.xlsx') or filename.endswith('.xls'):
            df = pd.read_excel(filename)
            phone_numbers = df.iloc[:, 0].astype(str).tolist()
        else:
            return

        self.left_table.setRowCount(len(phone_numbers))
        for i, number in enumerate(phone_numbers):
            self.left_table.setItem(i, 0, QTableWidgetItem(number))
            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda _, row=i: self.deleteRow(row))
            self.left_table.setCellWidget(i, 1, delete_button)
            self.left_table.setRowHeight(i, 30)

    def addPhone(self):
        new_phone = self.phone_input.text()
        if new_phone:
            row_count = self.left_table.rowCount()
            self.left_table.insertRow(row_count)
            self.left_table.setItem(row_count, 0, QTableWidgetItem(new_phone))
            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda _, row=row_count: self.deleteRow(row))
            self.left_table.setCellWidget(row_count, 1, delete_button)
            self.left_table.setRowHeight(row_count, 30)
        self.phone_input.clear()

    def clearAll(self):
        self.left_table.setRowCount(0)

    def deleteRow(self, row):
        self.left_table.removeRow(row)

    def openGenerator(self):
        self.generator_interface = PhoneNumberGeneratorApp()
        self.generator_interface.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhoneApp()
    window.show()
    sys.exit(app.exec_())
