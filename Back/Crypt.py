import base64


def encrypt(password):
    passw = password.encode('UTF-8')
    passw_enc = base64.b64encode(passw)
    return passw_enc


def decrypt(password):
    passw = base64.b64decode(password)
    passw_dec = passw.decode('UTF-8')
    return passw_dec