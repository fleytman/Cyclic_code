px = int(raw_input(),2) # int(a,2) = a in bin
str_px = bin(px)[2:] #Srez dlja izbavlenija ot 0b stroke
operand = []
operand.append('fun_xor')
while str_px[1:]:
    if str_px[0] == '0':
        operand.append('sdvig')
    if str_px[0] == '1':
        operand.append('fun_xor')
    str_px = str_px[1:]
