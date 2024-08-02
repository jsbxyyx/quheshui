import sys
from datetime import datetime

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui import main_ui
from ui import res_rc

___not_use = res_rc.qt_resource_name

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = main_ui.Ui_Form()
        self.ui.setupUi(self)

        self.create_notice_ui()
        self.create_tray()
        self.hide()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time_show)
        self.timer.start(1000)

    def create_notice_ui(self):
        desktop = QApplication.desktop()
        width = desktop.width()
        height = desktop.height()
        print(width, height)
        self.error_dialog = QWidget()
        self.error_dialog.setLayout(QVBoxLayout())
        self.error_dialog.setWindowFlags(Qt.CustomizeWindowHint)
        self.error_dialog.setMinimumSize(width, height)
        self.error_dialog.setFixedSize(width, height)
        self.error_dialog.setMaximumSize(width, height)

        label = QLabel('30秒后自动关闭')
        label.setMinimumSize(width, height)
        label.setAlignment(Qt.AlignCenter)

        self.error_dialog.layout().addWidget(label)
        self.error_dialog.setWindowTitle("去喝水")

    def create_tray(self):
        self._restore_action = QAction()
        self._quit_action = QAction()
        self._tray_icon_menu = QMenu()
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(":/res/icon.png"))
        self.tray_icon.setToolTip("去喝水")

        self._restore_action = QAction("显示", self)
        self._restore_action.triggered.connect(self.restore_from_tray)
        self._quit_action = QAction("退出", self)
        self._quit_action.triggered.connect(QApplication.quit)

        self._tray_icon_menu = QMenu(self)
        self._tray_icon_menu.addAction(self._restore_action)
        self._tray_icon_menu.addSeparator()
        self._tray_icon_menu.addAction(self._quit_action)
        self.tray_icon.setContextMenu(self._tray_icon_menu)
        self.tray_icon.show()

        self.tray_icon.activated.connect(self.tray_icon_activated)

    def tray_icon_activated(self, reason):
        # 当系统托盘图标被点击时的处理
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            # 如果点击的是触发事件（比如左键单击），则还原窗口
            self.restore_from_tray()

    def restore_from_tray(self):
        # 还原窗口
        if self.isMinimized():
            self.showNormal()
        elif self.isMaximized():
            self.showMaximized()
        else:
            self.show()

    def minimize_to_tray(self):
        # 最小化窗口到系统托盘
        self.hide()

    def time_show(self):
        now = datetime.now()
        t = now.strftime("%Y-%m-%d %H:%M:%S")
        self.ui.label_time.setText(t)

        minute = now.minute
        seconds = now.second
        if minute == 0 and seconds == 0:
            QTimer.singleShot(30000, self.close_error_dialog)
            self.error_dialog.show()
        pass

    def close_error_dialog(self):
        print('close error dialog')
        self.error_dialog.hide()

    def closeEvent(self, event):
        print('close event')
        event.ignore()
        self.hide()
        pass

    def changeEvent(self, event):
        print('change event')
        if event.type() == QEvent.WindowStateChange:
            if self.windowState() & Qt.WindowMinimized:
                event.ignore()
                self.hide()
                return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
