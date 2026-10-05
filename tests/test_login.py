import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_exitoso():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        usuario = driver.find_element(By.ID,"user-name")
        contraseña = driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")

    #ingreso de datos para login
        usuario.send_keys("standard_user")
        contraseña.send_keys("secret_sauce")
        boton_login.click()

        time.sleep(3)
    #valida url actual
        assert '/inventory.html' in driver.current_url

        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        logo = driver.find_element(By.CLASS_NAME,"app_logo")

    #valida titulos 
        assert logo.text == "Swag Labs"
        assert titulo.text == "Products"

    finally:
        driver.quit()