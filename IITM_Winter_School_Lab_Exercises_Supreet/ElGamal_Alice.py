from helper import *
# import random

m = "Hello, ElGamal works"
#----------------------------------------------------------------
def Alice(m, logging = False):
    c = socket_setup(client = True)
    #----------------------------------------------------------------
    def interaction(logging = False):

        pub_key_str = c.recv(1024).decode()
        G_sz, g, h = map(int, pub_key_str.split(","))
        if(logging):
            print("Public Key Received: ", pub_key_str)

        #------------------------------
        # EXERCISE: Write the missing code, import necessary functions from helper.py
        encoded_m = encode_message(m)
        if(logging):
            print("M: ", encoded_m)

        #------------------------------

        # EXERCISE: Find y, s and cipher_text and uncomment the following lines
        y = random.SystemRandom().randint(2, G_sz - 1)
        g_y = mod_exp(g, y, G_sz) 
        s = (mod_exp(h, y, G_sz)*encoded_m)
        cipher_text = [g_y, s]

        #------------------------------
        # Uncomment when above code is complete

        c.send(f"{cipher_text[0]},{cipher_text[1]}".encode())
        if(logging):
            print("Cipher text Sent: ", cipher_text)
            
    #----------------------------------------------------------------
    interaction(logging)
#----------------------------------------------------------------
Alice(m, logging = True)
