from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select  # Importer la classe Select
import time

def test_create_article():
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

    # Naviguer vers la page de création d'article
    driver.get("http://127.0.0.1:8000/create/")

    # Remplir le formulaire de création d'article
    titre_input = wait.until(EC.visibility_of_element_located((By.ID, "titre")))
    couverture_input = wait.until(EC.visibility_of_element_located((By.ID, "couverture")))
    resume_input = wait.until(EC.visibility_of_element_located((By.ID, "resume")))
    categorie_input = wait.until(EC.visibility_of_element_located((By.ID, "categorie_id")))
    tags_input = wait.until(EC.visibility_of_element_located((By.ID, "tags")))

    # Remplir les champs du formulaire
    titre_article = "Titre de l'article"  # Stocker le titre dans une variable pour la vérification
    titre_input.send_keys(titre_article)
    resume_input.send_keys("Résumé de l'article")
    
    # Remplir le champ de contenu (CKEditor)
    try:
        # Basculer vers l'iframe de CKEditor
        iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.cke_wysiwyg_frame")))
        driver.switch_to.frame(iframe)

        # Localiser et remplir le champ de contenu
        contenu_input = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        contenu_input.send_keys("Contenu détaillé de l'article")

        # Revenir au contexte principal
        driver.switch_to.default_content()
    except Exception as e:
        print(f"Erreur lors de la manipulation de CKEditor : {e}")
        driver.quit()
        assert False, "Erreur lors de la manipulation de CKEditor"

    # Sélectionner une catégorie et des tags (Assurez-vous que ces éléments existent dans la base de données)
    select_categorie = Select(categorie_input)  # Utiliser la classe Select
    select_categorie.select_by_value("48")
    select_tags = Select(tags_input)  # Utiliser la classe Select
    select_tags.select_by_value("92")  # Sélectionner le premier tag
    select_tags.select_by_value("93")  # Sélectionner le deuxième tag
    
    # Télécharger une image pour la couverture
    couverture_input.send_keys("D:/PS file/image PS/iphone.jpg")  # Remplacer par le chemin d'une image valide

    # Soumettre le formulaire
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-default")))
    # Faire défiler la page pour rendre le bouton visible
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    
    # Attendre que le bouton soit activé (s'il est désactivé)
    wait.until(lambda driver: not submit_button.get_attribute("disabled"))
    
    # Utiliser JavaScript pour cliquer sur le bouton
    driver.execute_script("arguments[0].click();", submit_button)

    # Attendre que l'article soit créé et que la redirection se produise
    try:
        wait.until(EC.url_changes("http://127.0.0.1:8000/create/"))
        print("Formulaire soumis avec succès.")
    except Exception as e:
        print(f"Échec de la soumission du formulaire : {e}")
        driver.quit()
        assert False, "Échec de la soumission du formulaire"

    # Naviguer vers la page du tableau des articles
    driver.get("http://127.0.0.1:8000/dashboard_blog/")

    # Vérifier que l'article créé apparaît dans le tableau
    try:
        # Attendre que le tableau soit chargé
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".table__row")))

        # Parcourir les lignes du tableau pour trouver l'article
        rows = driver.find_elements(By.CSS_SELECTOR, ".table__row")
        article_trouve = False

        time.sleep(5)

        for row in rows:
            cells = row.find_elements(By.CSS_SELECTOR, ".table__cell")
            if len(cells) > 1 and cells[1].text == titre_article:  # Vérifier le titre dans la deuxième cellule
                print(f"Article trouvé : {cells[1].text}")
                article_trouve = True
                break

        assert article_trouve, f"L'article '{titre_article}' n'a pas été trouvé dans le tableau."
        print("L'article a été trouvé dans le tableau avec succès.")
    except Exception as e:
        print(f"Erreur lors de la vérification de l'article dans le tableau : {e}")
        driver.quit()
        assert False, "Erreur lors de la vérification de l'article dans le tableau"

    driver.quit()