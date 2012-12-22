import string
##px = int(raw_input('vvedite px'),2) # int(a,2) = a in bin
px = int('10011', 2)
##gx = int(raw_input('vvedite A'),2) # int(a,2) = a in bin
gx = int('101101101', 2)

def operand(px):
    str_px = bin(px)[2:] #Srez dlja izbavlenija ot 0b stroke
##    str_px = bin(0b11001)[2:]
    operand = []
    ##operand.append('fun_xor')
    while str_px:
        if str_px[0] == '0':
            operand.append('sdvig')
        if str_px[0] == '1':
            operand.append('fun_xor')
        str_px = str_px[1:]
##    operand.reverse()
    return operand
    ##xor sdvig sdvig xor xor

def gx2(gx, px):
    return bin(gx) + "0"*px.bit_length()

def algoritm(px,gx2):
    trigers = []
    gx = list(gx2[2:])
    st = list(px.bit_length()* "0")
    print "G(x)*x^k =",gx
    print "P(x) =",bin(px)[2:]
    while gx != []:
        i = 0
        print st, " | ", gx
        head = gx.pop(0)
##        print st, " | ", gx
        oppa = st + ["test"]
        oppa.pop(len(oppa)-1)
        while i < len(st) - 1:
            if operands[i] == 'fun_xor': st[i] = str(int(oppa[0]).__xor__(int(oppa[i+1])))
            else: st[i] = str(oppa[i+1])
            i+=1
##            print st, " | "#, gx
        st[len(st) - 1] = str(int(oppa[0]).__xor__(int(head)))
    print st, " | ", gx
    print "gx =",gx,"\noperands = ",operands, "\nR(x)=" , st
    return st

def zakodir_slovo(gx,px):
    gx3 = gx2(gx,px)
	operands = operand(px)
	operands.append(operands.pop(0))
	rx = algoritm(px,gx3)
	print "F(x) =" ,bin(gx)[2:]+string.join(rx,"")

zakodir_slovo(gx,px)


