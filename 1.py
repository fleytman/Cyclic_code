##px = int(raw_input('vvedite px'),2) # int(a,2) = a in bin
px = int('10011', 2)
##px = int(raw_input('vvedite A'),2) # int(a,2) = a in bin
gx = int('101101101', 2)

def operands(px):
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
operands = operands(px)
operands.append(operands.pop(0))

def gx2(gx, px):
    return bin(gx) + "0"*px.bit_length()
gx2 = gx2(gx,px)

def algoritm(px,gx2):
    trigers = []
    gx = list(gx2[2:])
    st = list(px.bit_length()* "0")
    while gx != []:
        i = 0
        head = gx.pop(0)

        print st, "  ", gx
        while i < len(st) - 1:
            oppa = st
            if operands[i] == 'fun_xor': st[i] = str(int(st[i]).__xor__(int(oppa[i+1])))
            else: st[i] = str(oppa[i+1])
            i+=1
        print st, "  ", gx
        st[len(st) - 1] = str(int(oppa[0]).__xor__(int(head)))
    print "gx =",gx,"\noperands = ",operands, "\nst=" , st
    print operands
##    while bin(gx2):

algoritm(px,gx2)
