import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QFileDialog

class PhoneNumberGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Phone Number Generator")
        self.setGeometry(100, 100, 600, 400)
        
        self.generate_button = QPushButton("Generate Now", self)
        self.generate_button.setGeometry(10, 10, 100, 30)
        self.generate_button.clicked.connect(self.generate_numbers)
        
        self.phone_table = QTableWidget(self)
        self.phone_table.setGeometry(10, 50, 580, 250)
        self.phone_table.setColumnCount(1)
        self.phone_table.setHorizontalHeaderLabels(["Phone Numbers"])
        
        self.download_button = QPushButton("Download Numbers", self)
        self.download_button.setGeometry(10, 310, 150, 30)
        self.download_button.clicked.connect(self.download_numbers)
        
        self.delete_button = QPushButton("Delete Numbers", self)
        self.delete_button.setGeometry(170, 310, 150, 30)
        self.delete_button.clicked.connect(self.delete_numbers)
        
        self.phone_label = QLabel("Enter Phone Number:", self)
        self.phone_label.setGeometry(10, 360, 120, 20)
        
        self.phone_input = QLineEdit(self)
        self.phone_input.setGeometry(130, 360, 150, 20)
        
        self.count_label = QLabel("Number:", self)
        self.count_label.setGeometry(300, 360, 80, 20)
        
        self.count_input = QLineEdit(self)
        self.count_input.setGeometry(380, 360, 60, 20)
        
    def generate_numbers(self):
        start_number = int(self.phone_input.text())
        count = int(self.count_input.text())
        
        self.phone_table.setRowCount(count)
        for i in range(count):
            phone_number = str(start_number + i)
            self.phone_table.setItem(i, 0, QTableWidgetItem(phone_number))
        
    def download_numbers(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Phone Numbers", "", "Text Files (*.txt);;All Files (*)", options=options)
        
        if file_name:
            with open(file_name, "w") as f:
                for row in range(self.phone_table.rowCount()):
                    phone_number = self.phone_table.item(row, 0).text()
                    f.write(phone_number + "\n")
            print("Phone numbers downloaded to", file_name)
        
    def delete_numbers(self):
        self.phone_table.setRowCount(0)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhoneNumberGeneratorApp()
    window.show()
    sys.exit(app.exec_())