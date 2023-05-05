import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QGroupBox, QGridLayout, QRadioButton, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5 import QtCore, QtGui

def implement ():
    mbox = QMessageBox()
    mbox.setText("This feature is not implemented")
    mbox.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
    mbox.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    self = QWidget()
    self.resize(1000, 500)
    self.setWindowTitle('Monitoring tool')
    self.setStyleSheet("""
        .section_6, .section_7, .section_8 {
            width: 33.33%;
            float: left;
            box-sizing: border-box;
            }
        """)
    self.setWindowIcon(QtGui.QIcon('images/icon_monitor_2.png'))
    main_layout = QHBoxLayout()
    self.setLayout(main_layout)
    layout = QVBoxLayout()
    layout_2 = QVBoxLayout()
    layout_3 = QVBoxLayout()
    layout_4 = QVBoxLayout()
    main_layout.addLayout(layout)
    main_layout.addLayout(layout_2)    
    main_layout.addLayout(layout_3)    
    main_layout.addLayout(layout_4)    

    # first section
    section_1 = QGroupBox("First Sensor Waist", self)
    layout.addWidget(section_1)
        
    section_1_layout = QVBoxLayout()
    section_1.setLayout(section_1_layout)
    
    roll_label = QLabel("Roll:")
    section_1_layout.addWidget(roll_label)
    roll_qlineedit = QLineEdit()
    section_1_layout.addWidget(roll_qlineedit)
    pitch_label = QLabel("Pitch:")
    section_1_layout.addWidget(pitch_label)
    pitch_qlineedit = QLineEdit()
    section_1_layout.addWidget(pitch_qlineedit)
    accel_label = QLabel("Accleration:")
    section_1_layout.addWidget(accel_label)
    accel_qlineedit = QLineEdit()
    section_1_layout.addWidget(accel_qlineedit)

    # second section
    section_2 = QGroupBox("Second Sensor Left Things", self)
    layout_2.addWidget(section_2)
        
    section_2_layout = QVBoxLayout()
    section_2.setLayout(section_2_layout)
    
    roll_label = QLabel("Roll:")
    section_2_layout.addWidget(roll_label)
    roll_qlineedit = QLineEdit()
    section_2_layout.addWidget(roll_qlineedit)
    pitch_label = QLabel("Pitch:")
    section_2_layout.addWidget(pitch_label)
    pitch_qlineedit = QLineEdit()
    section_2_layout.addWidget(pitch_qlineedit)
    accel_label = QLabel("Accleration:")
    section_2_layout.addWidget(accel_label)
    accel_qlineedit = QLineEdit()
    section_2_layout.addWidget(accel_qlineedit)

    # third section
    section_3 = QGroupBox("Third Sensor Right Arm", self)
    layout_3.addWidget(section_3)
        
    section_3_layout = QVBoxLayout()
    section_3.setLayout(section_3_layout)
    
    roll_label = QLabel("Roll:")
    section_3_layout.addWidget(roll_label)
    roll_qlineedit = QLineEdit()
    section_3_layout.addWidget(roll_qlineedit)
    pitch_label = QLabel("Pitch:")
    section_3_layout.addWidget(pitch_label)
    pitch_qlineedit = QLineEdit()
    section_3_layout.addWidget(pitch_qlineedit)
    accel_label = QLabel("Accleration:")
    section_3_layout.addWidget(accel_label)
    accel_qlineedit = QLineEdit()
    section_3_layout.addWidget(accel_qlineedit)

    # fourth section
    section_4 = QGroupBox("Fourth Sensor Right Ankle", self)
    layout_4.addWidget(section_4)
        
    section_4_layout = QVBoxLayout()
    section_4.setLayout(section_4_layout)
    
    roll_label = QLabel("Roll:")
    section_4_layout.addWidget(roll_label)
    roll_qlineedit = QLineEdit()
    section_4_layout.addWidget(roll_qlineedit)
    pitch_label = QLabel("Pitch:")
    section_4_layout.addWidget(pitch_label)
    pitch_qlineedit = QLineEdit()
    section_4_layout.addWidget(pitch_qlineedit)
    accel_label = QLabel("Accleration:")
    section_4_layout.addWidget(accel_label)
    accel_qlineedit = QLineEdit()
    section_4_layout.addWidget(accel_qlineedit)

    # fifth section
    section_5 = QGroupBox("Sensor disposition", self)
    layout.addWidget(section_5)
        
    section_5_layout = QVBoxLayout()
    section_5.setLayout(section_5_layout)
    
    the_image = QLabel()
    image_content = QPixmap('images/sensor_2.png')
    image_content_2 = image_content.scaled(216, 190)
    the_image.setPixmap(image_content_2)
    section_5_layout.addWidget(the_image)

    # sixth section
    section_6 = QGroupBox("Activity", self)
    layout_2.addWidget(section_6)

    section_6_layout = QVBoxLayout()
    section_6.setLayout(section_6_layout)

    activity_label = QLabel('Select Activity:')
    section_6_layout.addWidget(activity_label)
    radio_1 = QRadioButton("Random")
    radio_1.isChecked()
    section_6_layout.addWidget(radio_1)
    radio_2 = QRadioButton("Sitting")
    section_6_layout.addWidget(radio_2)
    radio_3 = QRadioButton("Sittingdown")
    section_6_layout.addWidget(radio_3)
    radio_4 = QRadioButton("Standing")
    section_6_layout.addWidget(radio_4)
    radio_5 = QRadioButton("Standingup")
    section_6_layout.addWidget(radio_5)
    radio_6 = QRadioButton("Walking")
    section_6_layout.addWidget(radio_6)

    # seventh section
    section_7 = QGroupBox(" ", self)
    layout_3.addWidget(section_7)

    section_7_layout = QVBoxLayout()
    section_7.setLayout(section_7_layout)
    
    run_button = QPushButton("Run")
    run_button.clicked.connect(implement)
    section_7_layout.addWidget(run_button)
    
    reset_button = QPushButton("Reset")
    reset_button.clicked.connect(implement)
    section_7_layout.addWidget(reset_button)

    act_sel_label = QLabel("Activity Select:")
    section_7_layout.addWidget(act_sel_label)

    act_sel_lineedit = QLineEdit()
    section_7_layout.addWidget(act_sel_lineedit)

    act_pre_label = QLabel("Activity Predict:")
    section_7_layout.addWidget(act_pre_label)
    
    act_pre_lineedit = QLineEdit()
    section_7_layout.addWidget(act_pre_lineedit)

    # eigth section
    section_8 = QGroupBox(" ", self)
    layout_4.addWidget(section_8)

    section_8_layout = QVBoxLayout()
    section_8.setLayout(section_8_layout)

    match_label = QLabel("Match:")
    section_8_layout.addWidget(match_label)

    match_lineedit = QLineEdit()
    section_8_layout.addWidget(match_lineedit)

    match_pct_label = QLabel("Match Percentage:")
    section_8_layout.addWidget(match_pct_label)
    
    match_pct_lineedit = QLineEdit()
    section_8_layout.addWidget(match_pct_lineedit)

    self.show()
    sys.exit(app.exec_())
