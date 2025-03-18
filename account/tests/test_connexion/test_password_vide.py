from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver

def test_password_empty():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/sing_in")  # Remplace par ton URL réelle

    wait = WebDriverWait(driver, 20)  # Attente max 20 secondes

    # Trouver les champs du formulaire
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password1")))

    # Remplir l'email vide et un mot de passe valide
    email_input.send_keys("cedric@gmail.com")  # Email vide pour tester le champ requis
    password_input.send_keys("")
    password_input.send_keys(Keys.RETURN)

    time.sleep(2)  # Attendre le chargement de la page et des erreurs

    try:
        # Vérifier si le message d'erreur est affiché directement sur le champ email
        error_message = password_input.get_attribute("validationMessage")  # Get the validation message for the input
        assert error_message, "Aucun message d'erreur détecté sur le champ email"
        
        # Afficher le message d'erreur pour vérification
        print("Erreur détectée :", error_message)  # Afficher le texte du message d'erreur

        # Vérifier que le texte d'erreur correspond à un champ requis
        assert "renseigner" in error_message.lower(), f"Message d'erreur attendu, mais trouvé : {error_message}"

    except Exception as e:
        print(f"⚠️ Aucune erreur affichée : {str(e)}")
        assert False, "Le message d'erreur ne s'affiche pas ou est incorrect"

    driver.quit()
