from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_email_invalide():
    driver = webdriver.Chrome()  # Assurez-vous que le chemin de votre chromedriver est correct
    driver.get("http://127.0.0.1:8000/account/register")  # URL de la page d'inscription

    wait = WebDriverWait(driver, 20)  # Attente max de 20 secondes

    # Localiser les champs du formulaire
    name_input = wait.until(EC.visibility_of_element_located((By.ID, "name")))
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    password1_input = wait.until(EC.visibility_of_element_located((By.ID, "password1")))
    password2_input = wait.until(EC.visibility_of_element_located((By.ID, "password2")))

    # Remplir les champs avec des données invalides (email invalide)
    name_input.send_keys("peter karter")
    email_input.send_keys("invalidemail.com")  # Email invalide
    password1_input.send_keys("Password123")
    password2_input.send_keys("Password123")

    # Soumettre le formulaire
    password2_input.send_keys(Keys.RETURN)

    print("HTML de la page :", driver.page_source)

   

    driver.quit()
