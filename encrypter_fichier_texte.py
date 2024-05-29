import os
import string
from unicodedata import normalize

alphabet = string.ascii_lowercase
crypted_array = []
def encoder_caesar(mot, clef):
    mot_encode = ""
    for i in range(len(mot)):
        if mot[i] == ' ':
            mot_encode += ' '
        else:
            rang_lettre_mot = alphabet.find(mot[i])
            rang_lettre_mot_encode = rang_lettre_mot + clef
            if rang_lettre_mot_encode > 25:
                rang_lettre_mot_encode -= 26
            mot_encode += alphabet[rang_lettre_mot_encode]
    crypted_array.append(mot_encode)
    return mot_encode

def ecrire_fichier_crypte():
    array = crypted_array
    file_name = 'output.txt'
    with open(file_name, 'w', encoding='utf-8') as file:
        # Parcourir chaque mot de la liste et l'écrire dans le fichier
        for word in array:
            file.write(word + ' ')
    return
def encrypter_fichier_texte(clef):
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
            encoder_caesar(w, clef)
        print(crypted_array)
    ecrire_fichier_crypte()
    return

encrypter_fichier_texte(1)