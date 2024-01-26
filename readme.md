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

# Questions / Réponses

## 1. Qu’est-ce qu’un dépôt (repository) ?

Un dépôt, dans le contexte de Git, est une collection de fichiers de votre projet et de l'historique de toutes les modifications qui ont été faites à ces fichiers. C'est comme une base de données pour votre code, permettant de garder une trace des changements et de collaborer avec d'autres. Un dépôt peut exister sur votre ordinateur (dépôt local) et/ou sur un serveur distant (dépôt distant), comme GitHub ou GitLab.

## 2. Comment créer un dépôt ?

**Pour créer un dépôt local avec Git, vous devez suivre ces étapes :**

Ouvrez un terminal sur votre ordinateur.
Naviguez jusqu'au dossier où vous souhaitez créer le dépôt.
Exécutez la commande git init. Cette commande crée un nouveau sous-dossier nommé .git qui contient tous les fichiers nécessaires au fonctionnement de Git, initialisant ainsi un dépôt vide.
Pour créer un dépôt distant, vous devrez généralement utiliser une plateforme comme GitHub, GitLab ou Bitbucket, où vous pouvez créer un nouveau dépôt via leur interface graphique.

## 3. Qu’est-ce qu’un commit ?

Un commit dans Git est comme une "instantané" de votre projet à un moment donné. Quand vous faites un commit, Git enregistre l'état actuel de votre projet et toutes les modifications que vous avez apportées depuis le dernier commit. Chaque commit est identifié par un identifiant unique (SHA-1 hash) et contient des informations telles que l'auteur du commit, la date et un message décrivant les modifications. Les commits permettent de suivre l'historique des modifications et de revenir à une version antérieure du projet si nécessaire.

## 4. Qu’est-ce qu’une branche ?

Une branche dans Git est essentiellement une ligne de développement indépendante. Lorsque vous créez une branche, vous faites une copie du code tel qu'il existe sur la branche actuelle (par exemple la branche principale, souvent appelée master ou main). Cela vous permet de travailler sur des fonctionnalités, des corrections ou des expérimentations sans affecter la branche principale. Les branches sont un moyen puissant de gérer les modifications et de collaborer avec d'autres développeurs, car elles permettent de séparer les différents travaux avant de les fusionner dans la branche principale une fois terminés.
