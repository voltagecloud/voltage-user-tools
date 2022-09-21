import base64
from crypto import *
from lndgrpc.client import LNDClient


lnd = LNDClient()

new_password = "my_new_password"
old_password = "my_old_password"

seed_phrase = "enter your seed phrase here"

macaroon = lnd.change_password(current_password=old_password.encode(), new_password=new_password.encode(), stateless_init=True, new_macaroon_root_key=True)



admin_macaroon = macaroon.admin_macaroon
admin_macaroon_b64 = base64.b64encode(admin_macaroon)


encrypted_seed_phrase = encrypt(seed_phrase.encode(), new_password.encode())
encrypted_admin_macaroon = encrypt(admin_macaroon_b64, new_password.encode())