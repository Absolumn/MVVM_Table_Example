import sys
from PySide6.QtWidgets import QMainWindow, QHeaderView, QApplication
from PySide6.QtCore import Qt

from lib.item_model import CustomTableItemModel

from lib.ui.ui_TableWindow import Ui_TableExample



app = QApplication(sys.argv)

class TableExample(QMainWindow):
    def __init__(self, model:CustomTableItemModel):
        super().__init__()  #Must initialize base class
        self.setWindowTitle('Table Example')
        self.ui = Ui_TableExample()  #Connect the ui python file
        self.ui.setupUi(self)  #Create all the ui attributes
        table = self.ui.tbl_example
        table.setModel(model)  #Connect the model to the tableview
        table.setFocusPolicy(Qt.NoFocus) #Removes annoying dashed box around focused row
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch) #Allows column 0 to stretch to window size
        self.ui.le_add_entry.editingFinished.connect(lambda: model.create_entry(self.ui.le_add_entry.text())) #Text Entry Binding
        self.ui.pb_delete_entry.clicked.connect(lambda: model.delete_entry(table.selectedIndexes())) #Delete Entries Binding
