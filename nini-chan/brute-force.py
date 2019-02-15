import gdb

gdb.execute("b *0x555555669cde")
a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_"
w = ['@']*10
cont = 0

for i in range(10):
    for x in a:            
        w[i]=x
        gdb.execute("r {0}".format("".join(w)))
        for _ in range(i):
            gdb.execute("c")
        d = gdb.execute("x/xb $rax",to_string=True)
        if("0x01" in d):
            cont += 1
            break
print("".join(w))