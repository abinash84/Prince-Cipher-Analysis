# Calculation of DDT characteristics for Inverse S-box

S_inv={"0" : "b", "1" : "7", "2" : "3", "3" : "2", "4" : "f", "5" : "d", "6" : "8", "7" : "9",
"8" : "a", "9" : "6", "a" : "4", "b" : "0", "c" : "5", "d" : "e", "e" : "c", "f" : "1"}
DDT = [[0 for i in range(16)] for j in range(16)]


for i in range(16):
    for j in range(16):
        input_diff=i^j
        temp0=hex(i)
        temp0=temp0[2:]
        v0=int(S_inv[temp0],16)
        temp1=hex(j)
        temp1=temp1[2:]
        v1=int(S_inv[temp1],16)
        output_diff=v0^v1
        DDT[input_diff][output_diff]=DDT[input_diff][output_diff]+1

print("The DDT for the S-box is as follows : ")
print("")
for row in DDT:
    for j in row:
        print(str(j),end=' ')

    print("\n")
    
i=0
for row in DDT:

    count=0
    for j in row:
        if j!=0:
            count+=1
    print(str(i) + " - " + str(count) + " solutions"  )
    i+=1