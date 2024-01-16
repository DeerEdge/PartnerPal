import webbrowser

from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore, QtWidgets
import sqlite3
import urllib
import requests

from PyQt5.QtGui import QPixmap, QImage


class dash_screen(object):
    def __init__(self, tab):
        super().__init__()
        self.dash_tab = tab
        self.control_dashboard()

    def control_dashboard(self):
        self.main_logo = QtWidgets.QLabel(self.dash_tab)
        self.pixmap = QtGui.QPixmap('logo.png')
        self.main_logo.setPixmap(self.pixmap)
        self.main_logo.setScaledContents(True)
        self.main_logo.resize(220, 70)
        self.main_logo.move(12, 5)

        self.groupbox = QtWidgets.QGroupBox(self.dash_tab)
        self.groupbox.setObjectName("GroupBox_Dash")
        self.groupbox.resize(220, 540)
        self.groupbox.move(12, 80)

        self.filters_label = QtWidgets.QLabel(self.groupbox)
        self.filters_label.setText("Filter By:")
        self.filters_label.setObjectName("Filters_Label")
        self.filters_label.move(20, 20)

        self.state_label = QtWidgets.QLabel(self.groupbox)
        self.state_label.setText("State:")
        self.state_label.setObjectName("State_Label")
        self.state_label.move(10, 61)

        self.state_dropdown = QtWidgets.QComboBox(self.groupbox)
        self.state_dropdown.setObjectName("State_Dropdown")
        self.state_dropdown.addItem("No Preference")
        self.state_dropdown.addItem("Alaska")
        self.state_dropdown.addItem("Arizona")
        self.state_dropdown.addItem("Arkansas")
        self.state_dropdown.addItem("California")
        self.state_dropdown.addItem("Colorado")
        self.state_dropdown.addItem("Florida")
        self.state_dropdown.addItem("Hawaii")
        self.state_dropdown.addItem("Idaho")
        self.state_dropdown.addItem("Indiana")
        self.state_dropdown.addItem("Kentucky")
        self.state_dropdown.addItem("Maine")
        self.state_dropdown.addItem("Michigan")
        self.state_dropdown.addItem("Minnesota")
        self.state_dropdown.addItem("Missouri")
        self.state_dropdown.addItem("Montana")
        self.state_dropdown.addItem("Nevada")
        self.state_dropdown.addItem("New Mexico")
        self.state_dropdown.addItem("North Dakota")
        self.state_dropdown.addItem("North Carolina")
        self.state_dropdown.addItem("Ohio")
        self.state_dropdown.addItem("Oregon")
        self.state_dropdown.addItem("South Carolina")
        self.state_dropdown.addItem("South Dakota")
        self.state_dropdown.addItem("Tennessee")
        self.state_dropdown.addItem("Texas")
        self.state_dropdown.addItem("Utah")
        self.state_dropdown.addItem("Virginia")
        self.state_dropdown.addItem("Washington")
        self.state_dropdown.addItem("West Virginia")
        self.state_dropdown.addItem("Wyoming")
        self.state_dropdown.resize(140, 40)
        self.state_dropdown.move(70, 50)


        self.features_label = QtWidgets.QLabel(self.groupbox)
        self.features_label.setText("Aspects:")
        self.features_label.setObjectName("Features_Label")
        self.features_label.move(10, 111)

        self.features_dropdown = QtWidgets.QComboBox(self.groupbox)
        self.features_dropdown.setObjectName("Features_Dropdown")
        self.features_dropdown.addItem("No Preference")
        self.features_dropdown.addItem("Forest")
        self.features_dropdown.addItem("Mountainous")
        self.features_dropdown.addItem("Lake/River")
        self.features_dropdown.addItem("Ocean")
        self.features_dropdown.addItem("Desert")
        self.features_dropdown.resize(140, 40)
        self.features_dropdown.move(70, 100)

        self.activities_label = QtWidgets.QLabel(self.groupbox)
        self.activities_label.setText("Activities:")
        self.activities_label.move(10, 161)

        self.activities_dropdown = QtWidgets.QComboBox(self.groupbox)
        self.activities_dropdown.setObjectName("Activities_Dropdown")
        self.activities_dropdown.addItem("No Preference")
        self.activities_dropdown.addItem("Bicycling")
        self.activities_dropdown.addItem("Boating")
        self.activities_dropdown.addItem("Diving")
        self.activities_dropdown.addItem("Camping")
        self.activities_dropdown.addItem("Climbing")
        self.activities_dropdown.addItem("Equestrianism")
        self.activities_dropdown.addItem("Fishing")
        self.activities_dropdown.addItem("Hiking")
        self.activities_dropdown.addItem("Hunting")
        self.activities_dropdown.addItem("Swimming")
        self.activities_dropdown.addItem("Skiing/Snowboarding")
        self.activities_dropdown.resize(140, 40)
        self.activities_dropdown.move(70, 150)

        self.distance_label = QtWidgets.QLabel(self.groupbox)
        self.distance_label.setText("Distance:")
        self.distance_label.move(10, 211)

        self.distance_dropdown = QtWidgets.QComboBox(self.groupbox)
        self.distance_dropdown.setObjectName("Distance_Dropdown")
        self.distance_dropdown.addItem("No Preference")
        self.distance_dropdown.addItem("50 miles")
        self.distance_dropdown.addItem("100 miles")
        self.distance_dropdown.addItem("500 miles")
        self.distance_dropdown.addItem("Custom")
        self.distance_dropdown.resize(140, 40)
        self.distance_dropdown.move(70, 200)

        self.QandA_search_bar_icon = QtWidgets.QLabel(self.dash_tab)
        self.QandA_search_bar_icon.setPixmap(QtGui.QPixmap("resources/magnifyingIcon.png"))
        self.QandA_search_bar_icon.setScaledContents(True)
        self.QandA_search_bar_icon.setFixedSize(30, 30)
        self.QandA_search_bar_icon.move(248, 24)
        self.QandA_search_bar_icon.show()

        self.searchbar = QtWidgets.QLineEdit(self.dash_tab)
        self.searchbar.resize(430, 33)
        self.searchbar.move(284, 22)

        self.filter_dropdown = QtWidgets.QComboBox(self.dash_tab)
        self.filter_dropdown.setObjectName("Features_Dropdown")
        self.filter_dropdown.addItem("Filter By:")
        self.filter_dropdown.addItem("Rating")
        self.filter_dropdown.addItem("Popularity")
        self.filter_dropdown.resize(118, 30)
        self.filter_dropdown.move(720, 24)

        self.map_container = QtWidgets.QGroupBox(self.dash_tab)
        self.map_container.setGeometry(QtCore.QRect(244, 60, 595, 560))
        self.maps_objects = self.create_QScrollArea("dash_tab", "maps_QScrollArea", "vertical_layout", 244, 60, 595, 560)
        self.maps = self.maps_objects[0]
        self.maps_layout = self.maps_objects[1]
        self.maps_scrollArea = self.maps_objects[2]

        self.populate_with_all()
        self.maps_scrollArea.setWidget(self.maps)
        self.maps_scrollArea.verticalScrollBar().setSliderPosition(0)

    def connect_and_retrieve_all(self, db_file, table_name):
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        SQLString = "SELECT * FROM " + table_name
        cur.execute(SQLString)
        rows = cur.fetchall()

        return rows

    # def convertToParkData(self, rows):
    #     for row in rows:
    #         data.id = row[0]

    def populate_with_all(self):
        park_list = self.connect_and_retrieve_all('identifier.sqlite', 'PARK_NAMES')
        # park_list = park_list[0:2]
        print(park_list)
        # global indiv_park
        for indiv_park in park_list:
            self.park_info_container = QtWidgets.QGroupBox(self.maps)
            self.park_info_container.setFixedSize(568, 200)
            self.park_info_container.setLayout(QtWidgets.QVBoxLayout())
            self.park_img = QtWidgets.QLabel(self.park_info_container)
            image_address = ["assets/0 - Acadia.jpeg", "assets/1 - Arches.jpeg"]
            self.park_img.setPixmap(QtGui.QPixmap(image_address))
            self.park_img.setScaledContents(True)
            self.park_img.move(10, 10)
            self.park_img.setFixedSize(180, 180)
            self.park_img.show()

            self.park_title_label = self.create_QLabel("park_info", "park_gbox_title", str(indiv_park[1]) + " - " + str(indiv_park[3]), 200, 5, 250, 40)
            self.park_distance_label = self.create_QLabel("park_info", "park_dist_label", "100 Miles Away", 470, 5, 250, 40)
            # self.park_loc_label = self.create_QLabel("park_info", "park_gbox", str(indiv_park[3]), 110, 25, 250, 40)
            self.output_logs = QtWidgets.QPlainTextEdit(self.park_info_container)
            self.output_logs.setFixedSize(328, 140)
            self.output_logs.move(200, 50)
            self.output_logs.setPlainText("     " + str(indiv_park[2]))
            self.output_logs.setReadOnly(True)

            self.website_button = QtWidgets.QToolButton(self.park_info_container)
            self.website_button.setGeometry(531, 50, 32, 32)
            self.website_button.setText("↗︎")
            self.website_url = indiv_park[6]
            self.website_button.clicked.connect(lambda: self.link())
            # self.website_button.clicked.connect(lambda: webbrowser.open(self.website_url))
            print(indiv_park[6])


            self.resource1_button = QtWidgets.QToolButton(self.park_info_container)
            self.resource1_button.setGeometry(531, 85, 32, 32)
            self.resource1_button.setText("↗︎")

            self.resource2_button = QtWidgets.QToolButton(self.park_info_container)
            self.resource2_button.setGeometry(531, 120, 32, 32)
            self.resource2_button.setText("↗︎")

            self.resource3_button = QtWidgets.QToolButton(self.park_info_container)
            self.resource3_button.setGeometry(531, 155, 32, 32)
            self.resource3_button.setText("↗︎")

            self.maps_layout.addWidget(self.park_info_container)

    def link(self):
        print('link clicked')
        url = QtCore.QUrl(self.website_url)
        QtGui.QDesktopServices.openUrl(url)

    def create_QLabel(self, container, object_name, text, x_coordinate, y_coordinate, width, length):
        # Creates and associates QLabel to specified container
        if container == "park_info":
            self.QLabel = QtWidgets.QLabel(self.park_info_container)
        elif container == "central_widget":
            self.QLabel = QtWidgets.QLabel(self.central_widget)
        elif container == "dashboard_tab":
            self.QLabel = QtWidgets.QLabel(self.dashboard_tab)
        elif container == "upcoming_events_tab":
            self.QLabel = QtWidgets.QLabel(self.upcoming_events_tab)
        elif container == "points_tab":
            self.QLabel = QtWidgets.QLabel(self.points_tab)
        elif container == "rewards_tab":
            self.QLabel = QtWidgets.QLabel(self.rewards_tab)
        elif container == "student_profile_tab":
            self.QLabel = QtWidgets.QLabel(self.student_profile_tab)
        elif container == "slideshow_description_groupbox":
            self.QLabel = QtWidgets.QLabel(self.slideshow_description_groupbox)
        elif container == "event":
            self.QLabel = QtWidgets.QLabel(self.event_object)

        self.QLabel.setWordWrap(True)
        self.QLabel.setObjectName(object_name)
        self.QLabel.setText(text)
        # Geometry of QLabel is specified by the passed function parameters
        self.QLabel.setGeometry(QtCore.QRect(x_coordinate, y_coordinate, width, length))
        return self.QLabel

    def create_QScrollArea(self, container, object_name, layout, x_coordinate, y_coordinate, fixed_width, min_length):
        self.scrollArea_object_container = QtWidgets.QWidget()
        if container == "dash_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.dash_tab)
        elif container == "dashboard_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.dashboard_tab)
        elif container == "maps_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.maps_tab)
        elif container == "points_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.points_tab)
        elif container == "rewards_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.rewards_tab)
        elif container == "admin_statistics_tab":
            self.QScrollArea = QtWidgets.QScrollArea(self.admin_statistics_tab)
        self.QScrollArea.setFixedWidth(fixed_width)
        self.QScrollArea.setFixedHeight(min_length)
        self.QScrollArea.move(x_coordinate, y_coordinate)
        self.QScrollArea.setWidgetResizable(True)
        self.QScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        if layout == "vertical_layout":
            self.scroll_vertical_layout = QtWidgets.QVBoxLayout(self.scrollArea_object_container)
            self.scrollArea_object_container.setLayout(self.scroll_vertical_layout)
            return [self.scrollArea_object_container, self.scroll_vertical_layout, self.QScrollArea]
        elif layout == "grid_layout":
            self.scroll_grid_layout = QtWidgets.QGridLayout(self.scrollArea_object_container)
            self.scrollArea_object_container.setLayout(self.scroll_grid_layout)
            self.QScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            return [self.scrollArea_object_container, self.scroll_grid_layout, self.QScrollArea]

