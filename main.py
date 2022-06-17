#import libraries
import encryptor as enc
import decryptor as dcr

def main () :
    #Display the menu for options
    print ('\n','-'*28,
            ' '*12, 'MENU\n','-'*28,'\n',
            ' [*]  1.  Encrypt','\n',
            '[*]  2.  Decrypt\n',
            '[*] Press ENTER to Exit\n')
    user_choice = input (' Enter Choice: ')    
    
    while user_choice != "" :
        if user_choice == '1' :
            print ('\n','='*10,'Encryption','='*10,'\n\n')
            user_text = enc.get_user_input()
            cipher_key = enc.get_cipher_key()
            char_coord = enc.get_char_coord(cipher_key, user_text)
            char_shift = enc.get_char_shift(cipher_key, char_coord)
            encypted_char_value = enc.get_cipher_text_value(user_text, char_shift)
            cipher = enc.encrypt(encypted_char_value, char_coord, cipher_key)
            enc.cipher_printer(cipher)
            print ('\nYour Cipher is available in the "ouput.txt file"')
            while True :
                user_print = input('\nDo you want to display the cipher? [Y]/[N]: ')
                if user_print == 'Y' :
                    cipher_as_print = enc.cipher_printer(cipher)
                    print ('\n', cipher_as_print)
                else :
                    break
        elif user_choice == '2' :
            print ('\n','='*10,'Decryption','='*10,'\n\n')
            cipher = dcr.det_cipher_text()
            cipher_key = dcr.det_cipher_key()
            cal_user_text_lng = dcr.det_text_lng(cipher_key, cipher)
            det_char_list = dcr.det_char_list(cipher_key, cipher, cal_user_text_lng)
            cal_char_shift = dcr.det_char_shift(cipher_key)
            plaintext = dcr.decrypt(cipher_key, cal_user_text_lng, det_char_list, cal_char_shift)
            print (plaintext)
            

if __name__ == '__main__' :
    main()

