import base64

def encrypt_pass(password):
    encode_bytes = base64.b64encode(password.encode())
    print(encode_bytes)  # Corrected variable name here

user_pass = input("Enter your password: ")
encrypt_pass(user_pass)

