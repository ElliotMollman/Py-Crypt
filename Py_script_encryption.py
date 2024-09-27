from cryptography.fernet import Fernet
from colorama import Fore, Back


def encrypt(message, file, key):
    fernet = Fernet(key)
    print(f"{Fore.YELLOW}Encrypting starting......\n{Fore.WHITE}")
    if message != False:
        print(f"{Fore.GREEN}Encrypting message: {Fore.WHITE}{message}\n")
        encoded_message = fernet.encrypt(message.encode("utf-8"))
        print(f"{Fore.YELLOW}Encryption completed: {Fore.WHITE}{Back.BLUE}{encoded_message}{Back.BLACK}\n")
    elif file != False:
        print(f"{Fore.GREEN}Encrypting file: {Fore.WHITE}{file}\n")
        with open(file, "rb") as original_file:
            file_content = original_file.read()
            original_file.close()
        with open(file, "wb") as encrypted_file:
            encrypted_file_content = fernet.encrypt(file_content)
            encrypted_file.write(encrypted_file_content)
            encrypted_file.close()
            print(f"\n{Fore.YELLOW}Encryption completed.{Fore.WHITE}\n")