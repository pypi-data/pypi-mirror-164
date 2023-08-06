import sys
from PyQt5.QtCore import Qt
import yaml
from qtpy import QtGui
from qtpy import QtWidgets
import os
import subprocess
import platform


class Example(QtWidgets.QDialog):

    def __init__(self):
        super(Example, self).__init__()
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.pushButton = QtWidgets.QPushButton("Load yaml")
        self.verticalLayout.addWidget(self.pushButton)
        self.setLayout(self.verticalLayout)
        self.pushButton.clicked.connect(self.loadYaml)

    def loadYaml(self):
        fileName = "/Users/chenyang/Desktop/Developer/cpl/annolid/annolid/configs/keypoints.yaml"
        f = open(fileName)
        getData = yaml.safe_load(f)
        prettyData = yaml.dump(getData, default_flow_style=False)
        print(getData['EVENTS'], type(getData['EVENTS']))
        self.plainTextEdit.appendPlainText(str(prettyData))
        open_or_start_file(fileName)


def open_or_start_file(file_name):
    # macOS
    if platform.system() == 'Darwin':
        subprocess.call(('open', file_name))
    # Windows
    elif platform.system() == 'Windows':
        os.startfile(file_name)
    # linux
    else:
        subprocess.call(('xdg-open', file_name))


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
