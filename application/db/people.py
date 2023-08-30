from PyPDF2 import PdfReader


def get_employees():
  print('Запущена функция в модуле people')


def read_pdf():
  with open("application/db/pdf_file.pdf", 'rb') as pl:
    reader = PdfReader(pl)
    page = reader.pages[0]
    text = page.extract_text()
    print(text)
