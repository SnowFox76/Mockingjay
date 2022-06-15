#####################################################################################
#                                                                                   #
#          Welcome to the Nero Encryption, an extension of the Caesar Cipher        #
#                                                                                   #
#####################################################################################

#import libraries
import encryptor as enc

def main () :
    
    print ('\n','-'*28,
            ' '*12, 'MENU\n','-'*28,'\n',
            ' [*]  1.  Encrypt','\n',
            '[*]  2.  Decrypt\n',
            '[*] Press ENTER to Exit\n')
    user_choice = input (' Enter Choice: ')    
    
    while user_choice != "" :
        if user_choice == '1' :
            user_text = enc.get_user_input()
            cipher_key = enc.get_cipher_key()
            char_coord = enc.get_char_coord(cipher_key, user_text)
            char_shift = enc.get_char_shift(cipher_key, char_coord)
            encypted_char_value = enc.get_cipher_text_value(user_text, char_shift)
            cipher = enc.encrypt(encypted_char_value, char_coord, cipher_key)
            enc.cipher_printer(cipher)
            print ('\nYour Cipher is available in the "ouput.txt file"')
        elif user_choice == '2' :
            pass

if __name__ == '__main__' :
    main()

