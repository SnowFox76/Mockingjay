#import libraries
import numpy as np
import pandas as pd
import random, hashlib

def det_cipher_text() :
    """
    Calls the text that should be deciphered, either from the user's input, or reading the text file
    """
    print('Where is the cipher located?\n',
            '[*]  1.  The cipher is in the Text file "output.txt"\n',
            '[*}  2.  Clipboard (Copied it)\n'
            '[*]  Press ENTER to return to Main Menu\n')
    user_choice = input('Enter Choice: ')
    while user_choice != "" :
        if user_choice == '1' :
            f = open('output.txt', 'r')
            for i in f :
                pass
            f.close()
        elif user_choice == '2' :
            cipher = input( 'Enter the Cipher: ')
            return cipher
        else :
            print ('Invalid Input, Please try again.')

def det_cipher_key() :
    """
    Asks user to enter the key for the cipher
    """
    cipher_key = input('Enter Key: ')
    #encode the string input to for hashing
    cipher_key = cipher_key.encode()
    #hash the input string with SHA-3-256 hashing algorythm
    cipher_key256 = hashlib.sha3_256(cipher_key).hexdigest()
    #Use the hash to seed a numerical value usable by Numpy for seeding (0, 4294967296-1)
    random.seed(cipher_key256)
    cipher_key = random.randint(0,4294967295)
    return cipher_key

def det_text_lng (cipher_key, cipher) :
    """
    Determines the lenth of the original messege based on the cipher lenth
    """
    #Seed the random generator with cipher key
    np.random.seed(cipher_key)
    #Determine the factor of which the cipher lenth was created
    cipher_lng_det = np.random.uniform(0.8,1.5,1)
    cipher_lng_det = float(cipher_lng_det[0])
    #use the factor, and the lenth of the cipher to determine the lenth
    #of the messege in the cipher
    cal_user_text_lng = round(len(cipher)/cipher_lng_det/np.pi)
    return cal_user_text_lng

def det_char_list(cipher_key, cipher, cal_user_text_lng) :
    """
    Determine the characters that are part of the 'hidden' messege
    """
    np.random.seed(cipher_key)
    #Determines the place within the cipher the messege is located
    cal_char_coord = np.random.permutation(len(cipher))[:cal_user_text_lng]
    #Converts the numpy array to a list
    cal_char_coord = cal_char_coord.tolist()
    det_char_list = []
    #Calls the specific characters that are the hidden messege from the cipher
    for pos in cal_char_coord :
        det_char_list.append(cipher[pos])
    return det_char_list

def det_char_shift (cipher_key) :
    """
    Determines the amount the characters have been shifted in the cipher
    """
    np.random.seed(cipher_key)
    #Calculate the amount each character has shifted
    cal_char_shift = np.random.randint(15000)
    return cal_char_shift

def decrypt (cipher_key, cal_user_text_lng, det_char_list, cal_char_shift) :
    """
    Decrypt the cipher and returns the original messege
    """
    np.random.seed(cipher_key)
    #Calculate the step used in the encryption
    step = np.random.randint(cal_user_text_lng*(1+np.sqrt(5))/2)
    char_list = []
    loop_count = 0
    for val in det_char_list :
        loop_count += step
        if loop_count > 40000 :
            loop_count = 1
        #The final value of the character is derived from the reverse
        #calculation of the encryption method. 
        char_list.append(chr(val-cal_char_shift-loop_count))
    #converts the list to a string
    plaintext = ' '.join(char_list)
    return plaintext