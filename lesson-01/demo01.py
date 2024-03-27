from bitcoin import *

# Generate a new private key
private_key = random_key()

# Generate the public key
public_key = privtopub(private_key)

# Generate the address
address = pubtoaddr(public_key)

# Print the public key, private key, and address
print("=> Private Key:", private_key)
print("=> Public Key:", public_key)
print("=> Address:", address)