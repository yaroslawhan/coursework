import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 600, 400)
        # Создание всплывающего окна QMessageBox
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Message")
        msg_box.setText("This is a message box.")
        msg_box.setStandardButtons(QMessageBox.Ok)

        # Показать всплывающее окно
        msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
