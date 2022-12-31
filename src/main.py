import ctypes
import sys
import main_window
import lib.item_model as item_model

INITIAL_TEXT = [
                "Process email inbox",
                "Write blog post",
                "Prepare video scripts",
                "Tax accounting",
                "Prepare presentation",
                "Go to the gym",
]

def main()-> None:
    model = item_model.build_table_item_model(INITIAL_TEXT)
    window = main_window.TableExample(model)
    window.show()
    sys.exit(main_window.app.exec())



if __name__ == '__main__':
    myappid = u'Table.Example.VA' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    main()
