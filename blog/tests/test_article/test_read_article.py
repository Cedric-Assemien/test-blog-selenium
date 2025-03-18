from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
# Importer la classe Select



def test_consulter_article():
    driver = webdriver.Chrome()  # Assurez-vous que le chemin du chromedriver est correct
    driver.get("http://127.0.0.1:8000/account/sing_in")  # Remplacez par l'URL de votre page de connexion

    wait = WebDriverWait(driver, 20)

    # Connexion avec un utilisateur valide
    email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password1")))

    email_input.send_keys("cedric@gmail.com")  # Remplacez par un email valide
    password_input.send_keys("cedric")  # Remplacez par un mot de passe valide
    password_input.send_keys(Keys.RETURN)

    # Vérifier si la connexion a réussi
    try:
        wait.until(EC.url_to_be("http://127.0.0.1:8000/"))  # Attendre la redirection vers la page d'accueil
        print("Connexion réussie.")
    except Exception as e:
        print(f"Échec de la connexion : {e}")
        driver.quit()
        assert False, "La connexion a échoué"

   
    driver.get("http://127.0.0.1:8000/dashboard_blog/")

    # Attendre que le tableau soit chargé
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".table__row")))

    # Parcourir les lignes du tableau pour trouver l'article
    rows = driver.find_elements(By.CSS_SELECTOR, ".table__row")
    article_trouve = False

    for row in rows:
        cells = row.find_elements(By.CSS_SELECTOR, ".table__cell")
        if len(cells) > 1 and cells[1].text == "Article numero 1":  # Vérifier le titre dans la deuxième cellule
            print(f"Article trouvé : {cells[1].text}")
            article_trouve = True
            break

    assert article_trouve, f"L'article 'Article numero 1' n'a pas été trouvé dans le tableau."

  

    driver.quit()