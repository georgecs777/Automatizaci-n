from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

#Ubicacion del navegador
driver_path = "C:/Users/Cobos/OneDrive/Documentos/chromedriver-win64/chromedriver.exe"
service = Service(driver_path)

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_experimental_option("excludeSwitches", ["enable-automation"])


#ejemplo
EXAMPLE_EMAIL = "correodeprueba@gmail.com"
EXAMPLE_PASSWORD = "1234567"

#abrir navegador
driver = webdriver.Chrome(service=service, options=options)

try:
    print("Iniciando automatización de Facebook")
    
   
    driver.get("https://www.facebook.com")
    print("Página de Facebook cargada")
    
   
    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Permitir todas las cookies')]"))
        )
        cookie_button.click()
        print("✔ Cookies aceptadas")
    except:
        print("✘ No se encontró botón de cookies")
    
 
    print(f"➡ Ingresando email: {EXAMPLE_EMAIL}")
    email_field = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']"))
    )
    email_field.send_keys(EXAMPLE_EMAIL)
    #para que ingrese el ejemplo
    print(f"➡ Ingresando contraseña: {'*'*len(EXAMPLE_PASSWORD)}")
    password_field = driver.find_element(By.CSS_SELECTOR, "input[name='pass']")
    password_field.send_keys(EXAMPLE_PASSWORD)
    
  
    print(" Haciendo clic en el botón de login")
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()
    
    # Verificar resultado
    try:
        WebDriverWait(driver, 15).until(
            EC.or_(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Inicio')]")),
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Contraseña incorrecta')]"))
            )
        )
        
        if "Inicio" in driver.page_source:
            print("Login exitoso - Redirigido a página de inicio")
        else:
            print("Error en el login - Credenciales incorrectas")
    except:
        print("Tiempo de espera agotado - No se pudo verificar el login")
    
    #Tiempo para ver como resulto
    print("Esperando 30 segundos antes de cerrar...")
    time.sleep(30)
    
except Exception as e:
    print(f"Error crítico: {str(e)}")
    
finally:
    driver.quit()
    print("Navegador cerrado correctamente")