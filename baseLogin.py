import time
from selenium.webdriver.common.by import By
from PageObject.locator import elem
from PageObject.locator import link
from PageObject.data import inputan

def positive_login(driver):
    driver.get(link.baseUrl) #buka situs
    time.sleep(1)
    driver.maximize_window()
    driver.find_element(By.ID, elem.username).send_keys(inputan.username) #isi email
    time.sleep(1)
    driver.find_element(By.ID, elem.password).send_keys(inputan.password) #isi password
    time.sleep(1)
    driver.find_element(By.ID, elem.loginButton).click()
    time.sleep(3)

def negative_login_wrong_usn(driver):
    driver.get(link.baseUrl) #buka situs
    time.sleep(1)
    driver.maximize_window()
    driver.find_element(By.ID, elem.username).send_keys(inputan.wrongUsername) #isi email
    time.sleep(1)
    driver.find_element(By.ID, elem.password).send_keys(inputan.password) #isi password salah
    time.sleep(1)
    driver.find_element(By.ID, elem.loginButton).click()
    time.sleep(3)

def negative_login_wrong_pw(driver):
    driver.get(link.baseUrl) #buka situs
    time.sleep(1)
    driver.maximize_window()
    driver.find_element(By.ID, elem.username).send_keys(inputan.username) #isi email
    time.sleep(1)
    driver.find_element(By.ID, elem.password).send_keys(inputan.wrongPassword) #isi password salah
    time.sleep(1)
    driver.find_element(By.ID, elem.loginButton).click()
    time.sleep(3)

def negative_login_blank_usn(driver):
    driver.get(link.baseUrl) #buka situs
    time.sleep(1)
    driver.maximize_window()
    driver.find_element(By.ID, elem.username).send_keys("") #isi email
    time.sleep(1)
    driver.find_element(By.ID, elem.password).send_keys(inputan.password) #isi password salah
    time.sleep(1)
    driver.find_element(By.ID, elem.loginButton).click()
    time.sleep(3)

def negative_login_blank_pw(driver):
    driver.get(link.baseUrl) #buka situs
    time.sleep(1)
    driver.maximize_window()
    driver.find_element(By.ID, elem.username).send_keys(inputan.username) #isi email
    time.sleep(1)
    driver.find_element(By.ID, elem.password).send_keys("") #isi password salah
    time.sleep(1)
    driver.find_element(By.ID, elem.loginButton).click()
    time.sleep(3)

def negative_login_blank_all(driver):
    driver.get(link.baseUrl) #buka situs
    time.sleep(1)
    driver.maximize_window()
    driver.find_element(By.ID, elem.username).send_keys("") #isi email
    time.sleep(1)
    driver.find_element(By.ID, elem.password).send_keys("") #isi password salah
    time.sleep(1)
    driver.find_element(By.ID, elem.loginButton).click()
    time.sleep(3)

