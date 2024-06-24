from random import randint
 
if __name__ == '__main__':
 
    # Both persons agrees on public keys Gs and Ps
    # Prime number P
    Ps = 23
     
    # Gs is primitive root for Ps
    Gs = 9
     
      
    print('Value of Ps is : %d'%(Ps))
    print('Value of Gs is : %d'%(Gs))
     
    # g is the private key chosen by Joy
    g = 4
    print('Private Key g is: %d'%(g))
     
    # fetches the generated key
    p = int(pow(Gs,g,Ps)) 
     
    # h will be the chosen private key by Happy
    h = 3
    print('Private Key h is : %d'%(h))
    
    # fetches the generated key
    q = int(pow(Gs,h,Ps)) 
     
     
    # Joy's Secret key
    K_A = int(pow(q,g,Ps))
     
    #  Happy's Secret key
    K_B = int(pow(p,h,Ps))
     
    print('Alice\'s Secret key is : %d'%(K_A))
    print('Bob\'s Secret key is : %d'%(K_B))
