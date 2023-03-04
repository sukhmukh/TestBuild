'''
Created on 20-Sep-2020
Amazon.in : Sony
@author: LENOVO
'''
from selenium.webdriver.common.by import By

from ddtmethods import  XLUTils 
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.amazon.in')

path = r'C:\Users\HEMANTH\PycharmProjects\DataDriven\sample\pybook.xlsx'

rows = XLUTils.getRowCount(path,'Sheet1')
#print("the rowa ia ",rows)

for r in range(1, rows+1):
    input=XLUTils.readData(path, "Sheet1", r, 1)
    driver.find_element(By.ID,'twotabsearchtextbox').send_keys(input)
    driver.find_element(By.ID ,'nav-search-submit-button').click()
    time.sleep(3000)
    if XLUTils.readData(path,"Sheet1",r,2) in driver.title:
        #print("test passed")
        XLUTils.writeData(path,'Sheet1',r,3,"testpass")
    else:
        XLUTils.writeData(path,'Sheet1',r,3,"testfail")

