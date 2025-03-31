import secrets

secret_key_base = secrets.token_hex(64)
print(secret_key_base)
