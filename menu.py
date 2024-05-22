from encodage import decoder_caesar, encoder_caesar

def menu():
    while True:
        print('1. utiliser dans la console')
        print('2. à partir d\'un fichier')
        print('q. quitter')

        if choix == 'q':
            break

        depuis_fichier = input().lower() == '2'




def submenu(depuis_fichier):
    print('1. encrypter')
    print('2. decrypter')
    print('3. bruteforce')
    print('q. retour')
    choix = input().lower()

    if choix == 'q':
        return
    else:
        submenu()

    if depuis_fichier:
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
        clef = input('Clef ? \n')

    if choix == '1':
        print(encoder_caesar(message, clef))
        menu()
    elif choix == '2':
        print(decoder_caesar(message, clef))
        menu()