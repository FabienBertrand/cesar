# Les modules d'encodage et décodage sont importés
from encodage import decoder_caesar, encoder_caesar, brute_force
from decrypter_fichier_texte import decrypter_fichier_texte
from encrypter_fichier_texte import encrypter_fichier_texte
# Le module suivant est utlisé pour gerer les fichiers
import os
def menu():
    while True:
        #Affiche le Menu
        print("\nBienvenu! veuillez choisir une option pour encrypter ou décrypter du texte selon le chiffrement César\n")
        print("Tapez 1 pour utiliser le programme en mode console")
        print("Tapez 2 pour utiliser le programme sur un fichier texte")
        print("Tapez 'q' pour fermer le programme")
        choix = input("Votre choix : ").lower()

        # Quitte la abouche while et donc le programme s'arrete
        if choix == 'q':
            break

        # Lance la partie du programme qui s'occupe des fichiers
        if choix == '2':
            print('\nTapez 1 pour encrypter un fichier texte')
            print('Tapez 2 pour décrypter un fichier texte')
            choix2 = input("Votre choix : ").lower()

            if choix2 == '1':
                filename = input('\nPrécisez le nom du fichier à encrypter : ')
                clef = input('Choisissez une valeur pour la clef de chiffrement : ')
                whole_path = os.path.join(os.path.abspath(os.path.curdir),filename)
                if os.path.isfile(whole_path):
                    encrypter_fichier_texte(int(clef), whole_path)
                    print("\nLe message encrypté est écrit dans le fichier 'output.txt' \n")
                else:
                    print("\nFichier introuvable. Assurez-vous que l'orthographe du nom du fichier est correcte.\n")
                break

            elif choix2 == '2':
                filename = input('\nPrécisez le nom du fichier à décrypter : ')
                clef = input('Quelle est la valeur de la clef de chiffrement : ')
                whole_path = os.path.join(os.path.abspath(os.path.curdir), filename)
                if os.path.isfile(whole_path):
                    decrypter_fichier_texte(int(clef),whole_path)
                    print("\nLe message décrypté est écrit dans le fichier 'output.txt' \n")
                else:
                    print("\nFichier introuvable. Assurez-vous que l'orthographe du nom du fichier est correcte.\n")
                break
        #Lance la partie du programme qui permet d'utiliser les fonctions directement dans la console
        else:
            message = input('\nEcrivez le message à traiter : ')
            submenu(message)

def submenu(message):
    #Affiche le menu
    print('\nChoisissez une des options suivantes :')
    print('1. encrypter')
    print('2. decrypter')
    print('3. bruteforce')
    print('q. retour')
    choix = input("Votre choix : ").lower()

    #Demande la cle du code et encode/decode
    if choix == '1':
        clef = int(input('\nClef : '))
        print(f'\nLe mot encodé est {encoder_caesar(message, clef)}')
        return
    elif choix == '2':
        clef = int(input('\nClef : '))
        print(f'\nLe mot décodé est {decoder_caesar(message, clef)}')
        return
    #bruteforce en utilisant un mot connu
    elif choix == '3':
        mot_a_retrouver = input('\nMot a retrouver : ')
        res = brute_force(message, mot_a_retrouver)
        print(f'\nLe message était {res[0]} avec une clé de {res[1]}')
        return
    #retour en arriere au menu
    if choix == 'q':
        return
    else:
        submenu(message)