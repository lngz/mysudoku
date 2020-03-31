from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from mainwindow import Ui_MainWindow
from Sudoku import Solution
import sys
from PyQt5.QtCore import Qt
class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setFont(QtGui.QFont('SansSerif', 30)) # change font type and size

        self.ui.pushButton.clicked.connect(self.btnClicked) # connecting the clicked signal with btnClicked slot
        # self.ui.pushButton_2.clicked.connect(self.close) # connecting the clicked signal with btnClicked slot
        self.ui.pushButton_2.clicked.connect(self.btnsolve) # connecting the clicked signal with btnClicked slot

        self._createDisplay()
        
    def _createDisplay(self):
        """Create the display."""
        # Create the display widget
        self.btnClicked()
        
        # Add the display to the general layout
        # self.ui.generalLayout.addWidget(self.display)
    def btnClicked(self):

        for i in range(81):
            self.ui.block[i].setText(".")
    def btnsolve(self):

        question = [[".",".",".", ".",".",".", ".",".","."],
                    [".",".",".", ".",".",".", ".",".","."],
                    [".",".",".", ".",".",".", ".",".","."],

                    [".",".",".", ".",".",".", ".",".","."],
                    [".",".",".", ".",".",".", ".",".","."],
                    [".",".",".", ".",".",".", ".",".","."],

                    [".",".",".", ".",".",".", ".",".","."],
                    [".",".",".", ".",".",".", ".",".","."],
                    [".",".",".", ".",".",".", ".",".","."]]
        x = 0
        y = 0
        for i in range(81):
            x = (i % 9 )
            y = (i //9 ) 
            question[y][x] = self.ui.block[i].text()  
        

        s = Solution()

        s.solveSudoku(question)

        for i in range(81):
            x = (i % 9 )
            y = (i //9 ) 
            self.ui.block[i].setText(question[y][x])
      

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

