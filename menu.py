from encodage import decoder_caesar, encoder_caesar, brute_force
from decrypter_fichier_texte import decrypter_fichier_texte
from encrypter_fichier_texte import encrypter_fichier_texte
import os
def menu():
    while True:
        print("\nBienvenu! veuillez choisir une option pour encrypter ou décrypter du texte selon le chiffrement César\n")
        print("Tapez 1 pour utiliser le programme en mode console")
        print("Tapez 2 pour utiliser le programme sur un fichier texte")
        print("Tapez 'q' pour fermer le programme")
        choix = input("Votre choix : ").lower()

        if choix == 'q':
            break

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
        else:
            message = input('Message ? \n')
            submenu(message)

def submenu(message):
    print('1. encrypter')
    print('2. decrypter')
    print('3. bruteforce')
    print('q. retour')
    choix = input().lower()

    if choix == '1':
        clef = int(input('Clef ? \n'))
        print(encoder_caesar(message, clef))
        return
    elif choix == '2':
        clef = int(input('Clef ? \n'))
        print(decoder_caesar(message, clef))
        return
    elif choix == '3':
        mot_a_retrouver = input('Mot a retrouver ? \n')
        res = brute_force(message, mot_a_retrouver)
        print(f'Le message était {res[0]} avec une clé de {res[1]}')
        return
    if choix == 'q':
        return
    else:
        submenu(message)