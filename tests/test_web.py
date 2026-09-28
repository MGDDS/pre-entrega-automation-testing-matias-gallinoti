from selenium import webdriver
from selenium.webdriver.common.by import By
#By para seleccionar los elementos


import time


"""Arriba las importaciones necesarias"""


def test_login_exitoso():
    driver= webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")


#input( “Presiona una tecla para entrar…”)


    time.sleep(2)
# Introducir pausa para llegar a ver cuando abre y cierra la pagina
 
# Localizar elementos...
    usuario = driver.find_element(By.ID,"user-name")
    password = driver.find_element(By.ID,"password")
    boton_login = driver.find_element(By.ID,"login-button")


#Completar el form…
    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")


# Hacer login...
    boton_login.click()


# Validar el título por clase opc1 o por selector opc2.
    titulo=driver.find_element(By.CLASS_NAME,"app_logo")
   #titulo = driver.find_element(By.CSS_SELECTOR,'[data-test="title"]')    #opc2


# Validar la url despues del login
    assert driver.current_url=="https://www.saucedemo.com/inventory.html"
    assert titulo.text=="Swag Labs" #el nombre de la pestaña
#input(“Presiona cualquier tecla para cerrar”)
# ya no requerido, se cierra solo al ingresar por consola


# Validar general existencia de productos
# 	Localizo los elementos prod de la web para interactuarlos
# 	Arma lista de prods y la valida
    productos=driver.find_elements(By.CLASS_NAME,"inventory_item")
    assert len(productos)>0





# Validar individual existencia del primer producto
    primer_producto=productos[0]
    nombre_producto=primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text
    precio=primer_producto.find_element(
        By.CLASS_NAME, "inventory_item_price"
    ).text
# Mostrar producto a fin ilustrativo
    print(f"Primer producto: {nombre_producto}")
    print(f"Precio: {precio}")


#Validar menu y filtro
    menu=driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed()
    filtro=driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro.is_displayed()


    driver.quit()
