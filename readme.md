# Commande de base pour utiliser git

| Catégorie                          | Commande                                                   | Description                                                |
| ---------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| **Configuration**                  | `git config --global user.name "Votre Nom"`                | Configurer le nom d'utilisateur                            |
|                                    | `git config --global user.email "votre.email@example.com"` | Configurer l'adresse email                                 |
| **Création et Clonage**            | `git init`                                                 | Initialiser un nouveau dépôt                               |
|                                    | `git clone url_du_dépôt`                                   | Cloner un dépôt existant                                   |
| **Gestion des Branches**           | `git branch`                                               | Lister toutes les branches                                 |
|                                    | `git branch nom_de_la_branche`                             | Créer une nouvelle branche                                 |
|                                    | `git checkout nom_de_la_branche`                           | Changer de branche                                         |
|                                    | `git merge nom_de_la_branche`                              | Fusionner une branche dans la branche active               |
| **Modifications et Validation**    | `git status`                                               | Vérifier l'état des fichiers                               |
|                                    | `git add .`                                                | Ajouter tous les fichiers modifiés pour le prochain commit |
|                                    | `git commit -m "Message de commit"`                        | Faire un commit                                            |
| **Synchronisation et Mise à Jour** | `git fetch`                                                | Récupérer les dernières modifications sans fusionner       |
|                                    | `git pull`                                                 | Récupérer les dernières modifications et fusionner         |
|                                    | `git push origin nom_de_la_branche`                        | Pousser les modifications vers le dépôt distant            |
| **Annulation de Changements**      | `git checkout -- nom_du_fichier`                           | Annuler les modifications dans un fichier                  |
|                                    | `git reset --hard commit_id`                               | Revenir à un commit précédent                              |
| **Informations et Logs**           | `git log`                                                  | Afficher l'historique des commits                          |
|                                    | `git diff`                                                 | Afficher les différences non commitées                     |
