
L'objectif du programme est de permettre à un utilisateur de crypter ou décrypter un message selon le code César. Le texte à crypter/décrypter peut etre lu à partir de la console ou d'un fichier texte. Le programme est aussi être capable de retrouver la clef de chiffrement d'un message codé avec la méthode de 'brute-force'.
Le programme s'utilise en mode console, il suffit d'exécuter le fichier 'main.py' et de suivre les instructions affichées dans la console. Si vous souhaitez chiffrer/déchiffrer un fichier texte, il suffit de l'ajouter dans le dossier du projet et de donner son nom en entrée du programme lorsque cela vous sera demandé. Le résultat de l'encodage ou du décodage sera écrit dans le fichier 'output.txt'. In est nécessaire d'avoir installé sur son environnement les bibliothèques 'unicodedata', 'string' et 'os' pour que le programme s'exécute correctement.

Ce programme est divisé en plusieurs fichiers :
- 'encodage.py' : regroupe les différents fonctions utilisées pour encoder/décoder un message.
- 'menu.py' : est le code de notre console, permettant d'intéragir avec l'utilisateur.
- 'encrypter_fichier_texte.py' et 'decrypter_fichier_texte.py' : permettent de directement encoder et decoder des fichiers complets.
- 'main.py' : est le script principal à partir duquel il faut lancer le programme.
