from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow

from com.core.generate import Generate
from ui.face import Ui_Form


class Page(QMainWindow, Ui_Form):
    def __init__(self):
        super(Page, self).__init__()
        self.setupUi(self)
        self.paddingTxt.setValidator(QIntValidator(-100, 100, self))  # padding限制输入
        self.init_event()

    def init_event(self):
        self.inputBtn.clicked.connect(self.__open_input_file)
        self.outputBtn.clicked.connect(self.__open_output_file)

        self.generateBtn.clicked.connect(self.__generate_handler)
        pass

    def __open_input_file(self):
        Generate().open_file(Generate.input_file_path)
        pass

    def __open_output_file(self):
        Generate().open_file(Generate.output_file_path)
        pass

    def __generate_handler(self):
        arrange_list = ["hroi", "vert"]
        align_list = ["F", "M", "T"]
        arrange = arrange_list[self.arrangeBox.currentIndex()]
        alignH = align_list[self.alignHBox.currentIndex()]
        alignV = align_list[self.alignVBox.currentIndex()]
        padding = int(self.paddingTxt.text()) if (len(self.paddingTxt.text()) > 0) else 0
        Generate().setting(arrange, alignH, alignV, padding)
        Generate().run()
        pass
