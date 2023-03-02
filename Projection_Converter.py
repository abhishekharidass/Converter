# -*- coding: utf-8 -*-

#!/usr/bin/env python3

"""
Created on Thu Mar  2 15:43:13 2023
@author: Abhishek
"""
import sys
import utm
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QWidget, QPushButton

class ConverterGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create input fields for latitude/longitude and UTM coordinates
        self.lat_lon_input = QLineEdit()
        self.utm_input = QLineEdit()

        # Create output fields for latitude/longitude and UTM coordinates
        self.lat_lon_output = QLineEdit()
        self.utm_output = QLineEdit()

        # Create a button to perform the conversion
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert)

        # Create the main layout and add the input and output fields and button
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Latitude, Longitude (ex: 40.7128, -74.0060):"))
        input_layout.addWidget(self.lat_lon_input)
        input_layout.addWidget(QLabel("UTM (ex: 583959.37, 4507351.0, 18, T):"))
        input_layout.addWidget(self.utm_input)
        output_layout = QHBoxLayout()
        output_layout.addWidget(QLabel("Latitude, Longitude:"))
        output_layout.addWidget(self.lat_lon_output)
        output_layout.addWidget(QLabel("UTM:"))
        output_layout.addWidget(self.utm_output)
        main_layout.addLayout(input_layout)
        main_layout.addLayout(output_layout)
        main_layout.addWidget(self.convert_button)

        # Create a central widget and set the main layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def convert(self):
        # Check if the input is for latitude/longitude or UTM
        if "," in self.lat_lon_input.text().strip():
            # Convert latitude/longitude to UTM
            lat, lon = [float(x.strip()) for x in self.lat_lon_input.text().strip().split(",")]
            easting, northing, zone_number, zone_letter = utm.from_latlon(lat, lon)
            self.utm_output.setText("{:.2f}, {:.2f}, {}, {}".format(easting, northing, zone_number, zone_letter))
            self.lat_lon_output.setText("{:.4f}, {:.4f}".format(lat, lon))
        elif "," in self.utm_input.text().strip():
            # Convert UTM to latitude/longitude
            easting, northing, zone_number, zone_letter = [x.strip() for x in self.utm_input.text().strip().split(",")]
            lat, lon = utm.to_latlon(float(easting), float(northing), int(zone_number), zone_letter)
            self.lat_lon_output.setText("{:.4f}, {:.4f}".format(lat, lon))
            self.utm_output.setText("{:.2f}, {:.2f}, {}, {}".format(float(easting), float(northing), int(zone_number), zone_letter))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter_gui = ConverterGUI()
    converter_gui.show()
    sys.exit(app.exec_())




