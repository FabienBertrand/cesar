import string

alphabet = string.ascii_lowercase

def encoder_caesar(mot, clef):
    mot_encode = ""
    for i in range(len(mot)):
        rang_lettre_mot = alphabet.find(mot[i])
        rang_lettre_mot_encode = rang_lettre_mot + clef
        if rang_lettre_mot_encode > 25:
            rang_lettre_mot_encode -= 26
        mot_encode += alphabet[rang_lettre_mot_encode]
    return mot_encode


def decoder_caesar(mot_encode, clef):
    mot = ""
    for i in range(len(mot_encode)):
        rang_lettre_mot_encode = alphabet.find(mot_encode[i])
        rang_lettre_mot = rang_lettre_mot_encode - clef
        if rang_lettre_mot < 0:
            rang_lettre_mot += 26
        mot += alphabet[rang_lettre_mot]
    return mot
