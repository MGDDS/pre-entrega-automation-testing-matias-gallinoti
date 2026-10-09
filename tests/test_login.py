import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
#By para seleccionar los elementos


# import time para deprecado uso de  time.sleep(2) reemplazado x wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Arriba las importaciones necesarias"""

def test_login_exitoso():
    driver= webdriver.Chrome()
    
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://www.saucedemo.com/")
#Input( “Presiona una tecla para entrar…” usualmente no requerido, se cierra solo al ingresar por consola)
  
# Introducir pausa para llegar a ver cuando abre y cierra la pagina
 
# Localizar elementos...
        usuario = wait.until(EC.presence_of_element_located((By.ID,"user-name")))
        #driver.find_element(By.ID,"user-name")
        password = wait.until(EC.presence_of_element_located((By.ID,"password")))
        #driver.find_element(By.ID,"password")
        boton_login = wait.until(EC.element_to_be_clickable((By.ID,"login-button")))
        # driver.find_element(By.ID,"login-button")

#Completar el form…
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")


# Hacer login...
        boton_login.click()

        assert "/inventory.html" in driver.current_url


# Validar texto por clase opc1 o por selector opc2.
   #titulo=driver.find_element(By.CLASS_NAME,"app_logo")
   #titulo = driver.find_element(By.CSS_SELECTOR,'[data-test="title"]')    #opc2
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"

# Validar titulo y la url despues del login
        assert driver.current_url=="https://www.saucedemo.com/inventory.html"
#        assert titulo.text=="Swag Labs" el nombre de la pestaña
#input(“Presiona cualquier tecla para cerrar”)
# ya no requerido, se cierra solo al ingresar por consola
        titulo = driver.find_element(By.CSS_SELECTOR,"[data-test='title']")
        assert titulo.text == "Products"
    
    finally:
        driver.quit()