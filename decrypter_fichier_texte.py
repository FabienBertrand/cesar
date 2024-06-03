
import string
from unicodedata import normalize

alphabet = string.ascii_lowercase
decrypted_array = []            # initialisation du tableau stockant les données décryptés

def decoder_caesar(mot_encode, clef):
    mot = ""
    for i in range(len(mot_encode)):   # On boucle sur chaque lettre du mot à décoder
        if mot_encode[i] == ' ':
            mot += ' '
        else:
            rang_lettre_mot_encode = alphabet.find(mot_encode[i])
            rang_lettre_mot = rang_lettre_mot_encode - clef  # Décalage de l'indice de la lettre dans l'alphabet - valeur de la clef
            if rang_lettre_mot < 0:
                rang_lettre_mot += 26
            mot += alphabet[rang_lettre_mot]
    decrypted_array.append(mot)
    return decrypted_array
def ecrire_fichier_decrypte():
    array = decrypted_array
    file_name = 'output.txt'
    with open(file_name, 'w', encoding='utf-8') as file:
        # Parcourir chaque mot de la liste et l'écrire dans le fichier
        for word in array:      # Ecriture de chaque mot du tableau de mot décrypté dans un fichier de sortie
            file.write(word + ' ')
    return
def decrypter_fichier_texte(clef,crypted_file):
    clef = clef % 26   # Gestion des clefs négatives par l'opération modulo
    word_file = open(crypted_file, 'r', encoding='utf8')  # Ouverture en mode lecture
    words = word_file.read()
    word_array = words.split(" ")
    for index in range(len(word_array)):  # On boucle sur le tableau de mots pour gérer les caractères accentués
            word_array[index] = normalize('NFD',word_array[index]).encode('ASCII','ignore').decode('utf8').lower()
            decoder_caesar(word_array[index], clef) # On applique la fonction de decryption sur chaque mot du fichier texte
    ecrire_fichier_decrypte()  # On réécrit le message dans un nouveau fichier
    return

