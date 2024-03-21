from mnemonic import Mnemonic
import bip32utils

# Initialize the mnemonic generator
mnemon = Mnemonic('english')

# Example mnemonic (replace with your own)
# mnemonic_words = "aware report movie exile buyer drum poverty supreme gym oppose float elegant"
mnemonic_words = mnemon.generate(256) # Generate a 256-bit mnemonic

# Generate the seed from the mnemonic
seed = mnemon.to_seed(mnemonic_words)

# Generate the BIP32 root key from the seed
root_key = bip32utils.BIP32Key.fromEntropy(seed)

# Derive a child key (e.g., the first account's first address)
# This path follows the BIP44 standard for Bitcoin
child_key = root_key.ChildKey(44 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN).ChildKey(0).ChildKey(0)

# Get the public key and private key in Wallet Import Format (WIF)
private_key_wif = child_key.WalletImportFormat()
public_key = child_key.PublicKey().hex()

print('=> mnemonic_words:', mnemonic_words)
print('=> private key (WIF):', private_key_wif)
print('=> public key:', public_key)

# how to print a friendly address - bitcoin format
# metamax wallet