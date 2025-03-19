from helper import *
import random


#----------------------------------------------------------------
#--------------------Server Setup--------------------------------
def Bob(logging = False):
    s = socket_setup()
    # EXERCISE: Find a large prime for the group size
    group_sz = gen_large_prime(128)
    N = group_sz
     
    #----------------------------------------------------------------
    #--------------------Client Server Interaction-------------------
    def interaction(logging = False):
        c, addr = s.accept()
        if(logging):
            print("PUBLIC: Connection Established. Establishing Group Size.")
         #Uncomment after finding group_sz
        c.send(f"{group_sz}".encode())
        if(logging):
            print("PUBLIC: Group Size Established to be ", group_sz)
            print("PUBLIC: Generator g = 2")
        #------------------------------
        #EXERCISE: Write the missing code, import necessary functions from helper.py
        
        #------------------------------
        # b is the private key of Bob
        b = random.SystemRandom().randint(1, group_sz - 1)
        
        # EXERCISE: Find g^b and uncomment the following lines
        g_b = mod_exp(2, b, N)
        if(logging):
            print("PUBLIC: Sending g^b = ", g_b)
        c.send(f"{g_b}".encode())
        #------------------------------
        g_a = int(c.recv(1024).decode())
        if(logging):
            print("PUBLIC: Received g^a = ", g_a)
        #------------------------------
        # EXERCISE: Find g^ab and uncomment the following lines
        g_ab = mod_exp(g_a, b, N)
        
        if(logging):
            print("PRIVATE: Constructed g^ab = ", g_ab)
            print("---Key Exchange Complete---")
        s.close()
        return b, g_b, g_ab
    return interaction(logging)
#----------------------------------------------------------------
Bob(logging = True)

# EXERCISE: Add an extra interaction to establish generator g instead of fixing it as 2
