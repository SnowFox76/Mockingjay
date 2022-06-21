import numpy as np
import pandas as pd
import random, hashlib

#class encryptor :
   # """
  #  Takes user text as input, along with a cipher key and encrypts the text using the key
  #  """

def get_user_input() :
    """
    Takes the input of the user that will be encrypted
    """
    user_text = input(" Enter text: ")
    return user_text

def get_cipher_key() :
    """
    This key is used as the seed for random character 
    generation throughout the encryption.
    """
    cipher_key = input (" Enter Key:  ")
    #encode the string input to for hashing
    cipher_key = cipher_key.encode()
    #hash the input string with SHA-3-256 hashing algorythm
    cipher_key256 = hashlib.sha3_256(cipher_key).hexdigest()
    #Use the hash to seed a numerical value usable by Numpy for seeding (0, 4294967296-1)
    random.seed(cipher_key256)
    cipher_key = random.randint(0,4294967295)
    return cipher_key

def get_cipher_lng (user_text, cipher_key) :
    """
    Generates the lenth of the cipher based on the lenth
    of the user's text. 
    """
    #Seed the random generation with the cipher key
    np.random.seed(cipher_key)
    #Generate a random float between 0.8 and 1.5
    cipher_lng_det = np.random.uniform(0.8,1.5,1)
    cipher_lng_det = float(cipher_lng_det[0])
    #Use the random float as a determiner for the cipher lenth
    cipher_lng = round(len(user_text)*cipher_lng_det*np.pi)
    return cipher_lng

def get_char_coord(cipher_key, user_text, cipher_lng) :
    """
    Generate the coordinates the user text 
    will be placed within the cipher.
    """
    #Seed the random generation
    np.random.seed(cipher_key) 
    #Generate a seeded random array the 
    # lenght of the text the user wants to encrypt
    char_coord = np.random.permutation(cipher_lng)[:len(user_text)]
    #Converts the numpy array to a list
    char_coord = char_coord.tolist()
    return char_coord

def get_char_shift(cipher_key) :
    """
    The key is used to build the foundation for the encryption
    """
    np.random.seed(cipher_key)
    #Determining the character shift based on a seeded random number within the coordinates list
    char_shift = np.random.randint(15000)
    return char_shift

def get_cipher_text_value(user_text, char_shift, cipher_key) :
    """
    Shifts the user text to the encrypted numerals and or characters.
    """
    np.random.seed(cipher_key)
    #The step will be added to each character's numeric value, to inclease the
    #randomness of the values for each character. 
    step = np.random.randint(len(user_text)*(1+np.sqrt(5))/2)
    #Loop count is added to the step value to give each character an unique value
    loop_count = 0
    encrypted_char_value = []
    for char in user_text :
        loop_count += step
        #Ensures the charcter value does not exceed 65530
        if loop_count > 40000 :
            loop_count = 1
        #Append the character value, the shift value, and the loop count to the list. 
        encrypted_char_value.append(ord(char)+char_shift+loop_count)
    #Coverts the now determend numeric value back to unicode characters
    encrypted_text = []
    for num in encrypted_char_value :
        encrypted_text.append(chr(int(num)))
    #Change the next line if the desired output should be unicode characters
    return encrypted_char_value

def encrypt(encrypted_char, char_coord, cipher_key, cipher_lng):
    """
    Places the encrypted text of the user into the cipher list.s
    """
    np.random.seed(cipher_key)
    #Generate an the entire random non-repetitive array of numericals
    #the lenght based on the previously determined cipher lenth. 
    cipher = np.random.permutation(55000)[:cipher_lng]  
    cipher = cipher.tolist() #convert the numpy array to a list
    #Replace the specific positions in character coordinates with the encrypted text values.
    for pos in char_coord :
        cipher[pos] = encrypted_char[char_coord.index(pos)]
    #convert the list into a string
    cipher = ' '.join(str(i) for i in cipher)
    return cipher

def cipher_printer(cipher) :
    """
    Outputs the cipher
    """
    #create column names for the dataframe
    columns = []
    for i in range(10) :
        columns.append(i)
    #splits the long list into smaller lists to make it print ready. 
    rows = np.array_split(cipher, 374)
    #adds these rows to a dataframe
    df = pd.DataFrame(rows, columns=columns)
    #converts the dataframe to a string
    df_as_string = df.to_string(header=False, index=False)
    #open, write, and close the text file where the dataframe will be printed to. 
    f = open('output.txt', 'w')
    f.write(df_as_string)
    f.close()
    return df_as_string