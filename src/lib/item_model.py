from enum import Enum
from typing import Union, Self, ClassVar, Any
from dataclasses import dataclass
from PySide6.QtCore import (Qt, QAbstractItemModel, 
                            QModelIndex, QPersistentModelIndex, QObject, Signal)


@dataclass
class Node:
    text: str


class TableNode:
    '''
    Table model
    '''
    _root:ClassVar[Self]

    def __init__(self, node:Node=None, parent:Self=None):
        super().__init__() #Must init the base class QObject
        self._node = node 
        self._parent = parent

        if parent == None: #If parent is none, instance must be the root node
            TableNode.add_root(self)
            self._children = []
        else:
            parent.children.append(self)

    @classmethod
    def add_root(cls, root:Self):
        assert not hasattr(cls, '_root'), 'Root has already been assigned'
        cls._root = root

    @classmethod
    def row_count(cls):
        try:
            return len(cls._root.children) 
        except:
            return 0

    @classmethod
    def get_child(cls, row:int):
        try:
            root = cls._root
            return root.children[row]
        except:
            return None              
    
    @property
    def row(self)->int:
        try: 
            root = self._parent
            return root.children.index(self) 
        except:
            return None
        
    @property
    def type_info(self)->str:
        if self._parent:
            return 'Node'
        else:
            return 'Root'
    
    @property
    def text(self)->str:
        #Only children nodes have text
        return self._node.text if self._parent else None
    
    @property
    def children(self) -> list:
        #Only the root node has children
        try:
            return self._children
        except:
            return None

    def add_child(self, child:Self)->None:
        if self.type_info == 'Root':
            self.children.append(child)
        else:
            raise TypeError('Only Root Node may have children..')         


class CustomTableItemModel(QAbstractItemModel):
    '''
    Table View Model
    '''
    def __init__(self, root:TableNode):
        super().__init__()
        self._root = root

    def headerData(self, section: int, orientation:Qt.Orientation, role:Enum) -> Any:
        '''
        Reimplemented Qt AbstractItemModel function
        
        Returns the header data stored under the given role for the header referred to by the section and orientation
        '''
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            match section:
                case 0:
                    return 'Task'
                case _:
                    return None
        else:
            return super().headerData(section, orientation, role)

    def data(self, index:QModelIndex, role:Enum)->Any:
        '''
        Reimplemented Qt AbstractItemModel function
        
        Returns the data stored under the given role for the item referred to by the index
        '''
        if not index.isValid():
            return None 

        if role == Qt.TextAlignmentRole:
            '''
            Returns the view alignment for each column
            '''
            match index.column():
                case 0:
                    return Qt.AlignLeft|Qt.AlignVCenter 
                case _:
                    return None
                                                           
        if role == Qt.DisplayRole or role == Qt.EditRole:
            '''
            Returns the data to display for each column at the given
            index
            '''
            node = self.get_node(index)
            match index.column():
                case 0:
                    return node.text
                case _:
                    return None
                
    def get_node(self, index:QModelIndex)->TableNode:
        '''
        Returns the TableNode at the given index.
        If index is invalid, returns the root node
        '''
        try:
            if index.isValid():
                node = index.internalPointer()
                if node:
                    return node
        except:
            pass
                
        return self._root
                
      
    def index(self, row: int, column: int, parent=QModelIndex()) -> QModelIndex:
        '''
        Reimplemented Qt AbstractItemModel function
        
        Returns the index of the item in the model specified 
        by the given row, column and parent index.
        '''
        parentNode = self.get_node(parent)
        
        childItem = parentNode.get_child(row)

        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex() 

    def rowCount(self, parent: Union[QModelIndex, QPersistentModelIndex]=QModelIndex()) -> int:
        '''
        Reimplemented Qt AbstractItemModel function
        
        Returns the number of rows under the given parent. 
        When the parent is valid it means that rowCount is 
        returning the number of children of parent.

        When implementing a table based model, 
        rowCount() should return 0 when the parent is valid.
        '''        
        if not parent.isValid():
            return self._root.row_count()
        else:
            return 0

    def columnCount(self, parent: Union[QModelIndex, QPersistentModelIndex]=None) -> int:
        '''
        Reimplemented Qt AbstractItemModel function
        
        Returns the number of columns for the children of the given parent.

        When implementing a table based model, 
        columnCount() should return 0 when the parent is valid.
        '''        
        if not parent.isValid():
            return 1
        else:
            return 0

    def setData(self, index:QModelIndex, value:str, role:Enum=Qt.EditRole):
        '''
        Reimplemented Qt AbstractItemModel function
        
        Sets the role data for the item at index to value

        Note:   This function is called if the user edits the data in the view.
                You would update the data of the node and then return True

                Example:
                    if role == Qt.EditRole:
                        node = index.internalPointer()
                        node.text = value
                        return True

        '''
        return False
    
    def parent(self, index):
        '''
        Required Reimplemented Qt AbstractItemModel function

        Returns the parent of the model item with the given index. 
        If the item has no parent, an invalid QModelIndex is returned.
        All Table nodes have no typical parent as you would see in a treeView,
        so an invalid index is always returned.
        '''
        return QModelIndex()    

    def flags(self, index: Union[QModelIndex, QPersistentModelIndex]) -> Qt.ItemFlag:
        '''
        Reimplemented Qt AbstractItemModel function

        Returns the item flags for the given index
        '''
        super_flags = super().flags(index)
        flags = Qt.ItemIsEnabled|Qt.ItemNeverHasChildren
        return super_flags|flags     
    
    def create_entry(self,entry:str)->None:
        '''
        Creates a new node with the provided entry text
        '''
        root = self._root
        node = Node(entry)
        table_node = TableNode(node, root)
        row = table_node.row
        self.beginInsertRows(QModelIndex(), row, row)
        self.endInsertRows()

    def delete_entry(self, selection:list[QModelIndex])->None:
        '''
        Deletes all selected rows from the model        
        '''
        root = self._root
        nodes = [index.internalPointer() for index in selection]
        for node in nodes:
            row = node.row
            root.children.pop(row)
            self.beginRemoveRows(QModelIndex(), row, row)
            self.endRemoveRows()
    


def build_table_item_model(model_list:str)->CustomTableItemModel:
    '''
    Takes a list of strings and returns a Table Item Model
    '''
    root = TableNode()
    for item in model_list:
        node = Node(item)
        TableNode(node,root)

    return CustomTableItemModel(root)   
