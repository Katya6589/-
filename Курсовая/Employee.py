# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Employee.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Employee(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(853, 747)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 460, 831, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.layoutWidget_3 = QtWidgets.QWidget(Form)
        self.layoutWidget_3.setGeometry(QtCore.QRect(700, 170, 137, 58))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_3.addWidget(self.lineEdit_11)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_3.addWidget(self.pushButton_11)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(420, 50, 261, 291))
        self.label_10.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(700, 60, 137, 94))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_2.addWidget(self.lineEdit_10)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(10, 9, 681, 31))
        self.label_9.setMinimumSize(QtCore.QSize(0, 31))
        self.label_9.setObjectName("label_9")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(310, 50, 103, 134))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout.addWidget(self.lineEdit_8)
        self.layoutWidget_4 = QtWidgets.QWidget(Form)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 50, 282, 430))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget_4)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_4)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_12)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget_4)
        self.comboBox_3.setObjectName("comboBox_3")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_13)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_10.setObjectName("pushButton_10")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.pushButton_10)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget_4)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.spinBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_11.setText(_translate("Form", "Изменить"))
        self.pushButton_6.setText(_translate("Form", "Найти"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt;\">Сотрудники</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Открыть"))
        self.pushButton_2.setText(_translate("Form", "Добавить"))
        self.pushButton_3.setText(_translate("Form", "Удалить"))
        self.label.setText(_translate("Form", "Фамилия"))
        self.label_2.setText(_translate("Form", "Имя"))
        self.label_3.setText(_translate("Form", "Отчество"))
        self.label_7.setText(_translate("Form", "Телефон"))
        self.label_8.setText(_translate("Form", "Email"))
        self.label_5.setText(_translate("Form", "Серия паспорта"))
        self.label_6.setText(_translate("Form", "Номер паспорта"))
        self.label_12.setText(_translate("Form", "Дата рождения"))
        self.label_13.setText(_translate("Form", "Должность"))
        self.label_14.setText(_translate("Form", "Дата приема на работу"))
        self.label_11.setText(_translate("Form", "Фото"))
        self.pushButton_10.setText(_translate("Form", "Выбрать фото"))
        self.label_4.setText(_translate("Form", "ID_Отдела"))
