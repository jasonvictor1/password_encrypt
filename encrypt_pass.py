import base64

# Define a function to encrypt a password using base64 encoding.
def encrypt_pass(password):
    # Convert the password string to bytes. 
    password_bytes = password.encode()
    
    # Encode these bytes using base64 to get an encoded bytes object.
    encode_bytes = base64.b64encode(password_bytes)
    
    # Print the base64 encoded bytes. This is the 'encrypted' password.
    print(encode_bytes)

# Prompt the user to enter their password.
user_pass = input("Enter your password: ")

# Call the encrypt_pass function with the user's password to encrypt it.
encrypt_pass(user_pass)
