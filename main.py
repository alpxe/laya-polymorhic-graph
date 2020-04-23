import sys
from PyQt5.QtWidgets import QApplication
from com.core.page import Page
"""
pyinstaller --onefile --clean --noconfirm --hidden-import pkg_resources.py2_warn --noconsole  --icon="icon.ico" main.py
"""

class Main:
    def __init__(self):
        app = QApplication(sys.argv)
        page = Page()
        page.show()
        sys.exit(app.exec_())
        pass


if __name__ == "__main__":
    Main()

