# Defining Sboxes and round constants
S_box={"0" : "b", "1" : "f", "2" : "3", "3" : "2", "4" : "a", "5" : "c", "6" : "9", "7" : "1",
"8" : "6", "9" : "7", "a" : "8", "b" : "0", "c" : "e", "d" : "5", "e" : "d", "f" : "4"}
S_inv={"0" : "b", "1" : "7", "2" : "3", "3" : "2", "4" : "f", "5" : "d", "6" : "8", "7" : "9",
"8" : "a", "9" : "6", "a" : "4", "b" : "0", "c" : "5", "d" : "e", "e" : "c", "f" : "1"}
Round_constants=[[0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0],
                [0x1,0x3,0x1,0x9,0x8,0xa,0x2,0xe,0x0,0x3,0x7,0x0,0x7,0x3,0x4,0x4],
                [0xa,0x4,0x0,0x9,0x3,0x8,0x2,0x2,0x2,0x9,0x9,0xf,0x3,0x1,0xd,0x0],
                [0x0,0x8,0x2,0xe,0xf,0xa,0x9,0x8,0xe,0xc,0x4,0xe,0x6,0xc,0x8,0x9],
                [0x4,0x5,0x2,0x8,0x2,0x1,0xe,0x6,0x3,0x8,0xd,0x0,0x1,0x3,0x7,0x7],
                [0xb,0xe,0x5,0x4,0x6,0x6,0xc,0xf,0x3,0x4,0xe,0x9,0x0,0xc,0x6,0xc],
                [0x7,0xe,0xf,0x8,0x4,0xf,0x7,0x8,0xf,0xd,0x9,0x5,0x5,0xc,0xb,0x1],
                [0x8,0x5,0x8,0x4,0x0,0x8,0x5,0x1,0xf,0x1,0xa,0xc,0x4,0x3,0xa,0xa],
                [0xc,0x8,0x8,0x2,0xd,0x3,0x2,0xf,0x2,0x5,0x3,0x2,0x3,0xc,0x5,0x4],
                [0x6,0x4,0xa,0x5,0x1,0x1,0x9,0x5,0xe,0x0,0xe,0x3,0x6,0x1,0x0,0xd],
                [0xd,0x3,0xb,0x5,0xa,0x3,0x9,0x9,0xc,0xa,0x0,0xc,0x2,0x3,0x9,0x9],
                [0xc,0x0,0xa,0xc,0x2,0x9,0xb,0x7,0xc,0x9,0x7,0xc,0x5,0x0,0xd,0xd]]
# These are all functions used in the encryption implementation of PRINCE cipher
def format1(string):
    while len(string)<2:
        string='0'+string
    return string
def hex_to_list(data):
        ret=[]
        for num in data:
                ret.append(int(num,16))
        return ret
def dic2list(dic):
    temp=[]
    for i in range(16):
        temp.append(dic[i][0])
    return temp
def list_to_hex(data):
        res=""
        for nibble in data:
                temp=hex(nibble)[2:]
                res+=temp
        return res

def hex_to_bin(data):
        ret=[0 for i in range(4*len(data))]
        i=0
        for nibble in data:
                v=bin(nibble)[2:]
                extra_zeros='0'*(4-len(v))
                v=extra_zeros+v
                ret[i]=int(v[0])
                ret[i+1]=int(v[1])
                ret[i+2]=int(v[2])
                ret[i+3]=int(v[3])
                i=i+4
        return ret
def bin_to_int(data):
        listToStr = ''.join([str(elem) for elem in data])
        ret=[]
        for i in range(0,len(listToStr),4):
                ret.append(int(listToStr[i:i+4],2))
                
        return ret


def bit_xor(v1,v2):
    v3=[]
    for i in range(len(v1)):
        v3.append(v1[i]^v2[i])
    return v3
def bit_xor2(s1,s2):
    s3=''
    for i in range(len(s1)):
        s3=s3+hex((int('0x'+s1[i],16)^int('0x'+s2[i],16))).split('0x')[1]
    return s3
# Function to use sbox
def sbox(data, box):
        ret = []
        for nibble in data:
            temp=hex(nibble)
            temp=temp[2:]
            ret.append(int(box[temp],16))
        return ret

# Performing mixcolumns using M0, M1 as described in PRINCE
def m0(data):
        ret = [0 for i in range(16)]
        ret[0] = data[4] ^ data[8] ^ data[12]
        ret[1] = data[1] ^ data[9] ^ data[13]
        ret[2] = data[2] ^ data[6] ^ data[14]
        ret[3] = data[3] ^ data[7] ^ data[11]
        ret[4] = data[0] ^ data[4] ^ data[8]
        ret[5] = data[5] ^ data[9] ^ data[13]
        ret[6] = data[2] ^ data[10] ^ data[14]
        ret[7] = data[3] ^ data[7] ^ data[15]
        ret[8] = data[0] ^ data[4] ^ data[12]
        ret[9] = data[1] ^ data[5] ^ data[9]
        ret[10] = data[6] ^ data[10] ^ data[14]
        ret[11] = data[3] ^ data[11] ^ data[15]
        ret[12] = data[0] ^ data[8] ^ data[12]
        ret[13] = data[1] ^ data[5] ^ data[13]
        ret[14] = data[2] ^ data[6] ^ data[10]
        ret[15] = data[7] ^ data[11] ^ data[15]
        return ret

def m1(data):
        ret = [0 for i in range(16)]
        ret[0] = data[0] ^ data[4] ^ data[8]
        ret[1] = data[5] ^ data[9] ^ data[13]
        ret[2] = data[2] ^ data[10] ^ data[14]
        ret[3] = data[3] ^ data[7] ^ data[15]
        ret[4] = data[0] ^ data[4] ^ data[12]
        ret[5] = data[1] ^ data[5] ^ data[9]
        ret[6] = data[6] ^ data[10] ^ data[14]
        ret[7] = data[3] ^ data[11] ^ data[15]
        ret[8] = data[0] ^ data[8] ^ data[12]
        ret[9] = data[1] ^ data[5] ^ data[13]
        ret[10] = data[2] ^ data[6] ^ data[10]
        ret[11] = data[7] ^ data[11] ^ data[15]
        ret[12] = data[4] ^ data[8] ^ data[12]
        ret[13] = data[1] ^ data[9] ^ data[13]
        ret[14] = data[2] ^ data[6] ^ data[14]
        ret[15] = data[3] ^ data[7] ^ data[11]
        return ret
def mprime(data):
        data=hex_to_bin(data)
        ret = [0 for i in range(64)]
        ret[ 0:16] = m0(data[ 0:16])
        ret[16:32] = m1(data[16:32])
        ret[32:48] = m1(data[32:48])
        ret[48:64] = m0(data[48:64])
        ret=bin_to_int(ret)
        return ret
# Shift row
def shiftrows(data, inverse):
        ret = [0 for i in range(16)]
        idx = 0
        for nibble in data:
            ret[idx] = nibble
            if not inverse:
                idx = (idx + 13) % 16
            else:
                idx = (idx +  5) % 16
        return ret
# Key expansion
def extend(key):
        key_bin= hex_to_bin(key)

        newKey=[0 for i in range(192)]
        for i in range(64):
                newKey[i]=key_bin[i]
                newKey[i+128]=key_bin[i+64]
        for i in range(63):
                newKey[65+i]=key_bin[i]
        newKey[64]=key_bin[63]
        newKey[127]=newKey[127]^key_bin[0]
        return bin_to_int(newKey)
# Encrypt 4 rounds for the round reduced implementation
def encrypt_4round(plaintext,key):
        data=[0 for i in range(len(plaintext))]
        for i in range(len(plaintext)):
                data[i]=int(plaintext[i],16)
        k=[0 for i in range(len(key))]
        for i in range(len(key)):
                k[i]=int(key[i],16) 
        extended=extend(k)
        k0=extended[0:16]
        k0prime=extended[16:32]
        k1=extended[32:48]

        data=bit_xor(data,k0)
        data = sbox(data,S_box)
        data = mprime(data)
        data = shiftrows(data, inverse = False)
        data = bit_xor(bit_xor(Round_constants[5],k1),data)  
        #R5
        data = sbox(data, S_box)
        data = mprime(data)
        data = sbox(data, S_inv)

        data = bit_xor(bit_xor(Round_constants[6],k1),data)
        data = shiftrows(data, inverse = True)
        data = mprime(data)
        data = sbox(data,S_inv)
        data=bit_xor(data,bit_xor(k0prime,k1))
        return list_to_hex(data)
# Check balanced
def isbalanced(data):
    res=data[0]
    for nibble in range(1,len(data)):
        res=bit_xor2(res,data[nibble])
    if res == '0':
        return True
    return False
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3

# Defining inputs for 5 sets and key
all_=[]
const=[]
input1=[]
input_list=["0010000000000001","0010000111000010","1110000000100000","0010010000000000","0000000000000000"]
key="010110000000000000000000010a0b11"
k=[0 for i in range(len(key))]
for i in range(len(key)):
        k[i]=int(key[i],16) 
extended=extend(k)
k0=extended[0:16]
k0prime=extended[16:32]
k1=extended[32:48]
print("k1 is")
print(k1)
print("k1 xor k0 is")
print(bit_xor(k0prime,k1))
# Creating inputs with all property and constant property as described in the algorithm. Input 1 contains 1 active nibble whereas Input 2 contains 4 active nibbles
input3=[]
for i in range(16):
    all_.append(hex(i).split('0x')[1])
sets=[]
sets2=[]
input2=[]
for s in range(5):
        for i in range(16):
            input1.append(all_[i]+input_list[s][1:])
            input2.append(all_[i]+input_list[s][1:7]+all_[i]+input_list[s][8:10]+all_[i]+input_list[s][11:13]+all_[i]+input_list[s][14:16])
        sets.append(input1)
        sets2.append(input2)
        input1=[]
        input2=[]
candidates=[]
a=[]
b=[]
temp=[]
mydicl=[]
mydic={}
# Recovering k0 xor k1
for s in range(5):
    ciphertexts=[]
    mydic={}
    # Encrypting
    for i in range(16):
        ciphertexts.append(encrypt_4round(sets[s][i],key))
    for i in range(16):
        mydic[i]=[]
    # Guessing nibble by nibble the value of k0 xor k1
    for key_xor in range(16):
            for k in range(16):
                for j in range(16):
                    res1=bit_xor2(ciphertexts[j][k],hex(key_xor).split('0x')[1])
                    temp.append(S_box[res1])
                if isbalanced(temp):
                    mydic[k].append(key_xor)
                temp=[]
    mydicl.append(mydic)
final={}
# Finding intersection of 5 sets to remove false positives
for i in range(16):
    templist=mydicl[0][i]
    for j in range(5):
        templist=intersection(templist,mydicl[j][i])
    final[i]=templist
print("Value of k0 xor k1 obtained")
print(final.values())
#Recovering k1
mydicl=[]
for s in range(5):
    ciphertexts=[]
    peeledoff=[]
    mydic={}
    for i in range(16):
        mydic[i]=[]    
    sum_='0'
    sum2='0'
    for i in range(16):
        ciphertexts.append(encrypt_4round(sets2[s][i],key))
    xor=dic2list(final)
    cl=[]
    cll=[]
    for j in range(16):
        for i in range(len(ciphertexts[j])):
                cl.append(int(ciphertexts[j][i],16))
        cll.append(cl)
        cl=[]
    datal=[]
    for i in range(16):  
        # Peeling last layer          
        data=bit_xor(cll[i],xor)
        data=sbox(data,S_box)
        # Inverting shiftrow,mixcolumn
        data = mprime(data)
        data = shiftrows(data, inverse = False)
        data=bit_xor(Round_constants[6],data)
        for i in range(len(data)):
                data[i]=hex(data[i]).split('0x')[1] 
        datal.append(data)
    temp=[]
    # Guessing key nibble
    for key_nibble in range(16):
        for k in range(16):
            for j in range(16):
                res2=bit_xor2(datal[j][k],hex(key_nibble).split('0x')[1])
                temp.append(S_box[res2])
            #print(temp)
            if isbalanced(temp):
                mydic[k].append(key_nibble)
            temp=[]
    mydicl.append(mydic)
final2={}
#Remove false positives using 5 sets
for i in range(16):
    templist=mydicl[0][i]
    for j in range(5):
        templist=intersection(templist,mydicl[j][i])
    final2[i]=templist
print("k1 recovered is")
print(final2.values())