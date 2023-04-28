import sqlite3
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QFileDialog
from PyQt5 import QtWidgets
import login
import vxod
from Vacancy import Ui_Vacancy
from Candidates import Ui_Candidates
from Interview import Ui_Interview
from Employee import Ui_Employee
from Department import Ui_Department
from Vacation import Ui_Vacation
from Task import Ui_Task
from Salary import Ui_Salary

db = sqlite3.connect('database.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users(login TEXT, password TEXT)''')
db.commit()

class Registration(QtWidgets.QMainWindow, login.Ui_Form): #регистрация
    def __init__(self):
        super(Registration, self).__init__()
        self.setupUi(self)
        self.lineEdit.setPlaceholderText('Введите логин')
        self.lineEdit_2.setPlaceholderText('Введите пароль')
        self.pushButton.pressed.connect(self.reg) #  регитрация
        self.pushButton_2.pressed.connect(self.login) #переход на вход
        

    def login(self): #показ класса логин (вход)
        self.login = Login()
        self.login.show()
        self.hide()


    def reg(self): #регитрация
        user_login = self.lineEdit.text()
        user_password = self.lineEdit_2.text()

        if len(user_login) == 0:
            return
        if len(user_password) == 0:
            return
        cursor.execute(f'SELECT login FROM users WHERE login = "{user_login}" ')
        if cursor.fetchone() is None:
            cursor.execute(f'INSERT INTO users VALUES("{user_login}","{user_password}")')
            self.label_2.setText(f'Аккаунт {user_login} успешно зарегистрирован')
            db.commit()
        else:
            self.label_2.setText('Такая запись уже имеется')

class Login(QtWidgets.QMainWindow, vxod.Ui_Form_1):# вход
    def __init__(self):
        super(Login,self).__init__()
        self.setupUi(self)
        self.lineEdit.setPlaceholderText('Введите логин')
        self.lineEdit_2.setPlaceholderText('Введите пароль')


        self.pushButton_2.pressed.connect(self.login)
        self.pushButton.pressed.connect(self.reg)


    def reg(self):
        self.reg=Registration()
        self.reg.show()
        self.hide()


    def login(self):
        try:
           user_login = self.lineEdit.text()
           user_password = self.lineEdit_2.text()

           if len(user_login) == 0:
              return
           if len(user_password) == 0:
              return

           cursor.execute(f'SELECT password FROM users WHERE login = "{user_login}"')
           check_pass = cursor.fetchall()

           cursor.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
           check_login = cursor.fetchall()
           print (check_login)
           print(check_pass)

           if check_pass[0][0] == user_password and check_login[0][0] == user_login:
              self.label_2.setText(f'Успешная авториазация')
              self.Vacancy = Form_Vacancy()
              self.Vacancy.show()
              self.hide()
           else:
            self.label_2.setText(f'Ошибка авторизации')
        except Exception as e:
            self.label_2.setText(f'Ошибка авторизации')

POISK_VACANCY = ['ID_vacancy', 'Title', 'Description', 'Requirements', 'Salary']
class Form_Vacancy(QWidget, Ui_Vacancy): #таблица вакансия
   def __init__(self):
       super(Form_Vacancy, self).__init__()
       self.setupUi(self)
       self.pushButton.clicked.connect(self.open_Vacancy)#открыть таблицу
       self.pushButton_2.clicked.connect(self.insert_Vacancy)#добавить строки
       self.lineEdit_8.setPlaceholderText('Введите ID')
       self.pushButton_3.clicked.connect(self.delete_Vacancy)#удалить строку
       self.lineEdit_11.setPlaceholderText('Введите ID')
       self.comboBox_2.addItems(POISK_VACANCY)
       self.pushButton_6.clicked.connect(self.search_Vacancy)#поиск
       self.pushButton_11.clicked.connect(self.update_record)#изменить
       self.pushButton_4.clicked.connect(self.show_Candidates)
       self.pushButton_5.clicked.connect(self.show_Interview)
       self.pushButton_7.clicked.connect(self.show_Employee)
       self.pushButton_8.clicked.connect(self.show_Department)
       self.pushButton_9.clicked.connect(self.show_Vacation)
       self.pushButton_10.clicked.connect(self.show_Task)
       self.pushButton_12.clicked.connect(self.show_Salary)

   def open_Vacancy(self): #кнопка добавить вакансия
       try:
           self.conn = sqlite3.connect('Management.db')
           cur = self.conn.cursor()
           data = cur.execute("select * from Vacancy;")
           col_name = [i[0] for i in data.description]
           data_rows = data.fetchall()
       except Exception as e:
           print ("Ощибки с подключением к БД")
           return e
       self.tableWidget.setColumnCount(len(col_name))
       self.tableWidget.setHorizontalHeaderLabels(col_name)
       self.tableWidget.setRowCount(0)
       for i, row in enumerate(data_rows):
           self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j,QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()

   def update(self, query="select * from Vacancy"): #после добавление сразу видно запись
       try:
           cur = self.conn.cursor()
           data = cur.execute(query).fetchall()
       except Exception as d:
           print(f"Проблемы с подкл {d}")
           return d
       self.tableWidget.setRowCount(0) #обнулмяем все данные из таблцы
       #заносим по новой
       for i, row in enumerate(data):
           self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()


   def insert_Vacancy(self): #кнопка добавить
       row = [self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text()]
       try:
           cur = self.conn.cursor()
           cur.execute(f"""insert into Vacancy(Title, Description, Requirements, Salary)
           values('{row[0]}','{row[1]}','{row[2]}','{row[3]}')""" )
           self.conn.commit()
           cur.close()
       except Exception as r:
           print("Не смогли добавить запись")
           return r
       self.update()#обращаемся к update чтобы сразу увидеть изменения в БД

   def delete_Vacancy(self):
        id = self.lineEdit_8.text()
        conn = sqlite3.connect('Management.db')
        c = conn.cursor()
        c.execute("DELETE FROM Vacancy WHERE ID_vacancy=?", (id,))
        conn.commit()
        conn.close()
        self.update()

   def search_Vacancy(self):
        column_name = self.comboBox_2.currentText()
        column_index = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentColumn())
        search_text = self.lineEdit_10.text()
        query = f"select * from Vacancy where {column_name} like '%{search_text}%'"
        self.update(query)

   def update_record(self):#изменение
       # Открываем соединение с базой данных
       conn = sqlite3.connect('Management.db')
       cursor = conn.cursor()

       # Получаем данные из полей ввода и метки с фото
       Title = self.lineEdit.text()
       Description = self.lineEdit_2.text()
       Requirements = self.lineEdit_3.text()
       Salary = self.lineEdit_4.text()

       # Получаем ID_emploee из поля ввода
       ID_vacancy = self.lineEdit_11.text()

       # Обновляем запись в таблице Emploee
       try:
           cursor.execute(
               """UPDATE Vacancy SET Title=?, Description=?, Requirements=?, Salary=? WHERE ID_vacancy=?""",
               (Title, Description, Requirements, Salary, ID_vacancy))
           conn.commit()
       except Exception as e:
           print("Ошибка при обновлении записи в таблице Emploee:", e)
       finally:
           cursor.close()
           conn.close()

       # Обновляем данные в таблице на форме
       self.update()

   def show_Candidates(self):
       self.SH_can = Form_Candidates()
       self.SH_can.show()

   def show_Interview(self):
       self.SH_int = Form_Interview()
       self.SH_int.show()


   def show_Employee(self):
       self.SH_emp = Form_Employee()
       self.SH_emp.show()

   def show_Department(self):
       self.SH_depv = Form_Department()
       self.SH_depv.show()

   def show_Vacation(self):
       self.SH_vac = Form_Vacation()
       self.SH_vac.show()

   def show_Task(self):
       self.SH_tas = Form_Task()
       self.SH_tas.show()

   def show_Salary(self):
       self.SH_sal = Form_Salary()
       self.SH_sal.show()


POISK_Candidates = ['ID_Candidate', 'LastName', 'FirstName', 'Middle_name', 'Phone', 'Email', 'Passport_series', 'Passport_number', 'ID_vacancy']
class Form_Candidates(QWidget, Ui_Candidates): #таблица вакансия
   def __init__(self):
       super(Form_Candidates, self).__init__()
       self.setupUi(self)
       self.pushButton.clicked.connect(self.open_Candidates)
       self.pushButton_2.clicked.connect(self.insert_Candidates)
       self.pushButton_10.clicked.connect(self.select_image)
       self.pushButton_3.clicked.connect(self.delete_Candidates)
       self.comboBox_2.addItems(POISK_Candidates)
       self.pushButton_6.clicked.connect(self.search_Candidates)
       self.pushButton_11.clicked.connect(self.update_record)
       self.lineEdit_8.setPlaceholderText('Введите ID')
       self.lineEdit_11.setPlaceholderText('Введите ID')




   def open_Candidates(self):  # кнопка добавить
       try:
           self.conn = sqlite3.connect('Management.db')
           cur = self.conn.cursor()
           data = cur.execute("select * from Candidates;")
           col_name = [i[0] for i in data.description]
           data_rows = data.fetchall()
       except Exception as e:
           print("Ощибки с подключением к БД")
           return e
       self.tableWidget.setColumnCount(len(col_name))
       self.tableWidget.setHorizontalHeaderLabels(col_name)
       self.tableWidget.setRowCount(0)
       for i, row in enumerate(data_rows):
           self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()

   def update(self, query="select * from Candidates"):  # после добавление сразу видно запись
       try:
           cur = self.conn.cursor()
           data = cur.execute(query).fetchall()
       except Exception as d:
           print(f"Проблемы с подкл {d}")
           return d
       self.tableWidget.setRowCount(0)  # обнулмяем все данные из таблцы
       # заносим по новой
       for i, row in enumerate(data):
           self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()

   def select_image(self):  # фото
       file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Image Files (*.png *.jpg *.bmp)')
       if file_name:
           self.lineEdit_9.setText(file_name)
           pixmap = QPixmap(file_name)
           self.label_10.setPixmap(pixmap)

   def insert_Candidates(self):  # кнопка добавить
       row = [self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(),
              self.lineEdit_7.text(), self.lineEdit_6.text(),
              self.lineEdit_4.text(), self.lineEdit_5.text(), self.spinBox.text()]
       try:
           conn = sqlite3.connect('Management.db')  # фото
           with open(self.lineEdit_9.text(), 'rb') as f:  # фото
               image_data = f.read()  # фото
           cur = self.conn.cursor()
           cur.execute(f"""insert into Candidates(LastName,FirstName,Middle_name,Phone,Email,Passport_series,Passport_number,ID_vacancy, Photo)
           values('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}',?)""",
                       (image_data,))
           self.conn.commit()
           cur.close()
       except Exception as r:
           print("ошиб", r)
           return r
       self.update()  # обращаемся к update чтобы сразу увидеть изменения в БД

   def delete_Candidates(self):  # удалить агент
       id = self.lineEdit_8.text()
       conn = sqlite3.connect('Management.db')
       c = conn.cursor()
       c.execute("DELETE FROM Candidates WHERE ID_Candidate=?", (id,))
       conn.commit()
       conn.close()
       self.update()

   def search_Candidates(self):
       column_name = self.comboBox_2.currentText()
       column_index = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentColumn())
       search_text = self.lineEdit_10.text()
       query = f"select * from Candidates where {column_name} like '%{search_text}%'"
       self.update(query)

   def update_record(self):  # изменение
       # Открываем соединение с базой данных
       conn = sqlite3.connect('Management.db')
       cursor = conn.cursor()

       # Получаем данные из полей ввода и метки с фото
       LastName = self.lineEdit.text()
       FirstName = self.lineEdit_2.text()
       Middle_name = self.lineEdit_3.text()
       Phone = self.lineEdit_7.text()
       Email = self.lineEdit_6.text()
       Passport_series = self.lineEdit_4.text()
       Passport_number = self.lineEdit_5.text()
       ID_vacancy = self.spinBox.text()
       Photo = self.lineEdit_9.text()

       # Преобразуем фото в бинарный формат
       if Photo:
           with open(Photo, 'rb') as f:
               photo_data = f.read()
       else:
           photo_data = None

       # Получаем ID_emploee из поля ввода
       ID_Candidate = self.lineEdit_11.text()

       # Обновляем запись в таблице Emploee
       try:
           cursor.execute(
               """UPDATE Candidates SET LastName=?, FirstName=?, Middle_name=?, Phone=?, Email=?, Passport_series=?, Passport_number=?, ID_vacancy=?, Photo=? WHERE ID_Candidate=?""",
               (LastName, FirstName, Middle_name, Phone, Email, Passport_series, Passport_number, ID_vacancy, photo_data,
                ID_Candidate))
           conn.commit()
       except Exception as e:
           print("Ошибка при обновлении записи в таблице Emploee:", e)
       finally:
           cursor.close()
           conn.close()
       # Обновляем данные в таблице на форме
       self.update()


POISK_Interview = ['interview_id', 'candidate_id', 'interview_date', 'interview_time', 'Location', 'ID_Solution']

class Form_Interview(QWidget, Ui_Interview): #таблица вакансия
   def __init__(self):
       super(Form_Interview, self).__init__()
       self.setupUi(self)
       self.pushButton.clicked.connect(self.open_Interview)#открыть таблицу
       self.pushButton_2.clicked.connect(self.insert_Interview)#добавить строки
       self.lineEdit_11.setPlaceholderText('Введите ID')
       self.pushButton_3.clicked.connect(self.delete_Interview)#удалить строку
       self.lineEdit_8.setPlaceholderText('Введите ID')
       self.comboBox_2.addItems(POISK_Interview)
       self.pushButton_6.clicked.connect(self.search_Interview)#поиск
       self.pushButton_11.clicked.connect(self.update_Interview)#изменить


   def open_Interview(self): #кнопка добавить вакансия
       try:
           self.conn = sqlite3.connect('Management.db')
           cur = self.conn.cursor()
           data = cur.execute("select * from Interview;")
           col_name = [i[0] for i in data.description]
           data_rows = data.fetchall()
       except Exception as e:
           print ("Ощибки с подключением к БД")
           return e
       self.tableWidget.setColumnCount(len(col_name))
       self.tableWidget.setHorizontalHeaderLabels(col_name)
       self.tableWidget.setRowCount(0)
       for i, row in enumerate(data_rows):
           self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j,QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()

   def update(self, query="select * from Interview"): #после добавление сразу видно запись
       try:
           cur = self.conn.cursor()
           data = cur.execute(query).fetchall()
       except Exception as d:
           print(f"Проблемы с подкл {d}")
           return d
       self.tableWidget.setRowCount(0) #обнулмяем все данные из таблцы
       #заносим по новой
       for i, row in enumerate(data):
           self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()


   def insert_Interview(self): #кнопка добавить
       row = [self.spinBox_2.text(), self.dateEdit.text(), self.timeEdit.text(), self.lineEdit_7.text(), self.spinBox.text()]
       try:
           cur = self.conn.cursor()
           cur.execute(f"""insert into Interview(candidate_id, interview_date, interview_time, Location, ID_Solution)
           values('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}')""" )
           self.conn.commit()
           cur.close()
       except Exception as r:
           print("Не смогли добавить запись")
           return r
       self.update()#обращаемся к update чтобы сразу увидеть изменения в БД

   def delete_Interview(self):
        id = self.lineEdit_8.text()
        conn = sqlite3.connect('Management.db')
        c = conn.cursor()
        c.execute("DELETE FROM Interview WHERE interview_id=?", (id,))
        conn.commit()
        conn.close()
        self.update()

   def search_Interview(self):
        column_name = self.comboBox_2.currentText()
        column_index = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentColumn())
        search_text = self.lineEdit_10.text()
        query = f"select * from Interview where {column_name} like '%{search_text}%'"
        self.update(query)

   def update_Interview(self):#изменение
       # Открываем соединение с базой данных
       conn = sqlite3.connect('Management.db')
       cursor = conn.cursor()

       # Получаем данные из полей ввода и метки с фото
       candidate_id = self.spinBox_2.text()
       interview_date = self.dateEdit.text()
       interview_time = self.timeEdit.text()
       Location = self.lineEdit_7.text()
       ID_Solution = self.spinBox.text()

       # Получаем ID_emploee из поля ввода
       interview_id = self.lineEdit_11.text()

       # Обновляем запись в таблице Emploee
       try:
           cursor.execute(
               """UPDATE Interview SET candidate_id=?, interview_date=?, interview_time=?, Location=?, ID_Solution=?  WHERE interview_id=?""",
               (candidate_id, interview_date, interview_time, Location, ID_Solution,  interview_id))
           conn.commit()
       except Exception as e:
           print("Ошибка при обновлении записи в таблице Emploee:", e)
       finally:
           cursor.close()
           conn.close()

       # Обновляем данные в таблице на форме
       self.update()


POISK_Employee = ['Employee_id', 'LastName', 'FirstName', 'Middle_name', 'Birthday', 'Phone', 'Mail', 'Passport_series', 'Passport_number', 'Position', 'Date_of_employment', 'Photo', 'id_Department']
POSITION = ['Инженер', 'Разработчик', 'Аналитик', 'Дизайнер', 'Маркетолог', 'Кадровик', 'Представитель', 'Сис. админ', 'Экономист']
class Form_Employee(QWidget, Ui_Employee): #таблица вакансия
   def __init__(self):
       super(Form_Employee, self).__init__()
       self.setupUi(self)
       self.comboBox_3.addItems(POSITION)
       self.pushButton.clicked.connect(self.open_Employee)
       self.pushButton_2.clicked.connect(self.insert_Employee)
       self.pushButton_10.clicked.connect(self.select_image)
       self.pushButton_3.clicked.connect(self.delete_Employee)
       self.comboBox_2.addItems(POISK_Employee)
       self.pushButton_6.clicked.connect(self.search_Employee)
       self.pushButton_11.clicked.connect(self.update_record)
       self.lineEdit_8.setPlaceholderText('Введите ID')
       self.lineEdit_11.setPlaceholderText('Введите ID')



   def open_Employee(self):  # кнопка добавить
       try:
           self.conn = sqlite3.connect('Management.db')
           cur = self.conn.cursor()
           data = cur.execute("select * from Employee;")
           col_name = [i[0] for i in data.description]
           data_rows = data.fetchall()
       except Exception as e:
           print("Ощибки с подключением к БД")
           return e
       self.tableWidget.setColumnCount(len(col_name))
       self.tableWidget.setHorizontalHeaderLabels(col_name)
       self.tableWidget.setRowCount(0)
       for i, row in enumerate(data_rows):
           self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()

   def update(self, query="select * from Employee"):  # после добавление сразу видно запись
       try:
           cur = self.conn.cursor()
           data = cur.execute(query).fetchall()
       except Exception as d:
           print(f"Проблемы с подкл {d}")
           return d
       self.tableWidget.setRowCount(0)  # обнулмяем все данные из таблцы
       # заносим по новой
       for i, row in enumerate(data):
           self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()

   def select_image(self):  # фото
       file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Image Files (*.png *.jpg *.bmp)')
       if file_name:
           self.lineEdit_9.setText(file_name)
           pixmap = QPixmap(file_name)
           self.label_10.setPixmap(pixmap)

   def insert_Employee(self):  # кнопка добавить
       row = [self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(),
              self.lineEdit_12.text(), self.lineEdit_7.text(),
              self.lineEdit_6.text(), self.lineEdit_4.text(), self.lineEdit_5.text(),self.comboBox_3.itemText(self.comboBox_3.currentIndex()), self.lineEdit_13.text(), self.spinBox.text()]
       try:
           conn = sqlite3.connect('Management.db')  # фото
           with open(self.lineEdit_9.text(), 'rb') as f:  # фото
               image_data = f.read()  # фото
           cur = self.conn.cursor()
           cur.execute(f"""insert into Employee(LastName,FirstName,Middle_name,Birthday,Phone,Mail,Passport_series,Passport_number, Position, Date_of_employment, Photo, id_Department)
           values('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}','{row[9]}','{row[10]}',?)""",
                       (image_data,))
           self.conn.commit()
           cur.close()
       except Exception as r:
           print("ошиб", r)
           return r
       self.update()  # обращаемся к update чтобы сразу увидеть изменения в БД

   def delete_Employee(self):  # удалить агент
       id = self.lineEdit_8.text()
       conn = sqlite3.connect('Management.db')
       c = conn.cursor()
       c.execute("DELETE FROM Employee WHERE Employee_id=?", (id,))
       conn.commit()
       conn.close()
       self.update()

   def search_Employee(self):
       column_name = self.comboBox_2.currentText()
       column_index = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentColumn())
       search_text = self.lineEdit_10.text()
       query = f"select * from Employee where {column_name} like '%{search_text}%'"
       self.update(query)

   def update_record(self):  # изменение
       # Открываем соединение с базой данных
       conn = sqlite3.connect('Management.db')
       cursor = conn.cursor()

       # Получаем данные из полей ввода и метки с фото
       LastName = self.lineEdit.text()
       FirstName = self.lineEdit_2.text()
       Middle_name = self.lineEdit_3.text()
       Birthday = self.lineEdit_12.text()
       Phone = self.lineEdit_7.text()
       Mail = self.lineEdit_6.text()
       Passport_series = self.lineEdit_4.text()
       Passport_number = self.lineEdit_5.text()
       Position = self.comboBox_3.itemText(self.comboBox_3.currentIndex())
       Date_of_employment = self.lineEdit_13.text()
       id_Department = self.spinBox.text()
       Photo = self.lineEdit_9.text()

       # Преобразуем фото в бинарный формат
       if Photo:
           with open(Photo, 'rb') as f:
               photo_data = f.read()
       else:
           photo_data = None

       # Получаем ID_emploee из поля ввода
       Employee_id = self.lineEdit_11.text()

       # Обновляем запись в таблице Emploee
       try:
           cursor.execute(
               """UPDATE Employee SET LastName=?, FirstName=?, Middle_name=?, Birthday=?, Phone=?, Mail=?, Passport_series=?, Passport_number=?, Position=?, Date_of_employment=?, id_Department=?, Photo=? WHERE Employee_id=?""",
               (LastName, FirstName, Middle_name, Birthday, Phone, Mail, Passport_series, Passport_number, Position, Date_of_employment, id_Department, photo_data,
                Employee_id))
           conn.commit()
       except Exception as e:
           print("Ошибка при обновлении записи в таблице Emploee:", e)
       finally:
           cursor.close()
           conn.close()
       # Обновляем данные в таблице на форме
       self.update()



POISK_Department = ['id_Department', 'Title', 'Description', 'Manager']
class Form_Department(QWidget, Ui_Department): #таблица вакансия
   def __init__(self):
       super(Form_Department, self).__init__()
       self.setupUi(self)
       self.pushButton.clicked.connect(self.open_Department)#открыть таблицу
       self.pushButton_2.clicked.connect(self.insert_Department)#добавить строки
       self.lineEdit_8.setPlaceholderText('Введите ID')
       self.pushButton_3.clicked.connect(self.delete_Department)#удалить строку
       self.lineEdit_11.setPlaceholderText('Введите ID')
       self.comboBox_2.addItems(POISK_Department)
       self.pushButton_6.clicked.connect(self.search_Department)#поиск
       self.pushButton_11.clicked.connect(self.update_record)#изменить

   def open_Department(self): #кнопка добавить вакансия
       try:
           self.conn = sqlite3.connect('Management.db')
           cur = self.conn.cursor()
           data = cur.execute("select * from Department;")
           col_name = [i[0] for i in data.description]
           data_rows = data.fetchall()
       except Exception as e:
           print ("Ощибки с подключением к БД")
           return e
       self.tableWidget.setColumnCount(len(col_name))
       self.tableWidget.setHorizontalHeaderLabels(col_name)
       self.tableWidget.setRowCount(0)
       for i, row in enumerate(data_rows):
           self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j,QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()

   def update(self, query="select * from Department"): #после добавление сразу видно запись
       try:
           cur = self.conn.cursor()
           data = cur.execute(query).fetchall()
       except Exception as d:
           print(f"Проблемы с подкл {d}")
           return d
       self.tableWidget.setRowCount(0) #обнулмяем все данные из таблцы
       #заносим по новой
       for i, row in enumerate(data):
           self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()


   def insert_Department(self): #кнопка добавить
       row = [self.lineEdit_2.text(), self.lineEdit_3.text(), self.spinBox.text()]
       try:
           cur = self.conn.cursor()
           cur.execute(f"""insert into Department(Title, Description, Manager)
           values('{row[0]}','{row[1]}','{row[2]}')""" )
           self.conn.commit()
           cur.close()
       except Exception as r:
           print("Не смогли добавить запись")
           return r
       self.update()#обращаемся к update чтобы сразу увидеть изменения в БД

   def delete_Department(self):
        id = self.lineEdit_8.text()
        conn = sqlite3.connect('Management.db')
        c = conn.cursor()
        c.execute("DELETE FROM Department WHERE id_Department=?", (id,))
        conn.commit()
        conn.close()
        self.update()

   def search_Department(self):
        column_name = self.comboBox_2.currentText()
        column_index = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentColumn())
        search_text = self.lineEdit_10.text()
        query = f"select * from Department where {column_name} like '%{search_text}%'"
        self.update(query)

   def update_record(self):#изменение
       # Открываем соединение с базой данных
       conn = sqlite3.connect('Management.db')
       cursor = conn.cursor()

       # Получаем данные из полей ввода и метки с фото
       Title = self.lineEdit_2.text()
       Description = self.lineEdit_3.text()
       Manager = self.spinBox.text()

       # Получаем ID_emploee из поля ввода
       id_Department = self.lineEdit_11.text()

       # Обновляем запись в таблице Emploee
       try:
           cursor.execute(
               """UPDATE Department SET Title=?, Description=?,Manager=?  WHERE id_Department=?""",
               (Title, Description, Manager,  id_Department))
           conn.commit()
       except Exception as e:
           print("Ошибка при обновлении записи в таблице Emploee:", e)
       finally:
           cursor.close()
           conn.close()

       # Обновляем данные в таблице на форме
       self.update()


POISK_Vacation = ['ID_vacation', 'ID_employee', 'Start_date', 'End_date', 'Vacation_type']
Vacation = ['Неоплачиваемый',  'Оплачиваемый', 'По уходу за ребенком', 'По беременности и родам' ,'Eжегодный дополнительный', 'Учебный']
class Form_Vacation(QWidget, Ui_Vacation): #таблица вакансия
   def __init__(self):
       super(Form_Vacation, self).__init__()
       self.setupUi(self)
       self.pushButton.clicked.connect(self.open_Vacation)#открыть таблицу
       self.pushButton_2.clicked.connect(self.insert_Vacation)#добавить строки
       self.lineEdit_8.setPlaceholderText('Введите ID')
       self.pushButton_3.clicked.connect(self.delete_Vacation)#удалить строку
       self.lineEdit_11.setPlaceholderText('Введите ID')
       self.comboBox_2.addItems(POISK_Vacation)
       self.pushButton_6.clicked.connect(self.search_Vacation)#поиск
       self.comboBox_3.addItems(Vacation)
       self.pushButton_11.clicked.connect(self.update_record)


   def open_Vacation(self): #кнопка добавить вакансия
       try:
           self.conn = sqlite3.connect('Management.db')
           cur = self.conn.cursor()
           data = cur.execute("select * from Vacation;")
           col_name = [i[0] for i in data.description]
           data_rows = data.fetchall()
       except Exception as e:
           print ("Ощибки с подключением к БД")
           return e
       self.tableWidget.setColumnCount(len(col_name))
       self.tableWidget.setHorizontalHeaderLabels(col_name)
       self.tableWidget.setRowCount(0)
       for i, row in enumerate(data_rows):
           self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j,QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()

   def update(self, query="select * from Vacation"): #после добавление сразу видно запись
       try:
           cur = self.conn.cursor()
           data = cur.execute(query).fetchall()
       except Exception as d:
           print(f"Проблемы с подкл {d}")
           return d
       self.tableWidget.setRowCount(0) #обнулмяем все данные из таблцы
       #заносим по новой
       for i, row in enumerate(data):
           self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()


   def insert_Vacation(self): #кнопка добавить
       row = [self.spinBox_2.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.comboBox_3.itemText(self.comboBox_3.currentIndex())]
       try:
           cur = self.conn.cursor()
           cur.execute(f"""insert into Vacation(ID_employee, Start_date, End_date, Vacation_type)
           values('{row[0]}','{row[1]}','{row[2]}','{row[3]}')""" )
           self.conn.commit()
           cur.close()
       except Exception as r:
           print("Не смогли добавить запись")
           return r
       self.update()#обращаемся к update чтобы сразу увидеть изменения в БД

   def delete_Vacation(self):
        id = self.lineEdit_8.text()
        conn = sqlite3.connect('Management.db')
        c = conn.cursor()
        c.execute("DELETE FROM Vacation WHERE ID_vacation=?", (id,))
        conn.commit()
        conn.close()
        self.update()

   def search_Vacation(self):
        column_name = self.comboBox_2.currentText()
        column_index = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentColumn())
        search_text = self.lineEdit_10.text()
        query = f"select * from Vacation where {column_name} like '%{search_text}%'"
        self.update(query)

   def update_record(self):#изменение
       # Открываем соединение с базой данных
       conn = sqlite3.connect('Management.db')
       cursor = conn.cursor()

       # Получаем данные из полей ввода и метки с фото
       ID_employee = self.spinBox_2.text()
       Start_date = self.lineEdit_2.text()
       End_date = self.lineEdit_3.text()
       Vacation_type = self.comboBox_3.itemText(self.comboBox_3.currentIndex())

       # Получаем ID_emploee из поля ввода
       ID_vacation = self.lineEdit_11.text()

       # Обновляем запись в таблице Emploee
       try:
           cursor.execute(
               """UPDATE Vacation SET ID_employee=?, Start_date=?, End_date=?, Vacation_type=? WHERE ID_vacation=?""",
               (ID_employee, Start_date, End_date, Vacation_type, ID_vacation))
           conn.commit()
       except Exception as e:
           print("Ошибка при обновлении записи в таблице Emploee:", e)
       finally:
           cursor.close()
           conn.close()

       # Обновляем данные в таблице на форме
       self.update()


POISK_Task = ['ID_task', 'ID_employee', 'Description', 'Task_issue_date', 'Task_completion_date']

class Form_Task(QWidget, Ui_Task): #таблица вакансия
   def __init__(self):
       super(Form_Task, self).__init__()
       self.setupUi(self)
       self.pushButton.clicked.connect(self.open_Task)#открыть таблицу
       self.pushButton_2.clicked.connect(self.insert_Task)#добавить строки
       self.lineEdit_8.setPlaceholderText('Введите ID')
       self.pushButton_3.clicked.connect(self.delete_Task)#удалить строку
       self.lineEdit_11.setPlaceholderText('Введите ID')
       self.comboBox_2.addItems(POISK_Task)
       self.pushButton_6.clicked.connect(self.search_Task)#поиск
       self.pushButton_11.clicked.connect(self.update_record)


   def open_Task(self): #кнопка добавить вакансия
       try:
           self.conn = sqlite3.connect('Management.db')
           cur = self.conn.cursor()
           data = cur.execute("select * from Task;")
           col_name = [i[0] for i in data.description]
           data_rows = data.fetchall()
       except Exception as e:
           print ("Ощибки с подключением к БД")
           return e
       self.tableWidget.setColumnCount(len(col_name))
       self.tableWidget.setHorizontalHeaderLabels(col_name)
       self.tableWidget.setRowCount(0)
       for i, row in enumerate(data_rows):
           self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j,QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()

   def update(self, query="select * from Task"): #после добавление сразу видно запись
       try:
           cur = self.conn.cursor()
           data = cur.execute(query).fetchall()
       except Exception as d:
           print(f"Проблемы с подкл {d}")
           return d
       self.tableWidget.setRowCount(0) #обнулмяем все данные из таблцы
       #заносим по новой
       for i, row in enumerate(data):
           self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()


   def insert_Task(self): #кнопка добавить
       row = [self.spinBox_2.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_7.text()]
       try:
           cur = self.conn.cursor()
           cur.execute(f"""insert into Task(ID_employee, Description, Task_issue_date, Task_completion_date)
           values('{row[0]}','{row[1]}','{row[2]}','{row[3]}')""" )
           self.conn.commit()
           cur.close()
       except Exception as r:
           print("Не смогли добавить запись")
           return r
       self.update()#обращаемся к update чтобы сразу увидеть изменения в БД

   def delete_Task(self):
        id = self.lineEdit_8.text()
        conn = sqlite3.connect('Management.db')
        c = conn.cursor()
        c.execute("DELETE FROM Task WHERE ID_task=?", (id,))
        conn.commit()
        conn.close()
        self.update()

   def search_Task(self):
        column_name = self.comboBox_2.currentText()
        column_index = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentColumn())
        search_text = self.lineEdit_10.text()
        query = f"select * from Task where {column_name} like '%{search_text}%'"
        self.update(query)

   def update_record(self):#изменение
       # Открываем соединение с базой данных
       conn = sqlite3.connect('Management.db')
       cursor = conn.cursor()

       # Получаем данные из полей ввода и метки с фото
       ID_employee = self.spinBox_2.text()
       Description = self.lineEdit_2.text()
       Task_issue_date = self.lineEdit_3.text()
       Task_completion_date = self.lineEdit_7.text()

       # Получаем ID_emploee из поля ввода
       ID_task = self.lineEdit_11.text()

       # Обновляем запись в таблице Emploee
       try:
           cursor.execute(
               """UPDATE Task SET ID_employee=?, Description=?, Task_issue_date=?, Task_completion_date=? WHERE ID_task=?""",
               (ID_employee, Description, Task_issue_date, Task_completion_date, ID_task))
           conn.commit()
       except Exception as e:
           print("Ошибка при обновлении записи в таблице Emploee:", e)
       finally:
           cursor.close()
           conn.close()

       # Обновляем данные в таблице на форме
       self.update()


POISK_Salary = ['ID','ID_employee', 'Salary_amount', 'ID_bonus', 'ID_fine', 'Total']

class Form_Salary(QWidget, Ui_Salary): #таблица вакансия
   def __init__(self):
       super(Form_Salary, self).__init__()
       self.setupUi(self)
       self.pushButton.clicked.connect(self.open_Salary)#открыть таблицу
       self.pushButton_2.clicked.connect(self.insert_Salary)#добавить строки
       self.lineEdit_8.setPlaceholderText('Введите ID')
       self.pushButton_3.clicked.connect(self.delete_Salary)#удалить строку
       self.lineEdit_11.setPlaceholderText('Введите ID')
       self.comboBox_2.addItems(POISK_Salary)
       self.pushButton_6.clicked.connect(self.search_Salary)#поиск
       self.pushButton_11.clicked.connect(self.update_record)


   def open_Salary(self): #кнопка добавить вакансия
       try:
           self.conn = sqlite3.connect('Management.db')
           cur = self.conn.cursor()
           data = cur.execute("select * from Salary;")
           col_name = [i[0] for i in data.description]
           data_rows = data.fetchall()
       except Exception as e:
           print ("Ощибки с подключением к БД")
           return e
       self.tableWidget.setColumnCount(len(col_name))
       self.tableWidget.setHorizontalHeaderLabels(col_name)
       self.tableWidget.setRowCount(0)
       for i, row in enumerate(data_rows):
           self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j,QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()

   def update(self, query="select * from Salary"): #после добавление сразу видно запись
       try:
           cur = self.conn.cursor()
           data = cur.execute(query).fetchall()
       except Exception as d:
           print(f"Проблемы с подкл {d}")
           return d
       self.tableWidget.setRowCount(0) #обнулмяем все данные из таблцы
       #заносим по новой
       for i, row in enumerate(data):
           self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
           for j, elen in enumerate(row):
               self.tableWidget.setItem(i, j, QTableWidgetItem(str(elen)))
       self.tableWidget.resizeColumnsToContents()


   def insert_Salary(self): #кнопка добавить
       row = [self.spinBox_2.text(), self.spinBox_3.text(), self.spinBox_4.text(), self.spinBox_5.text(), self.spinBox_6.text()]
       try:
           cur = self.conn.cursor()
           cur.execute(f"""insert into Salary(ID_employee, Salary_amount, ID_bonus, ID_fine, Total)
           values('{row[0]}','{row[1]}','{row[2]}','{row[3]}','{row[4]}')""" )
           self.conn.commit()
           cur.close()
       except Exception as r:
           print("Не смогли добавить запись")
           return r
       self.update()#обращаемся к update чтобы сразу увидеть изменения в БД

   def delete_Salary(self):
        id = self.lineEdit_8.text()
        conn = sqlite3.connect('Management.db')
        c = conn.cursor()
        c.execute("DELETE FROM Salary WHERE ID=?", (id,))
        conn.commit()
        conn.close()
        self.update()

   def search_Salary(self):
        column_name = self.comboBox_2.currentText()
        column_index = self.tableWidget.horizontalHeaderItem(self.tableWidget.currentColumn())
        search_text = self.lineEdit_10.text()
        query = f"select * from Salary where {column_name} like '%{search_text}%'"
        self.update(query)

   def update_record(self):#изменение
       # Открываем соединение с базой данных
       conn = sqlite3.connect('Management.db')
       cursor = conn.cursor()

       # Получаем данные из полей ввода и метки с фото
       ID_employee = self.spinBox_2.text()
       Salary_amount = self.spinBox_3.text()
       ID_bonus = self.spinBox_4.text()
       ID_fine = self.spinBox_5.text()
       Total = self.spinBox_6.text()

       # Получаем ID_emploee из поля ввода
       ID = self.lineEdit_11.text()

       # Обновляем запись в таблице Emploee
       try:
           cursor.execute(
               """UPDATE Salary SET ID_employee=?, Salary_amount=?, ID_bonus=?, ID_fine=?, Total=?  WHERE ID=?""",
               (ID_employee, Salary_amount, ID_bonus, ID_fine, Total, ID))
           conn.commit()
       except Exception as e:
           print("Ошибка при обновлении записи в таблице Emploee:", e)
       finally:
           cursor.close()
           conn.close()

       # Обновляем данные в таблице на форме
       self.update()




App = QtWidgets.QApplication([])
window = Login()
window.show()
App.exec()