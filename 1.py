##px = int(raw_input('vvedite px'),2) # int(a,2) = a in bin
px = int('11001', 2)
##px = int(raw_input('vvedite A'),2) # int(a,2) = a in bin
gx = int('101010110', 2)

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
    operand.reverse()
    return operand
    ##xor sdvig sdvig xor xor
operands = operands(px)

def gx2(gx, px):
    return bin(gx) + "0"*px.bit_length()
gx2 = gx2(gx,px)

def algoritm(px):
    st = []
    ##itrigers = lamda px.bit_length(), st.append('0')
    print "gx2 =",gx2,"\noperands = ",operands##, "\ntrigers=" , trigers
    ost = []
    ##print trigers[1] 
##    while bin(gx2):

algoritm(px)
