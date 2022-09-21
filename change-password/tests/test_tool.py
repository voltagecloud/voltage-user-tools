from crypto import *

secret_passphrase = "test1234".encode()
secret_string = "blah".encode()
encrypted_string = encrypt(secret_string, secret_passphrase)

decrypted_string = decrypt(encrypted_string, secret_passphrase)

print(f"Is successful? {secret_string == decrypted_string}")
