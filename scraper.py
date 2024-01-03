import requests
from bs4 import BeautifulSoup
import time
webhook_url = "https://discord.com/api/webhooks/"
langue = input("Select the lang french/english\n")
if langue == "french":
    adresse = input("Entrez l'adresse du site web à scraper:\n")
elif langue == "english":
    adresse = input("Enter the address of the website to scrape:\n")
try:
    reponse = requests.get(adresse)
    reponse.raise_for_status()
except:
    if langue == "french":
        print("Une erreur s'est produite, veuillez entrer une adresse valide.")
    elif langue == "english":
        print("An error occurred, please enter a valid address.")
    else:
        print("Langue non reconnue.")
    exit()
soup = BeautifulSoup(reponse.content, "html.parser")
titre = soup.title.string
with open(titre + ".html", "w", encoding="utf-8") as fichier:
    fichier.write(soup.prettify())
requests.post(webhook_url, files={"file": (titre + ".html", open(titre + ".html", "rb"), "text/html")})
if langue == "french":
    print("Le script a réussi, le fichier HTML a été envoyé au webhook discord.")
elif langue == "english":
    print("The script succeeded, the HTML file was sent to the discord webhook.")
else:
    print("Langue non reconnue.")
