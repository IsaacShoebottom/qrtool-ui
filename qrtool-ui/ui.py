import sys
from PySide6.QtWidgets import QApplication, QLabel, QTabWidget, QWidget, QVBoxLayout, QMainWindow, QHBoxLayout


# TODO: Layout Example
# /---------------------------------------------------------\
# | [Generic Tab] [Wi-Fi Helper Tab]                    	|
# |                                     /----------------\  |
# | 			                        |				 |  |
# | [Text Example]                      |                |  |
# | [Option Example]                    |                |  |
# |                                     |                |  |
# |     [Generate QR Code]              \----------------/  |
# | [Save Image] [Copy to Clipboard]                        |
# \---------------------------------------------------------/

app = QApplication(sys.argv)

# Create a QMainWindow instance
window = QMainWindow()
window.setWindowTitle("QR Tool")

root = QWidget()
root.setLayout(QHBoxLayout())

# Create a QTabWidget instance
tab_widget = QTabWidget()
qr_image = QLabel("QR Image")

# Add layouts to root
root.layout().addWidget(tab_widget)
root.layout().addWidget(qr_image)

# Set central widget of QMainWindow instance
window.setCentralWidget(root)

# Add QWidget for each tab
tab_1 = QWidget()
tab_2 = QWidget()

# Set layout for each tab
tab_1.setLayout(QVBoxLayout())
tab_2.setLayout(QVBoxLayout())

# Create labels for each tab

label_1 = QLabel("This is Tab 1")
label_2 = QLabel("This is Tab 2")

# Add labels to layouts
tab_1.layout().addWidget(label_1)
tab_2.layout().addWidget(label_2)

tab_widget.addTab(tab_1, "Tab 1")
tab_widget.addTab(tab_2, "Tab 2")


window.show()
app.exec()
