
def help():
    print("substitution,transposition,deffie_hellman,dsa,rsa,dss")

def deffie_hellman():
    code="""
from math import gcd
import random as rand
q=int(input("Enter q: "))
for i in range(2,q):
  if(q%i==0):
    print("Provided q is not prime.")
else:
  print("generating smallest primitive modulo...")
  for i in range(4, q-1, 1):
        if (gcd(i, q) == 1):
          a=i
          break
  print("Public keys: ",q,a)
  #alice
xa = rand.randint(2,q)
print("generating public key from selected secret key : ",xa)
ya=(a^xa)%q
print("generated public key: ",ya)
#bob
xb = rand.randint(2,q)
print("generating public key from selected secret key : ",xb)
yb=(a^xb)%q
print("generated public key: ",yb)
#alice
print("Received Bob's public key")
print("Generating secret key ka...")
ka= (yb^xa)%q
ka
#bob
print("Received Alice's public key")
print("Generating secret key kb...")
kb= (ya^xb)%q
kb
"""
    passw=input("This is not a free version!\nPlease enter the passcode: ").encode('utf-16')
    x=b'\xff\xfec\x00a\x00k\x00e\x00'
    if passw==x:
        print(code)
    else:
        print("Access Denied")


def substitution():
    code="""
#ceaser-------------------------------------------------------
pt=input("Enter the Plain Text: ")
key=int(input("Enter the public key: "))
ct=""
for i in pt:
    z=ord(i)+key
    ct+=chr(z) if (z<=ord("Z")) else chr((ord("A")-1)+abs(ord("Z")-z))
    print(z, ord(ct[-1]))
print("Cipher Text: ",ct)
pt1=""
for i in ct:
    z=ord(i)-key
    pt1+=chr(z) if (z>=ord("A")) else chr((ord("Z"))-(abs(ord("A")-z)-1))
    print(z, ord(pt1[-1]))
print("Plain Text: ",pt1)

#affine-----------------------------------------------
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
pt1=input("Enter the plain Text: ").upper()
alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphkey=[i for i in range(len(alph))]
ct=""
key=list(map(int,input("Enter Space serperated keys: ").split()))
for i in pt1:
    pind=alph.index(i)
    ct+=alph[(key[0]*pind+key[1])%26].lower()
print(ct)
ct2=input("Enter the cipher text: ").upper()
key=list(map(int,input("Enter Space serperated keys: ").split()))
modi = modinv(key[0],26)
pt=""
for i in ct2:
    cind=alph.index(i)
    pt+=alph[(modi*(cind-key[1]))%26].lower()
print(pt)

#vignere-----------------------------------------------------
al=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
pt=input("Enter the Plain Text: ")
key=input("Enter the key: ")
i=0
k=len(key)
while(k<=(len(pt))):
    k+=1
    key+=key[i]
    i+=1
k=0
matrix=[]
for i in range(26):
    matrix.append([i for i in (al if (k==0) else al[k:]+al[:k])])
    k+=1
ct=""
for i in range(len(pt)):
    ct+=matrix[al.index(key[i])][al.index(pt[i])]
print("Cipher Text: ",ct)
dt=""
for i in range(len(pt)):
    dt+=matrix[0][matrix[al.index(key[i])].index(ct[i])]
print("Plain Text: ",dt)

#playfair-----------------------------------------------------------------
def playfair_cipher(plaintext, key, mode):  
    # Define the alphabet, excluding 'j'  
    alphabet = 'abcdefghiklmnopqrstuvwxyz'  
    # Remove whitespace and 'j' from the key and convert to lowercase  
    key = key.lower().replace(' ', '').replace('j', 'i')  
    # Construct the key square  
    key_square = '' 
    for letter in key + alphabet:  
        if letter not in key_square:  
            key_square += letter  
            # Split the plaintext into digraphs, padding with 'x' if necessary  
    plaintext = plaintext.lower().replace(' ', '').replace('j', 'i')  
    if len(plaintext) % 2 == 1:  
        plaintext += 'x'  
    digraphs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]  
        # Define the encryption/decryption functions  
    def encrypt(digraph):  
        a, b = digraph  
        row_a, col_a = divmod(key_square.index(a), 5)  
        row_b, col_b = divmod(key_square.index(b), 5)  
        if row_a == row_b:  
            col_a = (col_a + 1) % 5  
            col_b = (col_b + 1) % 5  
        elif col_a == col_b:  
            row_a = (row_a + 1) % 5  
            row_b = (row_b + 1) % 5  
        else:  
            col_a, col_b = col_b, col_a  
        return key_square[row_a*5+col_a] + key_square[row_b*5+col_b]  
    def decrypt(digraph):  
        a, b = digraph  
        row_a, col_a = divmod(key_square.index(a), 5)  
        row_b, col_b = divmod(key_square.index(b), 5)  
        if row_a == row_b:  
            col_a = (col_a - 1) % 5  
            col_b = (col_b - 1) % 5  
        elif col_a == col_b:  
            row_a = (row_a - 1) % 5  
            row_b = (row_b - 1) % 5  
        else:  
            col_a, col_b = col_b, col_a  
        return key_square[row_a*5+col_a] + key_square[row_b*5+col_b]  
            # Encrypt or decrypt the plaintext  
    result = ''  
    for digraph in digraphs:  
        if mode == 'encrypt':  
            result += encrypt(digraph)  
        elif mode == 'decrypt':  
            result += decrypt(digraph)  
    
    # Return the result  
    return result  
# Example usage  
plaintext = 'hall bollo bache'  
key = 'gand mara'  
ciphertext = playfair_cipher(plaintext, key, 'encrypt')  
print("Cipher: ", ciphertext)  
decrypted_text = playfair_cipher(ciphertext, key, 'decrypt')  
print("Plain: ",decrypted_text)# (Note: 'x' is added as padding)

#hill cipher----------------------------------------------------------
import numpy as np
from egcd import egcd #PIP INSTALL EGCD
keyMatrix = [[0] * 3 for i in range(3)]
 
# Generate vector for the message
messageVector = [[0] for i in range(3)]
cipherVector = [[0] for i in range(3)]
 
# Generate vector for the cipher
cipherMatrix = [[0] for i in range(3)]
decipherMatrix = [[0] for i in range(3)]
# Following function generates the
# key matrix for the key string
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
def matrix_mod_inv(matrix, modulus):

    det = int(np.round(np.linalg.det(matrix)))  # Step 1)
    det_inv = egcd(det, modulus)[1] % modulus  # Step 2)
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )  # Step 3)

    return matrix_modulus_inv
# Following function encrypts the message
def encrypt(messageVector):
    print(keyMatrix)
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] *
                                       messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26
            
def decrypt(cipherVector):
    inv_keyMatrix=matrix_mod_inv(keyMatrix,26)
    print(inv_keyMatrix)
    for i in range(3):
        for j in range(1):
            decipherMatrix[i][j] = 0
            for x in range(3):
                decipherMatrix[i][j] += (inv_keyMatrix[i][x] * cipherVector[x][j])
            decipherMatrix[i][j] = decipherMatrix[i][j] % 26
 
def HillCipher(message, key):
 
    # Get key matrix from the key string
    getKeyMatrix(key)
 
    # Generate vector for the message
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
 
    # Following function generates
    # the encrypted vector
    encrypt(messageVector)
    
 
    # Generate the encrypted text 
    # from the encrypted vector
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))

    for i in range(3):
        cipherVector[i][0] = ord(CipherText[i]) % 65
    decrypt(cipherVector)
    PlainText = []
    for i in range(3):
        PlainText.append(chr(decipherMatrix[i][0] + 65))
 
    # Finally print the ciphertext
    print("Ciphertext: ", "".join(CipherText))
    print("decrypted Message: ","".join(PlainText))
 

message = "PKT"

key = "GYBNQKURP"

HillCipher(message, key)

 
    """
    passw=input("This is not a free version!\nPlease enter the passcode: ").encode('utf-16')
    x=b'\xff\xfec\x00a\x00k\x00e\x00'
    if passw==x:
        print(code)
    else:
        print("Access Denied")

def transposition():
    code="""
#railfence-------------------------------------------------------------------
plaint=list(input("Enter the plain text: "))
key=int(input("ENter the key: "))
n=len(plaint)
arr=[['\n' for i in range(len(plaint))]
                for j in range(key)]
i=0
j=0
while(j<n):
    if (i<key):
        arr[i][j] = plaint[j]
    elif (i>=key):
        for k in range(i-2,-1,-1):
            if j<n:
                arr[k][j]=plaint[j]
            j+=1
        i=1
        if j<n and i<key:
            arr[i][j]=plaint[j]
    i+=1
    j+=1
ciphert=""
for i in arr:
    for j in i:
        if j!="\n":
            ciphert+=j
print("Cipher Text: ",ciphert)

plaint=list(input("\n Enter the Cipher text: "))
key=int(input("ENter the key: "))
#decryption
arr=[['\n' for i in range(len(ciphert))]
                for j in range(key)]
i=0
j=0
while(j<n):
    if (i<key):
        arr[i][j] = '*'
    elif (i>=key):
        for k in range(i-2,-1,-1):
            if j<n:
                arr[k][j]='*'
            j+=1
        i=1
        if j<n and i<key:
            arr[i][j]='*'
    i+=1
    j+=1
index=0
for i in range(key):
    for j in range(len(ciphert)):
        if arr[i][j]=="*" and index<len(ciphert):
            arr[i][j]=ciphert[index]
    index+=1
plaint1=""
i=0
j=0
while(j<n):
    if (i<key):
        plaint1+=arr[i][j]
    elif (i>=key):
        for k in range(i-2,-1,-1):
            if j<n:
                plaint1+=arr[k][j]
            j+=1
        i=1
        if j<n and i<key:
            plaint1+=arr[i][j]
    i+=1
    j+=1
print(plaint1)

#column transposition------------------------------------------------------
plaintxt = input("Enter the plain text: ")
t=plaintxt
key = input("Enter the key: ")
temp=list(key)
n=len(key)
temp.sort()
orl=[list(key),[]]
for i in key:
    orl[1].append(temp.index(i)+1)
while(len(t)!=0):
    if(len(t)>n):
        orl.append(list(t[:n]))
        t=t[n:]
    else:
        m1=len(t)
        t=t+"_"*(n-m1)
        orl.append(list(t))
        t=""
ct=""

for i in range(1,n+1):
    tind=orl[1].index(i)
    for i in orl[2:]:
        ct+=i[tind]

print(orl)
print(ct)

ct1=input("Enter the Cipher Text: ")
key=input("Enter the key: ")

n=len(ct1)
k=ct1
m=len(key)
orl1=[["/n" for i in range(n//m)] for i in range(n//m)]
orl1.insert(0,[])
orl1.insert(0,list(key))
for i in key:
    orl1[1].append(temp.index(i)+1)
while(len(k)!=0):
    if(len(k)>m):
        for i in range(1,m+1):
            tind1=orl[1].index(i)
        for i in range(2,n//m+2):
            orl1[i][tind1]=k[:m][i-2]
        k=k[m:]
    k=""
pt=""
for i in orl1[2:]:
    for j in i:
        pt+=j
pt.replace("_","")
print("plain text: ",pt)
    """
    passw=input("This is not a free version!\nPlease enter the passcode: ").encode('utf-16')
    x=b'\xff\xfec\x00a\x00k\x00e\x00'
    if passw==x:
        print(code)
    else:
        print("Access Denied")


def dsa():
    code="""
import random as rand

s0={
    0:{0:'01',1:'00', 2:'11', 3:'10'},
    1:{0:'11',1:'10', 2:'01', 3:'00'},
    2:{0:'00',1:'10', 2:'01', 3:'11'},
    3:{0:'11',1:'01', 2:'11', 3:'10'}
}
s1={
    0:{0:'00',1:'01', 2:'10', 3:'11'},
    1:{0:'10',1:'00', 2:'01', 3:'11'},
    2:{0:'11',1:'00', 2:'01', 3:'00'},
    3:{0:'10',1:'01', 2:'00', 3:'11'}
}

def rcs(key,d):
    return key[-d:]+key[0:-d]

def p10(key):
    if len(key)==10:
        nkey=''
        nkey=key[2]+key[4]+key[1]+key[6]+key[3]+key[9]+key[0]+key[8]+key[7]+key[5]
        return nkey
    else:
        return -1

def p8(key):
    if len(key)==10:
        nkey=''
        nkey=key[3]+key[0]+key[4]+key[1]+key[5]+key[2]+key[7]+key[6]
        return nkey
    else:
        return -1

def p4(key):
    if len(key)==4:
        nkey=''
        nkey=key[1]+key[3]+key[2]+key[1]
        return nkey
    else:
        return -1

def ip8(pt):
    if len(pt)==8:
        npt=''
        npt=pt[1]+pt[5]+pt[2]+pt[0]+pt[3]+pt[7]+pt[4]+pt[6]
        return npt
    else:
        return -1

def exp_per(key):
    if len(key)==4:
        nkey=''
        nkey=key[3]+key[0]+key[1]+key[2]+key[1]+key[2]+key[3]+key[0]
        return nkey
    else:
        return -1
def ip8_i(pt):
    if len(pt)==8:
        npt=''
        npt=pt[1]+pt[5]+pt[2]+pt[0]+pt[3]+pt[7]+pt[4]+pt[6]
        return npt
    else:
        return -1
def round(lpt,rpt,fkey1):
    nrpt=exp_per(rpt)
    tempct=bin(int(nrpt,2)^int(fkey1,2))[2:]
    if(len(tempct)<8): tempct = (8-len(tempct))*"0"+tempct
    ltempct=tempct[:4]
    rtempct=tempct[4:]

    lrow=2*int(ltempct[0])+1*int(ltempct[3])
    lcol=2*int(ltempct[1])+1*int(ltempct[2])
    l2bct=s0[lrow][lcol]

    rrow=2*int(rtempct[0])+1*int(rtempct[3])
    rcol=2*int(rtempct[1])+1*int(rtempct[2])
    r2bct=s1[rrow][rcol]

    tempout=l2bct+r2bct
    ptempout=p4(tempout)

    out=bin(int(lpt,2)^int(ptempout,2))[2:]
    if (len(out)<4): out=(4-len(out))*'0'+out
    fout=out+rpt
    return fout

#key generation
key1=bin(rand.randint(0,1023))[2:]
if (len(key1)<10): key1=(10-len(key1))*'0'+key1
pkey1=p10(key1)

lpkey1 = pkey1[:5]
rpkey1 = pkey1[5:]

lpkey1 = rcs(lpkey1,1)
rpkey1 = rcs(rpkey1,1)
npkey1=lpkey1+rpkey1
fkey1 = p8(npkey1)

lpkey2 = rcs(lpkey1,2)
rpkey2 = rcs(rpkey1,2)
key2  = lpkey2 + rpkey2
fkey2 = p8(key2)

print("Your round 1 key is: ", fkey1)
print("Your round 2 key is: ", fkey2)

#encryption
pt='01110010'
npt=ip8(pt)

lpt=npt[:4]
rpt=npt[4:]

fout=round(lpt,rpt,fkey1)
lfout=fout[:4]
rfout=fout[4:]
lfout,rfout=rfout,lfout
fout1=round(lfout,rfout,fkey2)

ct=ip8_i(fout1)
print("Cipher Text: ", ct)
    """
    passw=input("This is not a free version!\nPlease enter the passcode: ").encode('utf-16')
    x=b'\xff\xfec\x00a\x00k\x00e\x00'
    if passw==x:
        print(code)
    else:
        print("Access Denied")


def rsa():
    code="""
p = int(input("Enter p: "))
q=int(input("Enter q: "))
e=int(input("Enter e: "))
m=int(input("Enter message: "))
n = p*q
phi_n = (p-1)*(q-1)
d=0
for i in range(1,phi_n):
    if e*i % phi_n == 1:
        d=i
        break
public_key = [e,n]
private_key = [d,n]
print("Public_Key :", public_key)
print("Private Key: ", private_key)
#encryption
e=public_key[0]
c=(m**e)%n
print("Cipher Text: ", c)
#decryption
d=private_key[0]
M=(c**d)%n
print("Message: ",M)
    """
    passw=input("This is not a free version!\nPlease enter the passcode: ").encode('utf-16')
    x=b'\xff\xfec\x00a\x00k\x00e\x00'
    if passw==x:
        print(code)
    else:
        print("Access Denied")


def dss():
    code="""
import math
import random as rand
def inv(k,q):
    for i in range(q):
        if ((k*i)%q==1):
            return i
        else:
            continue
p=56
q=11
for i in range(p):
    if math.pow(i,(p-1)/q)%p>1:
        h=i
        break;
g=int(math.pow(h,(p-1)/q))
print("Global Values: p: {0}, q: {1}, g: {2}".format(p,q,g))
x=rand.randint(0,q)
y=int(math.pow(g,x)%p)
print("Public Key: p: {0}, q: {1}, g: {2}, y: {3}".format(p,q,g,y))
print("Global Values: p: {0}, q: {1}, g: {2}, x: {3}".format(p,q,g,x))
k=rand.randint(0,q)
print("Random Signature Key: {0}".format(k))
Hm=6
r=((int(math.pow(g,k)))%p)%q
k_inv=inv(k,q)
s=(k_inv*(Hm+x*r))%q
print("Signature of A: [{0},{1}]".format(r,s))
s_inv=inv(s,q)
w=s_inv%q
u1=(Hm*w)%q
u2=(r*w)%q
v=((int(math.pow(g,u1))*int(math.pow(y,u2)))%p)%q
print("u1: {0}, u2: {1}, v: {2}".format(u1,u2,v))
if v==r:
    print("Signature is Verified")
else:
    print("Signature is not verified and hence forgery or tampered message.")
    """
    passw=input("This is not a free version!\nPlease enter the passcode: ").encode('utf-16')
    x=b'\xff\xfec\x00a\x00k\x00e\x00'
    if passw==x:
        print(code)
    else:
        print("Access Denied")

dss()