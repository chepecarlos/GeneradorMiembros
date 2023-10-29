import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ruta del acceso directo de Chrome
chrome_path = '/opt/google/chrome/google-chrome'

# Parámetros adicionales para el acceso directo
chrome_args = [
    "--profile-directory=Profile 1",
    "--app-id=iioankkojbognoennimnepkkamkfdemh"
]

# Abrir Chrome con el acceso directo
subprocess.Popen([chrome_path] + chrome_args)

# Esperar unos segundos para que Chrome se abra completamente
time.sleep(5)

# Inicializar el controlador de Chrome
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service)

# Navegar a la página web
driver.get("https://studio.youtube.com/channel/UCS5yb75qx5GFOG-uV5JLYlQ/monetization/memberships")

# Esperar un segundo para asegurarse de que la página se haya cargado completamente
time.sleep(1)

# Esperar hasta que el elemento esté presente en la página
wait = WebDriverWait(driver, 10)
ver_miembros_button = wait.until(EC.presence_of_element_located((By.ID, "open-button")))

# Hacer clic en el botón
ver_miembros_button.click()

# Esperar 2 minutos
time.sleep(120)

# Hacer clic en el segundo botón
remove_defaults_button = driver.find_element(By.CSS_SELECTOR, "tp-yt-iron-icon.remove-defaults.style-scope.ytcp-icon-button")
ActionChains(driver).move_to_element(remove_defaults_button).click().perform()

# Esperar 2 minutos
time.sleep(120)

# Hacer clic en el último botón
descargar_button = driver.find_element(By.CSS_SELECTOR, "div.label.style-scope.ytcp-button")
descargar_button.click()

# Cerrar el navegador
driver.quit()
