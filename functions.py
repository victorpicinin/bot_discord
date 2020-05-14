from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException   
import pandas as pd
from unicodedata import normalize
import re
import sys
import time
import datetime
from datetime import date
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

cap = DesiredCapabilities().FIREFOX
#cap = DesiredCapabilities().EDGE
cap["marionette"] = False
#driver = webdriver.Chrome()
#driver = driver.Chrome(executable_path=r"chromedriver.exe")

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=/Users/Victor/AppData/Local/Google/Chrome/User Data") #Path to your chrome profile
driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)

driver.maximize_window()

def frame_switch(name):
    driver.switch_to.frame(driver.find_element_by_id(name))

def frame_xpath_alike_switch(name):
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@id,'"+name+"')]"))

def get_true_text(tag):
    children = tag.find_elements_by_id(tag)
    original_text = tag.text
    for child in children:
        original_text = original_text.replace(child.text, '', 1)
    return original_text

def check_exists_by_id(id):
    try:
        driver.find_element_by_id(id)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def check_exists_by_text(text):
    try:
        driver.find_element_by_partial_link_text(text)
    except NoSuchElementException:
        return False
    return True

def check_exists_alike_by_xpath(htmltag,text):
    try:
        driver.find_element_by_xpath("//"+htmltag+"[contains(@id,'" + text +"')]")
    except NoSuchElementException:
        return False
    return True

def check_exists_xpath_text(htmltag,text):
    try:
        driver.find_element_by_xpath("//"+htmltag+"[contains(text(),'" + text +"')]")
    except NoSuchElementException:
        return False
    return True

def wait_and_click_for_element_id(element):
    while check_exists_by_id(element) == False:
        print('Waiting...')
        time.sleep(1)
    print('Next Step')
    driver.find_element_by_id(element).click()

def wait_and_click_for_element_text(element):
    while check_exists_by_text(element) == False:
        print('Waiting...')
        time.sleep(1)
    print('Next Step')
    time.sleep(0.3)
    driver.find_element_by_partial_link_text(element).click()

def wait_for_element_id(element):
    while check_exists_by_id(element) == False:
        print('Waiting...')
        time.sleep(1)
    print('Next Step')

def wait_for_element_text(element):
    while check_exists_by_text(element) == False:
        print('Waiting...')
        time.sleep(1)
    print('Next Step')

def sys_exit(msg):
    sys.exit(msg)
    print('END OF EXECUTION')

def select_by_value(webElement, value):
        options = webElement.find_elements_by_tag_name("option")
        for option in options:
            if option.text == value:
                webElement.click()
                webElement.send_keys(option.text)

def check_for_error_msg(field,mensagem):
    driver.switch_to.default_content()
    if check_exists_by_id(field) == True:
        driver.find_element_by_id('#ICOK').click()
        return True
    else:
        print(mensagem)
    return False

def chek_frame(frame):
    driver.switch_to.default_content()
    if check_exists_by_id(frame) == True:
        frame_switch(frame)

def formata_data(column):
    if row[column].day <= 9:
        day = '0'+str(row[column].day)
    else:
        day = str(row[column].day)

    if row[column].month <= 9:
        month = '0'+str(row[column].month)
    else:
        month = row[column].month
    return '{}/{}/{}'.format(day,month,row[column].year)

def wait_xpath_fixed(htmltag,text,tentaiva,msg):
    i=0
    while check_exists_alike_by_xpath(htmltag,text) == False and i < tentaiva:
        i=i+1
        print('Waiting... ' +str(i))
        time.sleep(1)
    if i == tentaiva and check_exists_alike_by_xpath(htmltag,text) == False:
        print(msg)
        result = False
    else:
        result = True
    if result == False:
        return False
    elif result == True:
        print('Elemento ' + htmltag + ' encontrado')

def wait_and_click_for_element_id_fixed(element,tentaiva,msg):
    i=0
    while check_exists_by_id(element) == False and i < tentaiva:
        i=i+1
        print('Waiting... ' +str(i))
        time.sleep(1)
    if i == tentaiva and check_exists_by_id(element) == False:
        print(msg)
        result = False
    else:
        result = True
    if result == False:
        return False
    elif result == True:
        print('Elemento ' + element + ' encontrado')
        driver.find_element_by_id(element).click()

def wait_and_click_for_element_text_fixed(element,tentaiva,msg):
    i=0
    while check_exists_by_text(element) == False and i < tentaiva:
        i=i+1
        print('Waiting... ' +str(i))
        time.sleep(1)
    if i == tentaiva and check_exists_by_text(element) == False:
        print(msg)
        result = False
    else:
        result = True
    if result == False:
        return False
    elif result == True:
        print('Elemento ' + element + ' encontrado')
        driver.find_element_by_partial_link_text(element).click()

def wait_for_element_id_fixed(element,tentaiva,msg):
    i=0
    while check_exists_by_id(element) == False and i < tentaiva:
        i=i+1
        print('Waiting... ' +str(i))
        time.sleep(1)
    if i == tentaiva and check_exists_by_id(element) == False:
        print(msg)
        return False
    else:
        return True

