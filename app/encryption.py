import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet


load_dotenv()


fernet_key = os.getenv('FERNET_KEY')


fernet = Fernet(fernet_key)

def encrypt_password(password):
    return fernet.encrypt(password.encode())  

def decrypt_password(token):
    return fernet.decrypt(token).decode()  
