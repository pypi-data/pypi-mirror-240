import pyotp

def get_totp(key:str):
    return pyotp.TOTP(key).now()