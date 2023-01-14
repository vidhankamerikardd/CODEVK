import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Web Browser')

        self.webview = QWebEngineView(self)
        self.webview.setUrl(QUrl("http://www.google.com"))

        self.setGeometry(100, 100, 800, 600)
        self.show()

app = QApplication(sys.argv)
browser = Browser()
sys.exit(app.exec_())
