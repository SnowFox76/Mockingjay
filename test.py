import numpy as np
import pandas as pd
import random

def dubchk(x) :
    dublic = 0
    for elem in x :
        if x.count(elem) > 1 :
            dublic += x.count(elem)
            return dublic
        else :
            return False


#############################################################


cipher_key = input('Key: ')
key_total = 0
for i in cipher_key :    
    key_total += ord(i)
cipher_key = round(key_total*np.pi+3)
user_text = input("Text: ")


lng = len(user_text)
np.random.seed(cipher_key)
cipher_lng_det = np.random.uniform(0.8,1.1,1)
cipher_lng_det = float(cipher_lng_det[0])
cipher_lng = round(lng*cipher_lng_det*np.pi)


np.random.seed(cipher_key) 
char_coord = np.random.permutation(cipher_lng)[:len(user_text)]
char_coord = char_coord.tolist()


np.random.seed(cipher_key)
char_shift = np.random.randint(15000)


np.random.seed(cipher_key)
step = np.random.randint(len(user_text)*(1+np.sqrt(5))/2)
loop_count = 0
encrypted_char_value = []
for char in user_text :
    loop_count += step
    if loop_count > 40000 :
        loop_count = 1
    encrypted_char_value.append(ord(char)+char_shift+loop_count)


np.random.seed(cipher_key)
cipher = np.random.permutation(65536)[:cipher_lng]
#cipher = np.random.randint(65535, size=cipher_lng)
cipher = cipher.tolist()
for pos in char_coord :
    cipher[pos] = encrypted_char_value[char_coord.index(pos)]
print ('\ncipher length: {}'.format(len(cipher)))
print ('user_text_length: {}\n'.format(len(user_text)))
print ('\n',cipher)


#############################################################


np.random.seed(cipher_key)
cipher_lng_det = np.random.uniform(0.8,1.1,1)
cipher_lng_det = float(cipher_lng_det[0])
cal_user_text_lng = round(len(cipher)/cipher_lng_det/np.pi)
np.random.seed(cipher_key)
cal_char_coord = np.random.permutation(cipher_lng)[:cal_user_text_lng]
cal_char_coord = cal_char_coord.tolist()


chr_val_list = []
chr_list = []


for pos in cal_char_coord :
    chr_val_list.append(cipher[pos])
print ('\nchr_val_list derived from the pos in the cipher: \n',chr_val_list)


np.random.seed(cipher_key)
cal_char_shift = np.random.randint(15000)


np.random.seed(cipher_key)
step = np.random.randint(cal_user_text_lng*(1+np.sqrt(5))/2)
loop_count = 0
for val in chr_val_list :
    loop_count += step
    if loop_count > 40000 :
        loop_count = 1
    chr_list.append(chr(val-cal_char_shift-loop_count))
for char in chr_list :
    print (char, end="",)

##############################################################

print ()
if dubchk(cipher) :
    print ('Duplicates')
else :
    print ('No Duplicates')


"""try:
    while True:
        number_array.remove('dtype=int64')

except ValueError:
    pass
"""


"""
print('Checking file integrity...', end='')
# (...)
print('ok')
"""