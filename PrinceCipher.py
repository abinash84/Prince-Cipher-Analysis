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



def hex_to_list(data):
        ret=[]
        for num in data:
                ret.append(int(num,16))
        return ret
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


def sbox(data, box):
        ret = []
        for nibble in data:
            temp=hex(nibble)
            temp=temp[2:]
            ret.append(int(box[temp],16))
        return ret


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

def first5(data, key):
        for idx in (1,2,3,4,5):
            data = sbox(data,S_box)
            data = mprime(data)
            data = shiftrows(data, inverse = False)
            data = bit_xor(bit_xor(Round_constants[idx],key),data)
        return data


def last5(data, key):
        for idx in (6,7,8,9,10):
            data = bit_xor(bit_xor(Round_constants[idx],key),data)
            data = shiftrows(data, inverse = True)
            data = mprime(data)
            data = sbox(data,S_inv)
        return data

def core(data, key):
        data = bit_xor(bit_xor(Round_constants[0],key),data)
        data = first5(data, key)

        data = sbox(data, S_box)
        data = mprime(data)
        data = sbox(data, S_inv)

        data = last5(data, key)
        return bit_xor(bit_xor(Round_constants[11],key),data)

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



def encrypt(plaintext,key):
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
        data=core(data,k1)
        data=bit_xor(data,k0prime)
        return list_to_hex(data)

def decrypt(plaintext,key):
        final_key= "0000000000000000c0ac29b7c97c50dd"
        data=[0 for i in range(len(plaintext))]
        for i in range(len(plaintext)):
                data[i]=int(plaintext[i],16)
        k=[0 for i in range(len(key))]
        for i in range(len(key)):
                k[i]=int(key[i],16)
        final=[0 for i in range(len(final_key))]
        for i in range(len(final_key)):
                final[i]=int(final_key[i],16)
        final=bit_xor(k,final)
        extended=extend(final)
        k0prime=extended[0:16]
        k0=extended[16:32]
        k1=extended[32:48]
        data=bit_xor(data,k0)
        data=core(data,k1)
        data=bit_xor(data,k0prime)
        return list_to_hex(data)

# Encryption Test Vectors
print(encrypt("0000000000000000","00000000000000000000000000000000"))
print(encrypt("ffffffffffffffff","00000000000000000000000000000000"))
print(encrypt("0000000000000000","ffffffffffffffff0000000000000000"))
print(encrypt("0000000000000000","0000000000000000ffffffffffffffff"))
print(encrypt("0123456789abcdef","0000000000000000fedcba9876543210"))


# Decryption Test Vectors
print(decrypt("818665aa0d02dfda","00000000000000000000000000000000"))
print(decrypt("604ae6ca03c20ada","00000000000000000000000000000000"))
print(decrypt("9fb51935fc3df524","ffffffffffffffff0000000000000000"))
print(decrypt("78a54cbe737bb7ef","0000000000000000ffffffffffffffff"))
print(decrypt("ae25ad3ca8fa9ccf","0000000000000000fedcba9876543210"))


