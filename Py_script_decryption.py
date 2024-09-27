from cryptography.fernet import Fernet
from colorama import Fore, Back


def decrypt(message, file, decryption_key):
    fernet = Fernet(decryption_key)
    print(f"\n{Fore.YELLOW}Decrypting starting......\n")
    if message != False:
        print(f"{Fore.GREEN}Decrypting message: {Fore.WHITE}{message}\n")
        dec_message = fernet.decrypt(message).decode()
        print(f"{Fore.YELLOW}Encryption completed: {Fore.WHITE}{Back.BLUE}{dec_message}{Back.BLACK}\n")
    elif file != False:
        print(f"{Fore.GREEN}Decrypting file: {Fore.WHITE}{file}\n")
        with open(file, "rb") as original_file:
            file_content = original_file.read()
            original_file.close()
        with open(file, "wb") as decrypted_file:
            decrypted_file_content = fernet.decrypt(file_content)
            decrypted_file.write(decrypted_file_content)
            decrypted_file.close()
            print(f"\n{Fore.YELLOW}Decryption completed.{Fore.WHITE}")