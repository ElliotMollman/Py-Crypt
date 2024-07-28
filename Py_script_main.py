from cryptography.fernet import Fernet
import argparse
import base64, hashlib
from colorama import Fore, Back
import Py_script_encryption as e
import Py_script_decryption as d


def show_banner():
    banner = print("""
    _________________________________________________________________________________                                                                                                                                                                                                                                                                                                                                
    8888888b. Y88b   d88P       .d8888b.  8888888b. Y88b   d88P 8888888b. 88888888888 
    888   Y88b Y88b d88P       d88P  Y88b 888   Y88b Y88b d88P  888   Y88b    888     
    888    888  Y88o88P        888    888 888    888  Y88o88P   888    888    888     
    888   d88P   Y888P         888        888   d88P   Y888P    888   d88P    888     
    8888888P"     888          888        8888888P"     888     8888888P"     888     
    888           888          888    888 888 T88b      888     888           888     
    888           888          Y88b  d88P 888  T88b     888     888           888     
    888           888           "Y8888P"  888   T88b    888     888           888
    _________________________________________________________________________________                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    """)                                                                             
                                                                                    

def generate_key(answer):
    if answer == "Y":
        password = input(f"\n{Fore.GREEN}Enter key for encryption: {Fore.WHITE}").encode("utf-8")
        byte_key = hashlib.md5(password).hexdigest().encode("utf-8")
        key_64 = base64.urlsafe_b64encode(byte_key)
        print(f"\n{Fore.GREEN}Your generated key is: {Fore.WHITE}{Back.BLUE}{key_64}{Back.BLACK}")
    elif answer == "N":
        key_64 = Fernet.generate_key()
        print(f"\n{Fore.GREEN}Your generated key is: {Fore.WHITE}{Back.BLUE}{key_64}{Back.BLACK}")
    return key_64


if __name__ == "__main__":
    # set up command line arguments
    parser = argparse.ArgumentParser(prog="Encryption",description=f"{Fore.MAGENTA}Encryption and decryption for files and string messages. When entering strings and keys for processing," 
                                     f" do not incorperate b''.{Fore.WHITE}")
    parser.add_argument("-m", "--message", type=str, metavar="", default=False, help="The string to be encrypted/decrypted.")
    parser.add_argument("-d", "--decrypt", action="store_true", default=False, help="Decryption method.")
    parser.add_argument("-e", "--encrypt", action="store_true", default=False, help="Ecryption method.")
    parser.add_argument("-f", "--file", type=str, metavar="", default=False, help="The FULL path of the file.")
    args = parser.parse_args()
    
    # Print banner
    show_banner()

    if args.encrypt == True:
    # ask user for custom key or randomly generated key
        answer = ""
        while answer != "Y" and answer != "N":
            answer = input(f"\n{Fore.GREEN}Would you like to enter your own key? Y/N:{Fore.WHITE}").upper()
            if answer != "Y" and answer != "N":
                print(f"\n{Fore.GREEN}Please enter Y or N.{Fore.WHITE}")
        # generate key and assign it to fernet instance for encrypting
        key = generate_key(answer)


    # encryption / decryption process
    if args.encrypt == True:
        e.encrypt(args.message, args.file, key)
    elif args.decrypt == True:
        decryption_key = input(f"\n{Fore.GREEN}Enter decryption key(Note: do not incorperate b'' around key): {Fore.WHITE}")
        d.decrypt(args.message, args.file, decryption_key)    
