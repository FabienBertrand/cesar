from encodage import decoder_caesar, encoder_caesar


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

        if not choix == '3':
            clef = int(input('Clef ? \n'))

        submenu(message, clef)


def submenu(message, clef=0):
    print('1. encrypter')
    print('2. decrypter')
    print('3. bruteforce')
    print('q. retour')
    choix = input().lower()

    if choix == '1':
        print(encoder_caesar(message, clef))
        return
    elif choix == '2':
        print(decoder_caesar(message, clef))
        return
    if choix == 'q':
        return
    else:
        submenu()
