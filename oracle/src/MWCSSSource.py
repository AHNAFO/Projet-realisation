import subprocess
import json
from Source import Source

class MCSSSource(Source):
    def __init__(self):
        super().__init__("MWCSS", "tab")
        

    def generateNumberSequence(self, lengthTab):
        # Définir le code JavaScript dans une chaîne
        code_js = "console.log(Array.from(Array({lengthTab}), Math.random));".format(lengthTab=lengthTab)

        # Exécuter le code JavaScript avec Node.js et stocker le résultat dans une variable Python
        resultat = subprocess.check_output(["node", "-e", code_js])

        # Afficher le résultat
        print(resultat.decode().strip())
        self.setNumberSequence(json.loads(resultat.decode().strip()))
