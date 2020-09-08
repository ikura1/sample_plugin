from pathlib import Path

from qgis.PyQt import QtGui, QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal

FORM_CLASS, _ = uic.loadUiType(str(Path(__file__).parent / "sample_dialog_base.ui"))


class SampleDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(SampleDialog, self).__init__(parent)
        self.setupUi(self)
