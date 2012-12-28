# -*- coding: utf-8 -*-

import gtk
import string
import random
import math

def on_calcbutton_pressed(calcbutton, arg1entry, arg2entry, sumlabel,reshlabel1):
##    x1 = int(arg1entry.get_text())
##    x2 = int(arg2entry.get_text())
    gx = int(arg1entry.get_text(),2)
    px = int(arg2entry.get_text(),2)

##    Надо добавить проверку px на соответствие к gx
    fx = zakodir_slovo(gx,px,reshlabel1)
    summ = fx
##    global qaz
    global qaze
    qaze = fx
    sumlabel.set_text(u"F(x):" + unicode(summ))


def on_decode_pressed(calcbutton,arg2entry, sumlabel, summlabel2, fail_x_radio, fail_random_radio, fail_none_radio, failentry, d_flabel,reshlabel2):
    px = int(arg2entry.get_text(), 2)
    if fail_x_radio.get_active():
        print failentry
        x = int(failentry.get_text())
    if fail_random_radio.get_active():
        x = random.randrange(0,len(qaze)-1)
    if fail_none_radio.get_active():
        x = None
    d_f = dop_fail(qaze,x)
    d_flabel.set_text(u"Слово с ошибкой в "+ str(x)+ " разряде " + d_f)
##    print "fail in", x," =",d_f
##    fx = decode_slovo(d_f,px)

    print "fail in", x," =",d_f
    rx = decode_slovo(d_f,px,reshlabel2)
    rx1 = int(string.join(rx,""))
    if rx1  == 0: rx_text = u"отсутствует"
    else: rx_text = u"есть"
    summlabel2.set_text(u"R(x) = " + unicode(rx) + u"следовательно ошибка " + rx_text)

##    summlabel2.set_text(u"Сумма = " + unicode(fx))

def main():
	##px = int(raw_input('vvedite px'),2) # int(a,2) = a in bin
##    px = int('1011 ', 2)
    ##gx = int(raw_input('vvedite A'),2) # int(a,2) = a in bin
##    gx = int('1010010', 2)

    window = gtk.Window()
    window.set_default_size(600,400)
    window.set_title(u"Кодирование циклическим кодом и декодирование с обнаружением ошибки")

    mainbox = gtk.VBox()
    window.add(mainbox)

    arg1box = gtk.HBox()
    mainbox.pack_start(arg1box, expand=False)
    arg2box = gtk.HBox()
    mainbox.pack_start(arg2box, expand=False)



    arg1label = gtk.Label(u"G(x):")
    arg1box.pack_start(arg1label)
    arg1entry = gtk.Entry()
    arg1box.pack_start(arg1entry)

    arg2label = gtk.Label(u"P(x):")
    arg2box.pack_start(arg2label)
    arg2entry = gtk.Entry()
    arg2box.pack_start(arg2entry)
##
##    inccheckbox = gtk.CheckButton(u"Добавить 1")
##    mainbox.pack_start(inccheckbox)


    calcbutton = gtk.Button(u"Закодировать")
    mainbox.pack_start(calcbutton, expand=False)

    reshlabel1 = gtk.Label(u"Тут будет ход решение")
    mainbox.pack_start(reshlabel1, expand=False)

    summlabel = gtk.Label(u"Тут бужет закодированное слово")
    mainbox.pack_start(summlabel, expand=False)

    reshbox = gtk.HBox()
    mainbox.pack_start(reshbox, expand=False)

    d_flabel = gtk.Label(u"Тут будет слово с ошибкой")
    mainbox.pack_start(d_flabel,expand=False)


    fail_random_radio = gtk.RadioButton(None, u"Случайная ошибка")
    mainbox.pack_start(fail_random_radio)

    fail_x_radio = gtk.RadioButton(fail_random_radio, u"Ошибка в x разряде:")
    mainbox.pack_start(fail_x_radio)

    failbox = gtk.VBox()
    mainbox.pack_start(failbox, expand=False)
    failentry = gtk.Entry()
    failbox.pack_start(failentry)

    fail_none_radio = gtk.RadioButton(fail_x_radio, u"Нет ошибки")
    mainbox.pack_start(fail_none_radio)

    reshlabel2 = gtk.Label(u"Тут будет ход решение")
    mainbox.pack_start(reshlabel2, expand=False)

    summlabel2 = gtk.Label(u"Декодированное")
    mainbox.pack_start(summlabel2, expand=False)

    calcbutton2 = gtk.Button(u"Декодировать")
    mainbox.pack_start(calcbutton2, expand=False)

##    string = ("a"*100 + " " + "b"*150 + " " + "c"*100 + " ")*20

    sw = gtk.ScrolledWindow()
    sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
##
##    textbuffer = gtk.TextBuffer()
##    textbuffer.set_text(string)

##    textview = gtk.TextView(textbuffer)
##    textview.set_wrap_mode(gtk.WRAP_WORD)
##    textview.set_editable(False)
##    sw.add(textview)

##    mainbox.pack_start(sw)

    window.connect("destroy", lambda _: gtk.main_quit())
    calcbutton.connect("clicked", on_calcbutton_pressed, arg1entry, arg2entry, summlabel, reshlabel1)


    window.connect("destroy", lambda _: gtk.main_quit())
    calcbutton2.connect("clicked", on_decode_pressed,arg2entry, summlabel, summlabel2, fail_x_radio, fail_random_radio, fail_none_radio, failentry,d_flabel, reshlabel2)

    window.show_all()
    gtk.main()

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

def algoritm(px,gx3,operands,reshlabel):
    trigers = []
    gxx = list(gx3)
    st = list((px.bit_length()-1)* "0")
    print "G(x)*x^k =",gxx
    print "P(x) =",bin(px)[2:]
    resh = "G(x)*x^k ="+str(gxx) + "\n" + "P(x) =" + str(bin(px)[2:])+"\n"
    while gxx != []:
        i = 0
        print st, " | ", gxx
        resh = resh + str(st) + " | "+ str(gxx) + "\n"
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
    resh = resh + str(st) + " | "+ str(gxx)+"\n"
    print "gx =", str(gxx),"\noperands = ",str(operands), "\nR(x)=" , str(st)
    resh = resh + "gx ="+str(gxx)+"\noperands = "+ str(operands) + "\nR(x)=" + str(st)
    print resh
    reshlabel.set_text(resh)
    return st

def zakodir_slovo(gx,px,reshlabel):
##    k >= log(m+k+1,2)
    m = gx.bit_length()
    k = 0
    while math.log(m+k+1,2) > k:
        k+=1
    if px.bit_length() < k:
        print u"Данное действие некорректно, так как наивысшая степень P(x)=", px.bit_length(), u"меньше k =", k
        return u"Данное действие некорректно, так как наивысшая степень P(x)="+ unicode(px.bit_length()) + u"меньше k =" + unicode(k)
##    if px.bit_length() > k:
##        print u"Данное действие нерационально, так как наивысшая степень P(x)=", px.bit_length(), u",больше k =", k
##        return u"Данное действие нерационально, так как наивысшая степень P(x)="+ unicode(px.bit_length()) + u"больше k =" + unicode(k)

    gx3 = gx2(gx,px)
    operands = operand(px)
##    operands.append(operands.pop(0))
    operands.pop(0)
    print operands
    rx = algoritm(px,gx3,operands,reshlabel)
    print "F(x) =" ,bin(gx)[2:]+string.join(rx,"")
    return bin(gx)[2:]+string.join(rx,"")

def dop_fail(fx, x):
    fx = list(fx)
    if x == None:

        return string.join(fx,"")
    elif fx[-x] == "0":
        fx[-x]="1"

        return string.join(fx,"")
    elif fx[-x] == "1":
        fx[-x] = "0"
        return string.join(fx,"")

def decode_slovo(d_f,px,reshlabel2):
    operands = operand(px)
    operands.pop(0)
    rx = algoritm(px,d_f,operands,reshlabel2)
    return rx

if __name__ == "__main__":
	main()
