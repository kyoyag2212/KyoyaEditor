from PySide2 import QtWidgets
from kyoya.filebrowser.ui import main


class MyFileBrowser(main.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(MyFileBrowser, self).__init__()
        self.setupUi(self)
        self.populate()

    def populate(self):
        path = r"/home"
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(path)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        self.treeView.setSortingEnabled(True)



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = MyFileBrowser()
    fb.show()
    app.exec_()