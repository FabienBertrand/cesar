from encodage import decoder_caesar, encoder_caesar, brute_force


def menu():
    while True:
        print('1. utiliser dans la console')
        print('2. à partir d\'un fichier')
        print('q. quitter')

        choix = input().lower()
        if choix == 'q':
            break

        if choix == '2':
            filename = input('filename ? \n')
            try:
                f = open(filename, 'r')
            except FileNotFoundError:
                print('Fichier introuvable')
                return
            else:
                with f:
                    message = f.read()
        else:
            message = input('Message ? \n')

        submenu(message)


def submenu(message, clef=0):
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
        submenu()
