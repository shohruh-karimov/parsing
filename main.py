from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
import time
import os

url = 'https://ru.wikipedia.org/wiki/%D0%94%D0%B8%D0%BD%D0%B0%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D1%81%D0%B0%D0%B9%D1%82'
org = requests.get(url)
netext = BeautifulSoup(org.text, 'html.parser')
org = netext.body.p.text
print(org)

wb = Workbook()

ws = wb.active

ws.append([org])

wb.save('newfile23-08.xlsx')

time.sleep(5)
os.system(r'newfile23-08.xlsx')