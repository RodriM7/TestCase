import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe", options=options)
driver.get("https://lavandanatural.com/")
time.sleep(2)

icono = driver.find_element(By.ID, "auth")
icono.click()
time.sleep(1)

login = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/div[2]/div[2]/div[1]/div/a[2]")
login.click()
time.sleep(3)

mail = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div/div[4]/form/div[1]/input")
mail.send_keys("rmunoz_probar@yahoo.com")
time.sleep(2)

passw = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div/div[4]/form/div[2]/input")
passw.send_keys("probar123456")
passw.send_keys(Keys.ENTER) # Inicia sesion
time.sleep(2)

categoriaProducto = driver.find_element(By. XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/ul/li[2]/a")
categoriaProducto.click() # Selecciona en el menu de categoria "Productos"
time.sleep(3)

requirement = ()    
labelObtained = ()      

def compareLabels():
    if requirement in labelObtained:
        print("Pass")
    else:
        print("Fail")


#valida que ingrese el producto que seleccionaste
linkProducto = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[6]/div/div[1]/div[1]/div[3]/div/div/div[2]/a")   


labelProducto =  driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[6]/div/div[1]/div[1]/div[3]/div/div/div[2]/a").text

labelObtained = labelProducto

print(labelObtained)

requirement = 'SHAMPOO'

compareLabels()

product = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[6]/div/div[1]/div[1]/div[3]/div/div/div[2]/a")
product.click() # Agrega producto al carro
time.sleep(2)

agregar = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div[1]/div[2]/div/div[2]/div/form/div[4]/div/div/input")
agregar.click() 
time.sleep(4)

requirement = ()    
labelObtained = ()      

def compareLabels():
    if requirement in labelObtained:
        print("Pass")
    else:
        print("Fail")


#valida que ingrese el producto que seleccionaste
linkProductoCarrito = driver.find_element(By.XPATH, "/html/body/div[3]/form/div/div[4]/div/div[2]/div/div[2]/div[1]")   


labelProductoCarrito  =  driver.find_element(By.XPATH, "/html/body/div[3]/form/div/div[4]/div/div[2]/div/div[2]/div[1]/a/span").text


labelObtained =labelProductoCarrito

print(labelObtained)

requirement = 'Shampoo'

compareLabels()

verMas = driver.find_element(By.XPATH, "/html/body/div[3]/form/div/div[4]/div/div[8]/div[2]/a")
verMas.click()
time.sleep(2)

driver.close()
