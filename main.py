from algorithm import PlantIdentifier
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QGroupBox, QFileDialog, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtCore, QtGui

def toIdentify():
    groupbox_2.resize(0,0)
    groupbox.resize(400, 400)
    layout.addWidget(groupbox)
    layout.removeWidget(groupbox_2)

def toMap():
    groupbox.resize(0,0)
    groupbox_2.resize(400,400)
    layout.removeWidget(groupbox)
    layout.addWidget(groupbox_2)

def inputting():
    '''variate = input_box.text()
    if variate == "lily":
        image_content = QPixmap('images/lily.jpg')
        image_content_2 = image_content.scaled(250, 250)
        image_tbi.setPixmap(image_content_2)
    elif variate == "lotus":
        image_content = QPixmap('images/lotus.jpg')
        image_content_2 = image_content.scaled(250, 250)
        image_tbi.setPixmap(image_content_2)
    elif variate == "orchid":
        image_content = QPixmap('images/orchid.jpg')
        image_content_2 = image_content.scaled(250, 250)
        image_tbi.setPixmap(image_content_2)
    else:
        image_content = QPixmap('images/sunflower.jpg')
        image_content_2 = image_content.scaled(250, 250)
        image_tbi.setPixmap(image_content_2)'''
    # Open a file dialog to select an image file
    global file_path
    file_path, a = QFileDialog.getOpenFileName(self, 'Open Image', '.', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
    image_content = QPixmap(file_path)
    image_content_2 = image_content.scaled(300, 300)
    image_tbi.setPixmap(image_content_2)

def identify ():
    # Define the labels for the model
    labels = ['lily', 'lotus', 'orchid', 'sunflower']

    # Create an instance of the PlantIdentifier class
    model_path = 'plant_id_model_simple.h5'
    plant_id = PlantIdentifier(model_path, labels)

    # Predict the plant species of a new image
    image_path = file_path
    predicted_plant = plant_id.predict_plant_species(image_path)
    mbox = QMessageBox()
    mbox.setText(f"Predicted plant species: {predicted_plant}")
    mbox.setWindowTitle('Identifier tool')
    mbox.setWindowIcon(QtGui.QIcon('images/icon2.png'))
    mbox.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
    mbox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    self = QWidget()
    self.resize(500, 500)
    self.setWindowTitle('Identifier tool')
    self.setWindowIcon(QtGui.QIcon('images/icon2.png'))
    layout = QVBoxLayout()
    self.setLayout(layout)
    

    # define the button layout
    button_layout = QHBoxLayout()
    layout.addLayout(button_layout)

    # add a tab button
    identify_button = QPushButton("Identify")
    button_layout.addWidget(identify_button)
    identify_button.clicked.connect(toIdentify)

    # add a map button
    map_button = QPushButton("Map")
    button_layout.addWidget(map_button)
    map_button.clicked.connect(toMap)

    # groupbox for the input/buttons
    groupbox = QGroupBox("", self)
    layout.addWidget(groupbox)
    groupbox_layout = QVBoxLayout()
    groupbox.setLayout(groupbox_layout)

    # add an input button
    padding = QLabel("")
    padding_layout = QHBoxLayout()
    padding_H1 = QLabel("")
    padding_H2 = QLabel("")
    padding_layout.addWidget(padding_H1)
    padding_layout.addWidget(padding)
    padding_layout.addWidget(padding_H2)
    groupbox_layout.addLayout(padding_layout)

    # add an image, which shows which image will be 
    image_layout = QHBoxLayout()
    blank_image_1 = QLabel()
    blank_image_1.resize(50, 50)
    image_layout.addWidget(blank_image_1)
    image_tbi = QLabel()
    image_content = QPixmap('images/img icon.png')
    image_content_2 = image_content.scaled(300, 300)
    image_tbi.setPixmap(image_content_2)
    image_layout.addWidget(image_tbi)
    blank_image_2 = QLabel()
    blank_image_2.resize(50, 50)
    image_layout.addWidget(blank_image_2)
    groupbox_layout.addLayout(image_layout)

    # add a run button
    run_button = QPushButton("Run")
    input_button = QPushButton("Input Image")
    button_layout = QHBoxLayout()
    button_padding_H1 = QLabel("")
    button_padding_H2 = QLabel("")
    button_layout.addWidget(button_padding_H1)
    button_layout.addWidget(input_button)
    button_layout.addWidget(run_button)
    button_layout.addWidget(button_padding_H2)
    groupbox_layout.addLayout(button_layout)
    input_button.clicked.connect(inputting)
    run_button.clicked.connect(identify)

    # groupox 2 for the map
    groupbox_2 = QGroupBox("", self)
    layout.addWidget(groupbox_2)
    groupbox_2_layout = QVBoxLayout()
    groupbox_2.resize(0,0)
    groupbox_2.setLayout(groupbox_2_layout)

    # pixmap 2 boogaloo
    image_layout_2 = QHBoxLayout()
    blank_image_3 = QLabel()
    blank_image_3.resize(50, 50)
    image_layout_2.addWidget(blank_image_3)
    image_map = QLabel()
    image_data = QPixmap('images/tomato.jpg')
    image_data_2 = image_data.scaled(300, 300)
    image_map.setPixmap(image_data_2)
    image_layout_2.addWidget(image_map)
    blank_image_4 = QLabel()
    blank_image_4.resize(50, 50)
    image_layout_2.addWidget(blank_image_4)
    groupbox_2_layout.addLayout(image_layout_2)
    toIdentify()
    self.show()
    sys.exit(app.exec_())