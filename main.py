from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Login import Ui_Form
from indexgui import Ui_IndexForm
import sys
#from socket import *
#import threading

class indexwindow(QtWidgets.QWidget,Ui_IndexForm):
    def __init__(self):
        super(indexwindow, self).__init__()
        self.setupUi(self)

    def hanelclick(self):
        if not self.isVisible():
            self.show()

class mywindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ifpushbutton)

    def ifpushbutton(self):
        nickname = self.nickname.toPlainText()
        if not nickname:
            msg_box = QMessageBox(QMessageBox.Warning, "Alert", "昵称不能为空！！", QMessageBox.Yes)
            msg_box.exec_()#窗口停留
            msg_box.show()
        else:
            _translate = QtCore.QCoreApplication.translate
            idewindow.nickname.setText(_translate("Form", nickname))
            idewindow.hanelclick()
            self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    idewindow = indexwindow()
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())