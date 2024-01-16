import io
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStatusBar

import location, dash, create_widgets

# import gmaps
# gmaps.configure(api_key='AIzaSyBUiLFkdSyaICX5TQQzBogB1169GO2KPtg')



class ui_main_window(object):
    def setup_window(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(850, 690)

        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")
        main_window.setStatusBar(self.status_bar)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.resize(850, 690)
        self.central_widget.setObjectName("display")

        self.tab_widget = QtWidgets.QTabWidget(self.central_widget)
        self.tab_widget.resize(850, 690)

        self.dash_tab = QtWidgets.QWidget()
        self.dash_tab.setObjectName("tab1")

        self.maps_tab = QtWidgets.QWidget()
        self.maps_tab.setObjectName("tab2")

        self.saved_tab = QtWidgets.QWidget()
        self.saved_tab.setObjectName("tab3")

        self.widget = QtWidgets.QWidget(self.dash_tab)

        self.tab_widget.addTab(self.dash_tab, "Dashboard")
        self.tab_widget.addTab(self.maps_tab, "Maps")
        self.tab_widget.addTab(self.saved_tab, "Saved")

        self.map_frame = QtWidgets.QVBoxLayout(self.central_widget)

        Screen1 = dash.dash_screen(self.dash_tab)
        Screen1.control_dashboard()

        Screen2 = location.maps_screen(self.maps_tab)
        Screen2.control_maps()

        self.status_bar = QtWidgets.QStatusBar(main_window)
        main_window.setStatusBar(self.status_bar)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    with open("styles.css", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    main_window = QtWidgets.QMainWindow()
    ui = ui_main_window()
    ui.setup_window(main_window)
    main_window.show()
    sys.exit(app.exec_())