import string
from unicodedata import normalize

alphabet = string.ascii_lowercase

# Fonction permettant d'encoder un mot à partir d une clef donnée
def encoder_caesar(mot, clef):
    mot_encode = ""
    mot = normalize('NFD', mot).encode('ASCII', 'ignore').decode('utf8').lower()
    clef = clef % 26 # Gestion des clés négatives
    for i in range(len(mot)):
        if mot[i] == ' ':# Permet de garder les espaces
            mot_encode += ' '
        else:
            rang_lettre_mot = alphabet.find(mot[i])
            rang_lettre_mot_encode = rang_lettre_mot + clef
            if rang_lettre_mot_encode > 25:
                rang_lettre_mot_encode -= 26
            mot_encode += alphabet[rang_lettre_mot_encode]
    return mot_encode

#fonction permettant de decoder un mot à partir d une clef donnée (revient au même que la fonction precedente avec une clef négative)
def decoder_caesar(mot_encode, clef):
    mot = ""
    mot_encode = normalize('NFD',mot_encode).encode('ASCII','ignore').decode('utf8').lower()
    clef = clef % 26 # Gestion des clés négatives
    for i in range(len(mot_encode)):
        if mot_encode[i] == ' ':
            mot += ' '
        else:
            rang_lettre_mot_encode = alphabet.find(mot_encode[i])
            rang_lettre_mot = rang_lettre_mot_encode - clef
            if rang_lettre_mot < 0:
                rang_lettre_mot += 26
            mot += alphabet[rang_lettre_mot]
    return mot

#fonction permettant de brut force un message encoder en Caesar a condition de lui donner un mot connu du message à décripter
def brute_force(message, mot_a_trouver): # renvoie le message decode et la clef
    liste_mot = message.split()  # Diviser le contenu, split() par défaut sépare par les espaces
    for i in range(len(liste_mot)):
        for j in range(25):
            if decoder_caesar(liste_mot[i], j) == mot_a_trouver:
                return (decoder_caesar(message,j),j)
    return ('erreur : le mot n est pas dans le message')

