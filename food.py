from tkinter import*
import random
import time;
import datetime
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo

root=Tk()
root.geometry("1350x750+0+0")
root.title("Fast Food Restaurant")

Tops = Frame (root, width = 1350 , height = 100, bd =6 , relief ="raise" , bg="salmon")
Tops.pack(side=TOP)
iblTitle = Label(Tops, font=('verdana', 40, 'bold'), text="\tʚFAST FOOD RESTARURANTɞ\t\t\t", bg="bisque")
iblTitle.grid(row =0, column=0)  

BottomMainFrame =Frame (root, width = 1350 , height = 650, bd = 12 , relief ="raise" , bg="salmon")
BottomMainFrame.pack(side=BOTTOM)

f1= Frame (BottomMainFrame, width = 450, height = 650, bd = 12, relief ="raise" , bg="salmon")
f1.pack(side=LEFT)
f2= Frame (BottomMainFrame, width = 450, height = 650, bd = 12, relief ="raise" , bg="salmon")
f2.pack(side=LEFT)
f2TOP= Frame (f2, width = 450, height = 350, bd = 4, relief ="raise" , bg="salmon")
f2TOP.pack(side=TOP)
f2BOTTOM= Frame (f2, width = 450, height = 300, bd = 4, relief ="raise" , bg="salmon")
f2BOTTOM.pack(side=BOTTOM)

f3= Frame (BottomMainFrame, width = 450, height = 650, bd = 12, relief ="raise", bg="salmon")
f3.pack(side=RIGHT)

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var14=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=StringVar()
var23=IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set("")
var23.set(0)

varFries = StringVar()
varSalad=StringVar()
varHamburger=StringVar()
varOnionrings=StringVar()
varChickenSalad=StringVar()
varFishSandwic=StringVar()
varCheeseSandwich=StringVar()
varChickenSandwich=StringVar()

varIceCream=StringVar()
varWaffle=StringVar()
varPancakeSyrup=StringVar()
varBananaStick=StringVar()
varChocholateMuffin=StringVar()

varLemonTea=StringVar()
varCola=StringVar()
varCoffee=StringVar()
varOrange=StringVar()
varCaramelFrappe=StringVar()

varOreoShakes=StringVar()
varChocolateShake=StringVar()
varStrawberryShake=StringVar()

varChange=StringVar()
varSubTotal=StringVar()
varTotal=StringVar()
varVat=StringVar()
varTax=StringVar()
varPayment=IntVar()

varFries.set("0")
varSalad.set("0")
varHamburger.set("0")
varOnionrings.set("0")
varChickenSalad.set("0")
varFishSandwic.set("0")
varCheeseSandwich.set("0")
varChickenSandwich.set("0")
varTotal.set("0")
varPayment.set("")

varIceCream.set("0")
varWaffle.set("0")
varPancakeSyrup.set("0")
varBananaStick.set("0")
varChocholateMuffin.set("0")

varLemonTea.set("0")
varCola.set("0")
varCoffee.set("0")
varOrange.set("0")
varCaramelFrappe.set("0")
varOreoShakes.set("0")
varChocolateShake.set("0")
varStrawberryShake.set("0")

varVat.set("")
varTax.set("0")
varTotal.set("0")
varChange.set("0")
varSubTotal.set("0")

def iExit():
    qExit = messagebox.askyesno("Fast Food", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return
    
def Reset():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set("")
    var23.set(0)

    varFries.set("0")
    varSalad.set("0")
    varHamburger.set("0")
    varOnionrings.set("0")
    varChickenSalad.set("0")
    varFishSandwic.set("0")
    varCheeseSandwich.set("0")
    varChickenSandwich.set("0")

    varIceCream.set("0")
    varWaffle.set("0")
    varPancakeSyrup.set("0")
    varBananaStick.set("0")
    varChocholateMuffin.set("0")

    varLemonTea.set("0")
    varCola.set("0")
    varCoffee.set("0")
    varOrange.set("0")
    varCaramelFrappe.set("0")
    varOreoShakes.set("0")
    varChocolateShake.set("0")
    varStrawberryShake.set("0")

    varVat.set("")
    varTax.set("0")
    varTotal.set("0")
    varChange.set("")
    varSubTotal.set("0")
    varPayment.set("0")

    txtFries.configure(state=DISABLED)
    txtSalad.configure(state=DISABLED)
    txtHamburger.configure(state=DISABLED)
    txtOnionRings.configure(state=DISABLED)
    txtChickenSalad.configure(state=DISABLED)
    txtFishSandwich.configure(state=DISABLED)
    txtCheeseSandwich.configure(state=DISABLED)
    txtChickenSandwich.configure(state=DISABLED)
    txtIceCream.configure(state=DISABLED)
    txtWaffle.configure(state=DISABLED)
    txtPancakeSyrup.configure(state=DISABLED)
    txtBananaStick.configure(state=DISABLED)
    txtChocholateMuffin.configure(state=DISABLED)
    txtLemonTea.configure(state=DISABLED)
    txtCola.configure(state=DISABLED)
    txtCoffee.configure(state=DISABLED)
    txtOrange.configure(state=DISABLED)
    txtCaramelFrappe.configure(state=DISABLED)
    txtOreoShakes.configure(state=DISABLED)
    txtChocolateShake.configure(state=DISABLED)
    txtStrawberryShake.configure(state=DISABLED)
    #txtPayment.configure(state=DISABLED)
    txtChange.configure(state=DISABLED)
    txtTax.configure(state=DISABLED)
    txtSubTotal.configure(state=DISABLED)
    txtTotal.configure(state=DISABLED)
    var8.get() == 0

def chkFries():
    if(var1.get() == 1):
        txtFries.configure(state=NORMAL)
        varFries.set("")
    elif (var1.get() == 0):
        txtFries.configure(state=DISABLED)
        varFries.set("0")

def chkSalad():
    if(var2.get() == 1):
        txtSalad.configure(state=NORMAL)
        varSalad.set("")
    elif (var2.get() == 0):
        txtSalad.configure(state=DISABLED)
        varSalad.set("0")

def chkHamburger():
    if(var3.get() == 1):
        txtHamburger.configure(state=NORMAL)
        varHamburger.set("")
    elif (var3.get() == 0):
        txtHamburger.configure(state=DISABLED)
        varHamburger.set("0")

def chkOnionRings():
    if(var4.get() == 1):
        txtOnionRings.configure(state=NORMAL)
        varOnionrings.set("")
    elif (var4.get() == 0):
        txtOnionRings.configure(state=DISABLED)
        varOnionrings.set("0")

def chkChickenSalad():
    if(var5.get() == 1):
        txtChickenSalad.configure(state=NORMAL)
        varChickenSalad.set("")
    elif (var5.get() == 0):
        txtChickenSalad.configure(state=DISABLED)
        varChickenSalad.set("0")

def chkFishSandwic():
    if(var6.get() == 1):
        txtFishSandwich.configure(state=NORMAL)
        varFishSandwic.set("")
    elif (var6.get() == 0):
        txtFishSandwich.configure(state=DISABLED)
        varFishSandwic.set("0")

def chkCheeseSandwich():
    if(var7.get() == 1):
        txtCheeseSandwich.configure(state=NORMAL)
        varCheeseSandwich.set("")
    elif (var7.get() == 0):
        txtCheeseSandwich.configure(state=DISABLED)
        varCheeseSandwich.set("0")

def chkChickenSandwich():
    if(var8.get() == 1):
        txtChickenSandwich.configure(state=NORMAL)
        varChickenSandwich.set("")
    elif (var8.get() == 0):
        txtChickenSandwich.configure(state=DISABLED)
        varChickenSandwich.set("0")

def chkIceCream():
    if(var9.get() == 1):
        txtIceCream.configure(state=NORMAL)
        varIceCream.set("")
    elif (var9.get() == 0):
        txtIceCream.configure(state=DISABLED)
        varIceCream.set("0")

def chkWaffle():
    if(var10.get() == 1):
        txtWaffle.configure(state=NORMAL)
        varWaffle.set("")
    elif (var10.get() == 0):
        txtWaffle.configure(state=DISABLED)
        varWaffle.set("0")

def chkPancakeSyrup():
    if(var11.get() == 1):
        txtPancakeSyrup.configure(state=NORMAL)
        varPancakeSyrup.set("")
    elif (var11.get() == 0):
        txtPancakeSyrup.configure(state=DISABLED)
        varPancakeSyrup.set("0")

def chkBananaStick():
    if(var12.get() == 1):
        txtBananaStick.configure(state=NORMAL)
        varBananaStick.set("")
    elif (var12.get() == 0):
        txtBananaStick.configure(state=DISABLED)
        varBananaStick.set("0")

def chkChocolateMuffin():
    if(var13.get() == 1):
        txtChocholateMuffin.configure(state=NORMAL)
        varChocholateMuffin.set("")
    elif (var13.get() == 0):
        txtChocholateMuffin.configure(state=DISABLED)
        varChocholateMuffin.set("0")

def chkLemonTea():
    if(var14.get() == 1):
        txtLemonTea.configure(state=NORMAL)
        varLemonTea.set("")
    elif (var14.get() == 0):
        txtLemonTea.configure(state=DISABLED)
        varLemonTea.set("0")

def chkCola():
    if(var15.get() == 1):
        txtCola.configure(state=NORMAL)
        varCola.set("")
    elif (var15.get() == 0):
        txtCola.configure(state=DISABLED)
        varCola.set("0")

def chkCoffee():
    if(var16.get() == 1):
        txtCoffee.configure(state=NORMAL)
        varCoffee.set("")
    elif (var16.get() == 0):
        txtCoffee.configure(state=DISABLED)
        varCoffee.set("0")

def chkOrange():
    if(var17.get() == 1):
        txtOrange.configure(state=NORMAL)
        varOrange.set("")
    elif (var17.get() == 0):
        txtOrange.configure(state=DISABLED)
        varOrange.set("0")

def chkCaramelFrappe():
    if(var18.get() == 1):
        txtCaramelFrappe.configure(state=NORMAL)
        varCaramelFrappe.set("")
    elif (var18.get() == 0):
        txtCaramelFrappe.configure(state=DISABLED)
        varCaramelFrappe.set("0")

def chkOreoShakes():
    if(var19.get() == 1):
        txtOreoShakes.configure(state=NORMAL)
        varOreoShakes.set("")
    elif (var19.get() == 0):
        txtOreoShakes.configure(state=DISABLED)
        varOreoShakes.set("0")

def chkChocolateShake():
    if(var20.get() == 1):
        txtChocolateShake.configure(state=NORMAL)
        varChocolateShake.set("")
    elif (var20.get() == 0):
        txtChocolateShake.configure(state=DISABLED)
        varChocolateShake.set("0")

def chkStrawberryShake():
    if(var21.get() == 1):
        txtStrawberryShake.configure(state=NORMAL)
        varStrawberryShake.set("")
    elif (var21.get() == 0):
        txtStrawberryShake.configure(state=DISABLED)
        varStrawberryShake.set("0")

def costofmeal():
    meal1 = float(varFries.get())
    meal2 = float(varSalad.get())
    meal3 = float(varHamburger.get())
    meal4 = float(varOnionrings.get())
    meal5 = float(varChickenSalad.get())
    meal6 = float(varFishSandwic.get())
    meal7 = float(varCheeseSandwich.get())
    meal8 = float(varChickenSandwich.get())
    meal9 = float(varIceCream.get())
    meal10 = float(varWaffle.get())
    meal11 = float(varPancakeSyrup.get())
    meal12 = float(varBananaStick.get())
    meal13 = float(varChocholateMuffin.get())
    meal14 = float(varLemonTea.get())
    meal15 = float(varCola.get())
    meal16 = float(varCoffee.get())
    meal17 = float(varOrange.get())
    meal18 = float(varCaramelFrappe.get())
    meal19 = float(varOreoShakes.get())
    meal20 = float(varChocolateShake.get())
    meal21 = float(varStrawberryShake.get())

    iTotal1 = ((meal1 * 4.50) + (meal2 * 2.50) + (meal3 * 4.00) + (meal4 * 6.80))
    iTotal2 = ((meal5 * 3.50) + (meal6 * 6.50) + (meal7 * 7.50) + (meal8 * 8.80))
    iTotal3 = ((meal9 * 4.50) + (meal10 * 3.50) + (meal11 * 6.00) + (meal12 * 7.40))
    iTotal4 = ((meal13 * 5.50) + (meal14 * 2.50) + (meal15 * 1.50) + (meal16 * 3.20))
    iTotal5 = ((meal17 * 3.20) + (meal18 * 5.80) + (meal19 * 8.00) + (meal20 * 6.50) + (meal21 * 6.90))

    if (var22.get() == "Cash"):
        iChange = float(varPayment.get())
        iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
        iTax = (iCost * 3.4) / 100
        iTaxq = "RM", str('%.2f' % (iTax))
        varTax.set(iTaxq)

        iCostq = "RM", str('%.2f' % (iCost))
        varSubTotal.set(iCostq)
        iTotalq = "RM", str('%.2f' % ((iCost + iTax)))
        varTotal.set(iTotalq)
        cChange = (iChange - (iCost + iTax))
        cChangeq = "RM", str('%.2f' % (cChange))
        varChange.set(cChangeq)
    elif (var22.get() == "Master Card" or "Visa Card" or "Debit Card"):
        varPayment.set("")
        iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
        iTax = (iCost * 3.4) / 100
        iTaxq = "RM", str('%.2f' % (iTax))
        varTax.set(iTaxq)
        iCostq = "RM", str('%.2f' % (iCost))
        varSubTotal.set(iCostq)
        iTotalq = "RM", str('%.2f' % ((iCost + iTax)))
        varTotal.set(iTotalq)
        varChange.set("")

#FAST MEAL

iblMeal = Label(f1, font=('arial', 18, 'bold'), text="\tFAST MEAL\t\n" , bg="salmon")
iblMeal.grid(row =0, column=0)

Fries = Checkbutton(f1, text="Fries\t\tRM4.50",bg="salmon",  variable=var1, onvalue=1, offvalue=0,
                    font=('arial,', 18, 'bold'), command=chkFries). grid(row =1, column=0, sticky=W)
txtFries = Entry(f1, font=('arial', 18, 'bold'), textvariable =varFries, width = 6, justify='right' ,state =DISABLED)
txtFries. grid(row =1, column=1)

Salad = Checkbutton(f1, text="Salad\t\tRM2.50",bg="salmon", variable=var2, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkSalad). grid(row =2, column=0, sticky=W)
txtSalad = Entry(f1, font=('Arial', 18, 'bold'), textvariable =varSalad, width = 6, justify='right', state =DISABLED)
txtSalad. grid(row =2, column=1)

Hamburger = Checkbutton(f1, text="Hamburger\tRM4.00",bg="salmon" , variable=var3, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkHamburger). grid(row =3, column=0, sticky=W)
txtHamburger = Entry(f1, font=('Arial', 18, 'bold'), textvariable =varHamburger, width = 6, justify='right' , state =DISABLED)
txtHamburger. grid(row =3, column=1)

OnionRings = Checkbutton(f1, text="OnionRings\tRM6.80",bg="salmon" , variable=var4, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'),command=chkOnionRings). grid(row =4, column=0, sticky=W)
txtOnionRings = Entry(f1, font=('Arial', 18, 'bold'), textvariable =varOnionrings, width = 6,justify='right' , state =DISABLED)
txtOnionRings. grid(row =4, column=1)

ChickenSalad = Checkbutton(f1, text="Chicken Salad\tRM3.50",bg="salmon", variable=var5, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkChickenSalad). grid(row =5, column=0, sticky=W)
txtChickenSalad = Entry(f1, font=('Arial', 18, 'bold'), textvariable =varChickenSalad, width = 6, justify='right' , state =DISABLED)
txtChickenSalad. grid(row =5, column=1)

iblSandwich = Label(f1, font=('arial', 18, 'bold'), bg="salmon", text="\nSANDWICH\n")
iblSandwich.grid(row=6, column=0)

FishSandwic = Checkbutton(f1, text="Fish Sandwich\t RM6.50", bg="salmon", variable=var6, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkFishSandwic). grid(row =7, column=0, sticky=W)
txtFishSandwich = Entry(f1, font=('Arial', 18, 'bold'), textvariable =varFishSandwic, width = 6, justify='right' , state =DISABLED)
txtFishSandwich. grid(row =7, column=1)

CheeseSandwich = Checkbutton(f1, text="Cheese Sandwich\t RM7.50", bg="salmon", variable=var7, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkCheeseSandwich). grid(row =8, column=0, sticky=W)
txtCheeseSandwich = Entry(f1, font=('Arial', 18, 'bold'), textvariable =varCheeseSandwich, width = 6, justify='right' , state =DISABLED)
txtCheeseSandwich. grid(row =8, column=1)

ChickenSandwich = Checkbutton(f1, text="Chicken Sandwich RM8.80", bg="salmon", variable=var8, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkChickenSandwich). grid(row =9, column=0, sticky=W)
txtChickenSandwich = Entry(f1, font=('Arial', 18, 'bold'), textvariable =varChickenSandwich, width = 6, justify='right' , state =DISABLED)
txtChickenSandwich. grid(row =9, column=1)

iblspace =Label(f1, text="\n\n\n\n\n\n\n\n\n\n", bg="salmon")
iblspace.grid(row=10, column=0)

#DESSERTS

iblMeal = Label(f2TOP, font=('arial', 18, 'bold'), bg="salmon", text="DESSERT\n")
iblMeal.grid(row =0, column=0)

IceCream = Checkbutton(f2TOP, text="Ice Cream\t  RM4.50", bg="salmon", variable=var9, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkIceCream). grid(row =1, column=0, sticky=W)
txtIceCream = Entry(f2TOP, font=('Arial', 18, 'bold'), textvariable =varIceCream, width = 6, justify='right' , state =DISABLED)
txtIceCream. grid(row =1, column=1)

Waffle = Checkbutton(f2TOP, text="Waffle\t\t  RM3.50", bg="salmon", variable=var10, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkWaffle). grid(row =2, column=0, sticky=W)
txtWaffle = Entry(f2TOP, font=('Arial', 18, 'bold'), textvariable =varWaffle, width = 6, justify='right', state =DISABLED)
txtWaffle. grid(row =2, column=1)

PancakeSyrup = Checkbutton(f2TOP, text="Pancake Syrup\t  RM6.00", bg="salmon" , variable=var11, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkPancakeSyrup). grid(row =3, column=0, sticky=W)
txtPancakeSyrup = Entry(f2TOP, font=('Arial', 18, 'bold'), textvariable =varPancakeSyrup, width = 6, justify='right', state =DISABLED)
txtPancakeSyrup. grid(row =3, column=1)

BananaStick = Checkbutton(f2TOP, text="Banana Stick\t  RM7.40", bg="salmon", variable=var12, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkBananaStick). grid(row =4, column=0, sticky=W)
txtBananaStick = Entry(f2TOP, font=('Arial', 18, 'bold'), textvariable =varBananaStick, width = 6, justify='right', state =DISABLED)
txtBananaStick. grid(row =4, column=1)

ChocholateMuffin = Checkbutton(f2TOP, text="Chocholate Muffin  RM5.50", bg="salmon", variable=var13, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkChocolateMuffin). grid(row =5, column=0, sticky=W)
txtChocholateMuffin = Entry(f2TOP, font=('Arial', 18, 'bold'), textvariable =varChocholateMuffin, width = 6, justify='right', state =DISABLED)
txtChocholateMuffin. grid(row =5, column=1)

#DRINK

iblMeal = Label(f3, font=('arial', 18, 'bold'), bg="salmon", text="DRINKS\n")
iblMeal.grid(row=0, column=0)

LemonTea = Checkbutton(f3, text="Lemon Tea\tRM2.50", bg="salmon", variable=var14, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'),command=chkLemonTea). grid(row =1, column=0, sticky=W)
txtLemonTea = Entry(f3, font=('Arial', 18, 'bold'), textvariable =varLemonTea, width = 6, justify='right', state =DISABLED)
txtLemonTea. grid(row =1, column=1)

Cola = Checkbutton(f3, text="Cola\t\tRM1.50", bg="salmon", variable=var15, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkCola). grid(row =2, column=0, sticky=W)
txtCola = Entry(f3, font=('Arial', 18, 'bold'), textvariable =varCola, width = 6, justify='right', state =DISABLED)
txtCola. grid(row =2, column=1)

Coffee = Checkbutton(f3, text="Coffee\t\tRM3.20", bg="salmon", variable=var16, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkCoffee). grid(row =3, column=0, sticky=W)
txtCoffee = Entry(f3, font=('Arial', 18, 'bold'), textvariable =varCoffee, width = 6, justify='right', state =DISABLED)
txtCoffee. grid(row =3, column=1)

Orange = Checkbutton(f3, text="Orange\t\tRM3.20", bg="salmon", variable=var17, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkOrange). grid(row =4, column=0, sticky=W)
txtOrange = Entry(f3, font=('Arial', 18, 'bold'), textvariable =varOrange, width = 6, justify='right', state =DISABLED)
txtOrange. grid(row =4, column=1)

CaramelFrappe = Checkbutton(f3, text="Caramel Frappe\tRM5.80", bg="salmon", variable=var18, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkCaramelFrappe). grid(row =5, column=0, sticky=W)
txtCaramelFrappe = Entry(f3, font=('Arial', 18, 'bold'), textvariable =varCaramelFrappe, width = 6, justify='right', state =DISABLED)
txtCaramelFrappe. grid(row =5, column=1)

iblShakes = Label(f3, font=('arial', 18, 'bold'), bg="salmon", text="\nSHAKES\n")
iblShakes.grid(row=6, column=0)

OreoShakes = Checkbutton(f3, text="Oreo Shakes\tRM8.00", bg="salmon", variable=var19, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkOreoShakes). grid(row =7, column=0, sticky=W)
txtOreoShakes = Entry(f3, font=('Arial', 18, 'bold'), textvariable =varOreoShakes, width = 6, justify='right', state =DISABLED)
txtOreoShakes. grid(row =7, column=1)

ChocolateShake = Checkbutton(f3, text="ChocolateShake\tRM6.50", bg="salmon", variable=var20, onvalue=1, offvalue=0,
                    font=('Arial',  18, 'bold'), command=chkChocolateShake). grid(row =8, column=0, sticky=W)
txtChocolateShake = Entry(f3, font=('Arial', 18, 'bold'), textvariable =varChocolateShake, width = 6, justify='right' , state =DISABLED)
txtChocolateShake. grid(row =8, column=1)

StrawberryShake = Checkbutton(f3, text="Strawberry Shake RM6.90", bg="salmon", variable=var21, onvalue=1, offvalue=0,
                    font=('Arial', 18, 'bold'), command=chkStrawberryShake). grid(row =9, column=0, sticky=W)
txtStrawberryShake = Entry(f3, font=('Arial', 18, 'bold'), textvariable =varStrawberryShake, width = 6, justify='right', state =DISABLED)
txtStrawberryShake. grid(row =9, column=1)

iblspace =Label(f3, text="\n\n\n\n\n\n\n\n\n\n", bg="salmon")
iblspace.grid(row=10, column=0) 

iblPaymentMethod = Label(f2BOTTOM, font=('arial', 16, 'bold'), text="PAYMENT METHOD", bg="salmon", bd=10, width=16, anchor='w')
iblPaymentMethod.grid(row =0, column=0)

iblChange = Label(f2BOTTOM, font=('arial', 14, 'bold'), text="CHANGE", bg="salmon", bd=10, anchor='w')
iblChange.grid(row=0, column=1)
txtChange = Entry(f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varChange, width=8, justify='right', state=DISABLED)
txtChange.grid(row=0, column=2)

cmbPaymentMethod =ttk.Combobox(f2BOTTOM, textvariable=var22, state='readonly', font=('arial', 10, 'bold'), width=20)
cmbPaymentMethod['value']=('Cash', 'Master Card', 'Visa Card', 'Debit Card')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row=1, column=0)

iblTax = Label(f2BOTTOM, font=('arial', 14, 'bold'), text="TAX", bg="salmon", bd=10, anchor='w')
iblTax.grid(row=1, column=1)
txtTax = Entry(f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varTax, width=8, justify='right', state=DISABLED)
txtTax.grid(row=1, column=2)

txtPayment = Entry(f2BOTTOM, font=('arial', 18, 'bold'),textvariable=varPayment, width=6, justify='right') #, state=DISABLED)
txtPayment.grid(row=2, column=0)
iblSubTotal = Label(f2BOTTOM, font=('arial', 14, 'bold'), text="SUB.T", bg="salmon", bd=10, width=7, anchor='w')
iblSubTotal.grid(row=2, column=1)
txtSubTotal = Entry(f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varSubTotal, width=8, justify='right', state=DISABLED)
txtSubTotal.grid(row=2, column=2)

iblTotal = Label(f2BOTTOM, font=('arial', 14, 'bold'), text="TOTAL", bg="salmon", bd=10, width=6, anchor='w')
iblTotal.grid(row=3, column=1)
txtTotal = Entry(f2BOTTOM, font=('arial', 18, 'bold'), textvariable=varTotal, width=8, justify='right', state=DISABLED)
txtTotal.grid(row=3, column=2)

btnTotal = Button(f2BOTTOM, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5, text="TOTAL", command=costofmeal, bg="bisque"). grid(row=4, column=0)

btnReset = Button(f2BOTTOM, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5, text="RESET", command=Reset, bg="bisque"). grid(row=4, column=1)

btnExit = Button(f2BOTTOM, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5, text="EXIT" , bg="bisque" , command=lambda: iExit()). grid(row=4, column=2)

iblspace =Label(f2BOTTOM, text="\n\n\n\n\n\n\n\n\n\n", bg="salmon")
iblspace.grid(row=5, column=0)

root.mainloop()