
# Calculation of DDT characteristics for S-box

S_box={"0" : "b", "1" : "f", "2" : "3", "3" : "2", "4" : "a", "5" : "c", "6" : "9", "7" : "1",
"8" : "6", "9" : "7", "a" : "8", "b" : "0", "c" : "e", "d" : "5", "e" : "d", "f" : "4"}
DDT = [[0 for i in range(16)] for j in range(16)]


for i in range(16):
    for j in range(16):
        input_diff=i^j
        temp0=hex(i)
        temp0=temp0[2:]
        v0=int(S_box[temp0],16)
        temp1=hex(j)
        temp1=temp1[2:]
        v1=int(S_box[temp1],16)
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