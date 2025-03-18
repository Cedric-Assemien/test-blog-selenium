from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_password_incorrect():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/sing_in")  # Remplace par ton URL réelle

    wait = WebDriverWait(driver, 20)  # Attente max 10 secondes

    email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password1")))

    email_input.send_keys("cedric@gmail.com") 
    password_input.send_keys("p123")
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)  # Attendre le chargement

    try:
        # Vérifier si le message d'erreur est affiché
        error_message = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "alert-danger")))
        assert error_message, "Aucun message d'erreur détecté"

        # Afficher le message d'erreur
        print("Erreur détectée :", error_message[0].text)  # Afficher le texte du message d'erreur

        # Vérifier que le texte d'erreur contient "inclus un" (partie du message attendu pour un email invalide)
        assert "mot de passe incorrecte" in error_message[0].text.lower(), f"Message d'erreur attendu, mais trouvé : {error_message[0].text}"

    except Exception as e:
        print(f"⚠️ Aucune erreur affichée : {str(e)}")
        assert False, "Le message d'erreur ne s'affiche pas ou est incorrect"

    driver.quit()
