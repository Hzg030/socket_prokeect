from PyQt5 import QtGui,QtWidgets
from socketGUI2 import Ui_chatWindow
import sys
#from socket import *
#import threading

class mywindow(QtWidgets.QWidget,Ui_chatWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.sentbutton.clicked.connect(self.presssentbutton)

    def presssentbutton(self):
        s = self.textsent.toPlainText()
        strin = str(s)
        if strin:
            self.textreceive.append('Send:\n  ' + strin)
            strin = ''
        self.textsent.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())