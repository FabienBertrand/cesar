import os
def decrypter_fichiers_textes(clef):

    #crypted_file = input(" Quel est le nom du fichier a décrypter ? ")
    crypted_file = "test_file.txt"
    whole_path = os.path.join(os.path.abspath(os.path.curdir), crypted_file)
    if os.path.isfile(whole_path):
        word_file = open(whole_path,'r', encoding='utf8')
        words = word_file.read()
        word_array = words.split(" ")
        print(word_array)
        #word = normalize('NFD',word).encode('ASCII','ignore').decode('utf8')
    return

decrypter_fichiers_textes(3)