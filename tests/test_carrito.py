import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_carrito():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        usuario = driver.find_element(By.ID,"user-name")
        contraseña = driver.find_element(By.ID,"password")
        boton_login = driver.find_element(By.ID,"login-button")

        usuario.send_keys("standard_user")
        contraseña.send_keys("secret_sauce")
        boton_login.click()

        time.sleep(3)

    #Validar productos en el carrito = 0
        carrito = driver.find_element(By.CSS_SELECTOR,'[data-test="shopping-cart-link"]')
        assert carrito.get_attribute('aria-label') =="Cart, empty"

    #Agregar al carrito
        boton_add_mochila = driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        boton_add_mochila.click()

    #Validar incremento de prodcutos
        carrito = driver.find_element(By.CSS_SELECTOR,'[data-test="shopping-cart-link"]')
        assert carrito.get_attribute('aria-label') == "Cart, 1 items"

    #Validar interaccion con el carrito
        carrito.click()
        time.sleep(2)

    #Validar titulo
        titulo_carrito = driver.find_element(By.CSS_SELECTOR,'[data-test="title"]')
        assert titulo_carrito.text == "Your Cart"

    #Validar nombre del producto añadido
        nombre_producto = driver.find_element(By.CSS_SELECTOR,'[data-test="inventory-item-name"]')
        assert nombre_producto.text == "Sauce Labs Backpack"


    finally:
        driver.quit()