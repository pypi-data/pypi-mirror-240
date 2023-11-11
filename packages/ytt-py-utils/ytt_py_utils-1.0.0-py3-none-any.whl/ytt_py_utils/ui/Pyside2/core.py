# System and core application related utils

def get_app():
    import sys
    from PySide2.QtWidgets import QApplication
    app = QApplication(sys.argv)
    return app