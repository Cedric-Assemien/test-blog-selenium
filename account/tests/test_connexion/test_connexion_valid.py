from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_connexion_valid():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/sing_in")  # URL de connexion

    wait = WebDriverWait(driver, 20)  # Attendre jusqu'à 10 secondes

    email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password1")))

    email_input.send_keys("cedric@gmail.com")
    password_input.send_keys("cedric")
    password_input.send_keys(Keys.RETURN)

    time.sleep(3)  # Attendre pour voir le résultat
    assert driver.current_url == "http://127.0.0.1:8000/", "connexion impossible"

    driver.quit()

