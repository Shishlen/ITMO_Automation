# 1. Создайте функцию которая
# a. переходит на страницу https://www.saucedemo.com/
# b. находит элементы:
# i. текстовое поле username
# ii. текстовое поле password
# iii. кнопку submit


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ok.ru/")

username = driver.find_element(By.CSS_SELECTOR, '#field_email')
password = driver.find_element(By.CSS_SELECTOR, '#field_password')
submit = driver.find_element(By.XPATH, '//button[contains(text(), "Войти")]' )

if username and password and submit:
    print("Элементы найдены")
else:
    print("Не все элементы найдены")