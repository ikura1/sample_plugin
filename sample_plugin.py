from pathlib import Path

from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

from .sample_dialog import SampleDialog


class SamplePlugin:
    def __init__(self, iface):
        self.iface = iface
        self.action = None
        self.menu = "SamplePlugin"

    def initGui(self):
        # QGISがプラグインを初期化するために呼び出す関数
        icon_path = Path(__file__).parent / "icon.png"
        text = "SamplePlugin"
        parent = self.iface.mainWindow()
        icon = QIcon(icon_path)

        self.action = QAction(icon, text, parent)
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(self.menu, self.action)

    def unload(self):
        # QGISがプラグインを削除するために呼び出す関数
        self.iface.removePluginMenu(u"&SamplePlugin", self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        self.dlg = SampleDialog()
        self.dlg.exec_()
