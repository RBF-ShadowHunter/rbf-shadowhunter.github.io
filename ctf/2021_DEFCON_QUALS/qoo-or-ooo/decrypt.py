from Crypto.Cipher import AES
import hashlib
import sys
from time import sleep

ciphertext = 'baba14aa468f7f0cc37aa61985cf01f08899e9a9799b496f8e21f09295b878b1571375e67768ef6d6d47596229bd1b046af56aef03'
nonce = '0e57c87d3787cf9ee34f6a67fd99fbb3'
secret_key = '100010000000001000011010101110'

#skl = [int(x) for x in secret_key]
ciphertext_bytes = bytes.fromhex(ciphertext)

def key_array_to_key_string(key_list):
    key_string_binary = b''.join([bytes([x]) for x in key_list])
    return hashlib.md5(key_string_binary).digest()


if __name__ == '__main__':
    #for i in range(1073741823,500000,-1): # Stopped at 1070727920
    #digi = 30
    digi = 11
    for i in range(4096):
        print("Trying {}...".format(i))
        secret_key = bin(i)[2:].zfill(digi)
        #secret_key = '00000101110' # Manual secret_key
        #secret_key = '100011111100'
        skl = [int(x) for x in secret_key]
        key = key_array_to_key_string(skl)
        #print("KEY: {}".format(key))
        cipher = AES.new(key, AES.MODE_EAX, nonce=bytes.fromhex(nonce))
        plaintext_bytes = cipher.decrypt(ciphertext_bytes)
        try:
            plaintext = plaintext_bytes.decode('ascii')
        except:
            plaintext = "SKIPPED"
        #plaintext = plaintext_bytes.decode('utf-8',errors='replace')
        #print("FLAG: {}".format(plaintext))
        #if "OOO{" in plaintext:
        if plaintext != "SKIPPED": #This will show the flag.
            print("KEY:  {}".format(key))
            print("FLAG: {}".format(plaintext))
            sleep(10)
    sys.exit()
        #else: # For manual, uncomment
        #    print("KEY:  {}".format(key))
        #    print("FLAG: {}".format(plaintext))
        #    sys.exit()
