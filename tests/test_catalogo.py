import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_validaciones_catalogo():
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
        
    #Validar titulo
        assert driver.title == "Swag Labs"

    #Validar cantidad de productos
        catalogo = driver.find_elements(By.CLASS_NAME,"inventory_item")
        cantidad_lista_catalogo = len(catalogo)
        assert cantidad_lista_catalogo > 0

        nombre_primer_producto = catalogo[0].find_element(By.CLASS_NAME,"inventory_item_name").text
        precio_primer_producto = catalogo[0].find_element(By.CLASS_NAME,"inventory_item_price").text
        
    #validar nombre y precio del primer producto
        assert nombre_primer_producto == "Sauce Labs Backpack"
        assert precio_primer_producto == "$29.99"

    #lista de nombres del primer prodcuto

        lista_nombres = []
        
        for producto in catalogo:
            nombres= producto.find_element(By.CLASS_NAME,"inventory_item_name").text
            lista_nombres.append(nombres)

        nombres_esperados = ["Sauce Labs Backpack","Sauce Labs Bike Light","Sauce Labs Bolt T-Shirt","Sauce Labs Fleece Jacket","Sauce Labs Onesie","Test.allTheThings() T-Shirt (Red)"]
        assert nombres_esperados == lista_nombres

    #verificar elementos visibles

        menu_hamburguesa = driver.find_element(By.ID,"react-burger-menu-btn")
        assert menu_hamburguesa.is_displayed()

        boton_filtro = driver.find_element(By.CSS_SELECTOR,"[data-test='product-sort-container']")
        assert boton_filtro.is_displayed()

    finally:
        driver.quit()