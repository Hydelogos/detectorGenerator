# Generateur de detecteurs d'objets
## Pour DLIB

Installation des dependances:
```
pip install --user pipenv
pipenv install
```
(Necessite un compilateur C++ d'installé sur la machine, comme CMake)

Il faudra placer les images necessaires à l'entrainement dans le dossier *img* du projet, chaque image devant contenir l'objet à détecter.
Si un test de la réussite du programme est souhaité il faudra placer de nouvelles images contenant l'objet à détecter dans le dossier *testImg* .

Pour lancer le programme:

```
pipenv run python main.py nomDuDetecteur
```
Un parametre (apparaissant sous le mot *nomDuDetecteur*) est obligatoire pour donner un nom au detecteur qui sera sauvegardé.

### Les etapes du programme

1. Avant la phase d'entrainement chaque image servant à ce dernier apparaitra alors et il faudra sélectionner l'endroit où se trouver l'objet à détecter puis appuyer sur la touche Entrée.

2. Une fois que chaque image sera passée, le programme entrainera le detecteur.

3. Si des images pour tester le fonctionnement du programme ont été données alors chaque image s'affichera avec l'objet encadré si celui-ci est detecté.

4. Un fichier ayant pour nom celui donné au lancement du programme sera alors créé dans le dossier *detector* et pourra être utilisé dans un autre programme usant de dlib pour la detection d'objets.
