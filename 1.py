import string
##px = int(raw_input('vvedite px'),2) # int(a,2) = a in bin
px = int('10011', 2)
##gx = int(raw_input('vvedite A'),2) # int(a,2) = a in bin
gx = int('101101101', 2)

def operand(px):
    str_px = bin(px)[2:] #Srez dlja izbavlenija ot 0b stroke
##    str_px = bin(0b11001)[2:]
    operands = []
    ##operands.append('fun_xor')
    while str_px:
        if str_px[0] == '0':
            operands.append('sdvig')
        if str_px[0] == '1':
            operands.append('fun_xor')
        str_px = str_px[1:]
##    operand.reverse()
    return operands
    ##xor sdvig sdvig xor xor

def gx2(gx, px):
    return bin(gx)[2:] + "0"*px.bit_length()

def algoritm(px,gx3,operands):
    trigers = []
    gxx = list(gx3)
    st = list(px.bit_length()* "0")
    print "G(x)*x^k =",gxx
    print "P(x) =",bin(px)[2:]
    while gxx != []:
        i = 0
        print st, " | ", gxx
        head = gxx.pop(0)
##        print st, " | ", gxx
        oppa = st + ["test"]
        oppa.pop(len(oppa)-1)
        while i < len(st) - 1:
            if operands[i] == 'fun_xor': st[i] = str(int(oppa[0]).__xor__(int(oppa[i+1])))
            else: st[i] = str(oppa[i+1])
            i+=1
##            print st, " | "#, gxx
        st[len(st) - 1] = str(int(oppa[0]).__xor__(int(head)))
    print st, " | ", gxx
    print "gx =",gxx,"\noperands = ",operands, "\nR(x)=" , st
    return st

def zakodir_slovo(gx,px):
    gx3 = gx2(gx,px)
    operands = operand(px)
    operands.append(operands.pop(0))
    rx = algoritm(px,gx3,operands)
    print "F(x) =" ,bin(gx)[2:]+string.join(rx,"")
    return bin(gx)[2:]+string.join(rx,"")
fx = zakodir_slovo(gx,px)

def dop_fail(fx, x = None):
    fx = list(fx)
    if x == None: return string.join(fx,"")
    elif fx[-x] == "0":
        fx[-x]="1"
        return string.join(fx,"")
    elif fx[-x] == "1":
        fx[-x] = "0"
        return string.join(fx,"")
    print fx
x=None
d_f = dop_fail(fx,x)
print "fail in", x," =",d_f

def decode_slovo(d_f,px):
    operands = operand(px)
    operands.append(operands.pop(0))
    rx = algoritm(px,d_f,operands)
    print rx
decode_slovo(d_f,px)
