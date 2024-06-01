from encodage import decoder_caesar, encoder_caesar, brute_force
from decrypter_fichier_texte import decrypter_fichier_texte
from encrypter_fichier_texte import encrypter_fichier_texte

def menu():
    while True:
        print('1. utiliser dans la console')
        print('2. à partir d\'un fichier')
        print('q. quitter')

        choix = input().lower()
        if choix == 'q':
            break

        if choix == '2':
            print('1. Encrypter un fichier texte')
            print('2. Decrypter un fichier texte')
            choix2 = input().lower()
            if choix2 == '1':
                filename = input('Précisez le nom du fichier à encrypter : ')
                clef = input('Choisissez une valeur pour la clés de chiffrement : ')
                encrypter_fichier_texte(int(clef), filename)
                print("Le message encrypté est écrit dans le fichier 'output.txt' \n")
                break

            elif choix2 == '2':
                filename = input('Précisez le nom du fichier à décrypter : ')
                clef = input('Quelle est la valeur de la clés de chiffrement : ')
                decrypter_fichier_texte(int(clef),filename)
                print("Le message décrypté est écrit dans le fichier 'output.txt' \n")
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