
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton,QLineEdit
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QGridLayout')
layout = QGridLayout()
layout.addWidget(QLineEdit('Button (0, 0)'), 0, 0)
layout.addWidget(QLineEdit('Button (0, 1)'), 0, 1)
layout.addWidget(QLineEdit('Button (0, 2)'), 0, 2)
layout.addWidget(QLineEdit('Button (1, 0)'), 1, 0)
layout.addWidget(QLineEdit('Button (1, 1)'), 1, 1)
layout.addWidget(QLineEdit('Button (1, 2)'), 1, 2)
layout.addWidget(QLineEdit('Button (2, 0)'), 2, 0)
layout.addWidget(QLineEdit('Button (2, 1) + 2 Columns Span'), 2, 1, 1, 2)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())