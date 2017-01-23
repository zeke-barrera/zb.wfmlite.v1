'''
Created on Jan 22, 2017

@author: ebarrer
'''
import sys
from PyQt4 import QtGui

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    window.setGeometry(50, 50, 500, 300)
    window.setWindowTitle("PyQT Test!")
    window.show()
    sys.exit(app.exec_())