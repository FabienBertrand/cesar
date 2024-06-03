
import string
from unicodedata import normalize

alphabet = string.ascii_lowercase
crypted_array = []  # initialisation du tableau stockant les données cryptés
def encoder_caesar(mot, clef):  # On boucle sur chaque lettre du mot à chiffrer
    mot_encode = ""
    for i in range(len(mot)):
        if mot[i] == ' ':
            mot_encode += ' '
        else:
            rang_lettre_mot = alphabet.find(mot[i])
            rang_lettre_mot_encode = rang_lettre_mot + clef   # Décalage de l'indice de la lettre dans l'alphabet + valeur de la clef
            if rang_lettre_mot_encode > 25:   # gestion des clef supérieur à 26
                rang_lettre_mot_encode -= 26
            mot_encode += alphabet[rang_lettre_mot_encode]
    crypted_array.append(mot_encode)
    return mot_encode

def ecrire_fichier_crypte():
    array = crypted_array
    file_name = 'output.txt'
    with open(file_name, 'w', encoding='utf-8') as file:
        # Parcourir chaque mot de la liste et l'écrire dans le fichier
        for word in array:  # Ecriture de chaque mot du tableau de mot crypté dans un fichier de sortie
            file.write(word + ' ')
    return
def encrypter_fichier_texte(clef,uncrypted_file):

    clef = clef % 26  # Gestion des clefs négatives par l'opération modulo
    word_file = open(uncrypted_file, 'r', encoding='utf8')  # Ouverture en mode lecture
    words = word_file.read()
    word_array = words.split(" ")
    for index in range(len(word_array)): # On boucle sur le tableau de mots pour gérer les caractères accentués
            word_array[index] = normalize('NFD',word_array[index]).encode('ASCII','ignore').decode('utf8').lower()
            encoder_caesar(word_array[index], clef) # On applique la fonction de d'encryption sur chaque mot du fichier texte
    ecrire_fichier_crypte() # On réécrit le message crypté dans un nouveau fichier
    return