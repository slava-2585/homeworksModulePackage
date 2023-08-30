import datetime

from application.db.people import get_employees, read_pdf
from application.salary import calculate_salary

if __name__ == '__main__':
  calculate_salary()
  get_employees()
  print ('Вывод из PDF файла далее')
  read_pdf()
  print('Текущая дата и время ',datetime.datetime.now())
  