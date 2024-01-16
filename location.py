from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtWebEngineWidgets
import folium
import io
import csv
import pandas as pd
import sys
class maps_screen(object):
    def __init__(self, tab):
        super().__init__()
        self.maps_tab = tab
        self.control_maps()

    def control_maps(self):
        self.map_container = QtWidgets.QGroupBox(self.maps_tab)
        self.map_container.setGeometry(QtCore.QRect(0, 0, 850, 500))
        self.map_container.setEnabled(True)
        self.map_container.setFlat(True)

        layout = QtWidgets.QVBoxLayout(self.map_container)
        df = pd.read_csv('nationalparks.csv', usecols=['longitude', 'latitude', 'details', ])
        df.columns = ['Longitude', 'Latitude', 'Name']


        coordinate = (48.31521, -114.66929)
        map = folium.Map(
            title="Map",
            zoom_start=3,
            location=coordinate,
            control_scale=True
        )

        for i, row in df.iterrows():
            iframe = folium.IFrame('Name:' + str(row["Name"]))
            popup = folium.Popup(iframe, min_width=300, max_width=300)
            folium.Marker(location=[row['Latitude'], row['Longitude']],
                          popup=popup, c=row['Name']).add_to(map)


        data = io.BytesIO()
        map.save(data, close_file=False)

        webView = QtWebEngineWidgets.QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)
        self.map_container.setLayout(layout)








