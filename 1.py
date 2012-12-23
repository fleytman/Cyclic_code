# -*- coding: utf-8 -*-

import string
import gtk
##
##def on_calcbutton_pressed(calcbutton, arg1entry, arg2entry, sumlabel, icb):
####    x1 = int(arg1entry.get_text())
####    x2 = int(arg2entry.get_text())
##    px = int(arg1entry.get_text(),2)
##    gx = int(arg2entry.get_text(),2)
##    summ = px + gx
##    if icb.get_active():
##      summ += 1
##    sumlabel.set_text(u"Сумма = " + unicode(summ))

def main():
    ##px = int(raw_input('vvedite px'),2) # int(a,2) = a in bin
    px = int('10011', 2)
    ##gx = int(raw_input('vvedite A'),2) # int(a,2) = a in bin
    gx = int('101101101', 2)
    fx = zakodir_slovo(gx,px)
    x=None
    d_f = dop_fail(fx,x)
    print "fail in", x," =",d_f

    decode_slovo(d_f,px)
##    window = gtk.Window()
##    window.set_default_size(300,100)
##    window.set_title(u"MatCAD 100500")
##
##    mainbox = gtk.VBox()
##    window.add(mainbox)
##
##    arg1box = gtk.HBox()
##    mainbox.pack_start(arg1box, expand=False)
##    arg2box = gtk.HBox()
##    mainbox.pack_start(arg2box, expand=False)
##
##    arg1label = gtk.Label(u"Слагаемое 1:")
##    arg1box.pack_start(arg1label)
##    arg1entry = gtk.Entry()
##    arg1box.pack_start(arg1entry)
##
##    arg2label = gtk.Label(u"Слагаемое 2:")
##    arg2box.pack_start(arg2label)
##    arg2entry = gtk.Entry()
##    arg2box.pack_start(arg2entry)
##
##    inccheckbox = gtk.CheckButton(u"Добавить 1")
##    mainbox.pack_start(inccheckbox)
##
##    fail_x_radio = gtk.RadioButton(None, u"Ошик в разряде:")
##    mainbox.pack_start(fail_x_radio)
##
##    fail_random_radio = gtk.RadioButton(fail_x_radio, u"Случайная ошибка")
##    mainbox.pack_start(fail_random_radio)
##
##    fail_none_radio = gtk.RadioButton(fail_random_radio, u"Нет ошибки")
##    mainbox.pack_start(fail_none_radio)
##
##    calcbutton = gtk.Button(u"Посчитать")
##    mainbox.pack_start(calcbutton, expand=False)
##
##    summlabel = gtk.Label(u"Тут будет сумма")
##    mainbox.pack_start(summlabel, expand=False)
##
##    window.connect("destroy", lambda _: gtk.main_quit())
##    calcbutton.connect("clicked", on_calcbutton_pressed, arg1entry, arg2entry, summlabel, inccheckbox)
##
##    window.show_all()
##    gtk.main()

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
    print "test op", operands
    operands.pop()
    print "test2 op", operands
    return operands
    ##xor sdvig sdvig xor xor

def gx2(gx, px):
    return bin(gx)[2:] + "0"*(px.bit_length()-1)

def algoritm(px,gx3,operands):
    trigers = []
    gxx = list(gx3)
    st = list((px.bit_length()-1)* "0")
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
##    operands.append(operands.pop(0))
    operands.pop(0)
    print operands
    rx = algoritm(px,gx3,operands)
    print "F(x) =" ,bin(gx)[2:]+string.join(rx,"")
    return bin(gx)[2:]+string.join(rx,"")

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

def decode_slovo(d_f,px):
    operands = operand(px)
##    operands.append(operands.pop(0))
    operands.pop(0)
    rx = algoritm(px,d_f,operands)
    print rx

if __name__ == "__main__":
	main()
