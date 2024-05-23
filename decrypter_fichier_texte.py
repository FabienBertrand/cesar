import os
import string
from unicodedata import normalize

alphabet = string.ascii_lowercase
decrypted_array = []

def decoder_caesar(mot_encode, clef):
    mot = ""
    for i in range(len(mot_encode)):
        if mot_encode[i] == ' ':
            mot += ' '
        else:
            rang_lettre_mot_encode = alphabet.find(mot_encode[i])
            rang_lettre_mot = rang_lettre_mot_encode - clef
            if rang_lettre_mot < 0:
                rang_lettre_mot += 26
            mot += alphabet[rang_lettre_mot]
    decrypted_array.append(mot)
    return decrypted_array


def decrypter_fichiers_textes(clef):
    #crypted_file = input(" Quel est le nom du fichier a décrypter ? ")
    crypted_file = "test_file.txt"
    whole_path = os.path.join(os.path.abspath(os.path.curdir), crypted_file)
    if os.path.isfile(whole_path):
        word_file = open(whole_path, 'r', encoding='utf8')
        words = word_file.read()
        word_array = words.split(" ")
        for index in range(len(word_array)):
                word_array[index] = normalize('NFD',word_array[index]).encode('ASCII','ignore').decode('utf8').lower()
        print(word_array)
        for w in word_array:
            decoder_caesar(w, clef)
        print(decrypted_array)
    ecrire_fichier_decrypte()
    return
def ecrire_fichier_decrypte():
    array = decrypted_array
    file_name = 'fichier_decryte.txt'
    with open(file_name, 'w', encoding='utf-8') as file:
        # Parcourir chaque mot de la liste et l'écrire dans le fichier
        for word in array:
            file.write(word + ' ')
    return

decrypter_fichiers_textes(1)
