from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_register_valid():
    driver = webdriver.Chrome()  # Assurez-vous que le chemin de votre chromedriver est correct
    driver.get("http://127.0.0.1:8000/account/register")  # URL de la page d'inscription

    wait = WebDriverWait(driver, 20)  # Attente max de 20 secondes

    # Localiser les champs du formulaire
    name_input = wait.until(EC.visibility_of_element_located((By.ID, "name")))
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    password1_input = wait.until(EC.visibility_of_element_located((By.ID, "password1")))
    password2_input = wait.until(EC.visibility_of_element_located((By.ID, "password2")))

    # Remplir les champs du formulaire avec des données valides
    name_input.send_keys("emmanuel")
    email_input.send_keys("emmanuel@example.com")
    password1_input.send_keys("emmanuel")
    password2_input.send_keys("emmanuel")

    # Soumettre le formulaire
    password2_input.send_keys(Keys.RETURN)

    time.sleep(2)  # Attendre que la page se charge après l'envoi du formulaire

    # Vérifier si l'utilisateur est redirigé vers la page de connexion
    assert "http://127.0.0.1:8000/account/sing_in" in driver.current_url, "Redirection vers la page de connexion échouée"

    # Vérifier que le message d'erreur est vide
    error_message = driver.find_elements(By.CLASS_NAME, "alert-danger")
    assert len(error_message) == 0, f"Un message d'erreur est affiché : {error_message[0].text}"

    driver.quit()
