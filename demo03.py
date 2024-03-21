from mnemonic import Mnemonic
import bip32utils

# Initialize the mnemonic generator
mnemon = Mnemonic('english')
# Generate a 256-bit mnemonic
mnemonic_words = mnemon.generate(256) 
# Generate the seed from the mnemonic
seed = mnemon.to_seed(mnemonic_words)

# Generate private key from the seed
root_key = bip32utils.BIP32Key.fromEntropy(seed)
# This path follows the BIP44 standard for Bitcoin
child_key = root_key.ChildKey(44 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN).ChildKey(0 + bip32utils.BIP32_HARDEN).ChildKey(0).ChildKey(0)

# Generate public key and private key in Wallet Import Format (WIF)
private_key_wif = child_key.WalletImportFormat()
public_key = child_key.PublicKey().hex()

# Generate address in bitcoin format
child_address = child_key.Address()

print('=> mnemonic_words:', mnemonic_words)
print('=> private key (WIF):', private_key_wif)
print('=> public key:', public_key)
print('=> address:', child_address)