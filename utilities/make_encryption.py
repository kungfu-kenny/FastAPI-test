import os
import base64
from pprint import pprint
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from config import EncryptionData, DefaultValues


class Encryption:
    """
    class which is dedicated to encryption or
    decryption values for the database
    ATTENTION: salt and key don't require to
    be regenerated. It is necessary only for
    test or if someone needs to change them
    """
    def __init__(self, salt=EncryptionData.salt):
        self.__kdf = PBKDF2HMAC(algorithm=hashes.SHA512, length=32, salt=salt, iterations=100000,)
        self.__key = base64.urlsafe_b64encode(self.__kdf.derive(EncryptionData.secret_key))
        self.encrypt_way = Fernet(self.__key)

    def encrypt(self, string_to_encrypt:str) -> str:
        """
        Method which is dedicated to a encrypting values
        Input:  string_to_encrypt = string which is going to be encrypted
        Output: we have successfully encrypted our string
        """
        pwd_to_encrypt = string_to_encrypt.encode()
        return self.encrypt_way.encrypt(pwd_to_encrypt).decode()
            
    def decrypt(self, string_to_encrypt:str) -> str:
        """
        Method which is dedicated to a decrypting values
        Input:  string_to_encrypt = string which is required to be decrypted
        Output: we have successfully decrypted our sting
        """
        en = string_to_encrypt.encode()
        pwd_to_decrypt = self.encrypt_way.decrypt(en)
        return pwd_to_decrypt.decode()

    @staticmethod
    def make_string_encoded(value_dict:object, value_check:bool=False) -> str:
        """
        Static method which is dedicated to work with the 
        Input:  value_dict = fastapi object values which would be inserted
        Output: we developed value of the string to work with
        """
        if not value_check:
            return f"event:{value_dict.event}|character_id:{value_dict.character_id}"
        return str(value_dict)

    @staticmethod
    def add_salt() -> str:
        """
        Method which is dedicated to adding salt for the encryption
        proccess to make the string storage more secure
        Input:  None
        Output: we have got salt, which helps us to encrypt the data
        """
        return os.urandom(16)

    @staticmethod
    def generate_key() -> str:
        """
        Method which is dedicated to a generating key for the string
        Input:  None
        Output: we have successfully generated key value for the work
        """
        return Fernet.generate_key()


if __name__ == '__main__':
    k = Encryption().encrypt('Hello World!')
    print(k)
    print(Encryption().decrypt(k))