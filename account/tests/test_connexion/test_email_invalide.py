from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_email_invalide():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/sing_in")

    wait = WebDriverWait(driver, 20)  # Augmentation du temps d'attente

    email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password1")))

    email_input.send_keys("emailinvalide.com")  # Email invalide
    password_input.send_keys("cedric")  # Mot de passe
    password_input.send_keys(Keys.RETURN)  # Soumission
    
    time.sleep(2)  # Attendre le chargement
    password_input.send_keys(Keys.RETURN)

    print("HTML de la page :", driver.page_source)
  

    driver.quit()
