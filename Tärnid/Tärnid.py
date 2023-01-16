from math import *
from random import *

#Ü6 1
print()
print("Ülesanne 6 1")
print()
for i in range(0,5):
    print("* "*5)
print()
for i in range(0,10):
    print("* "*i)
print()
for i in range(0,10):
    print("* "*(10-i))
print()

#Ü6 2
#print()
#print("Ülesanne 6 2")
#x=0
#while True:
#    if x<5:
#        print("* "*5)
#        x+=1
#    else:
#        break
#x=0
#print()
#while True:
#    if x<10:
#        print("* "*x)
#        x+=1
#    else:
#        break
#x=11
#print()
#while True:
#    if x>0:
#        print("* "*(x-1))
#        x-=1
#    break

#Ü6 3
#print()
#print("Ülesanne 6 3")
#x=0
#print()
#while x<5:
#    print("* "*5)
#    x+=1
#x=0
#print()
#while x<10:
#    print("* "*x)
#    x+=1
#x=11
#print()
#while x>0:
#    print("* "*(x-1))
#    x-=1

#Ü0 1
print()
print("Ülesanne 0 1")
print()
kujund=input("Vali kujund (ristkülik, rööpkülik, kolmnurk, ring) ").lower()
kujundid=["ristkülik", "rööpkülik", "kolmnurk", "ring"]
print(kujundid[3]) # ==> ring
while kujund not in kujundid:
    kujund=input("Palun kirjutage õige kujund! ").lower()
tegevus=input("Mis sa otsi? (pindala, perimeeter) ").lower()
while tegevus not in ["pindala","perimeeter"]:
    tegevus=input("Palun kirjuta õige tegevus! ").lower()
if kujund=="ristkülik":
    a=input("Kirjuta 1 külg ")
    while a.replace(".","",1).isdigit()==False:
        a=input("Kirjuta õige külg ")
    b=input("Kirjuta 2 külg ")
    while b.replace(".","",1).isdigit()==False:
        b=input("Kirjuta õige külg ")
    if tegevus=="pindala":
        S=float(a)*float(b)
        print("Pindala on ", S)
    else:
        P=2*(float(a)+float(b))
        print("Perimeeter on ",P)
elif kujund=="kolmnurk":
    a=input("Kirjuta alus ")
    while a.replace(".","",1).isdigit()==False:
        a=input("Kirjuta õige alus ")
    if tegevus=="pindala":
        h=input("Kirjuta kõrgus ")
        while h.replace(".","",1).isdigit()==False:
                h=input("Kirjuta õige kõrgus ")
        S=(float(a)*float(h))/2
        print("Pindala on ", S)
    else:
        b=input("Kirjuta 2 külg ")
        while b.replace(".","",1).isdigit()==False:
            b=input("Kirjuta õige külg ")
        c=input("Kirjuta 3 külg ")
        if c.replace(".","",1).isdigit()==False:
            c=input("Kirjuta õige külg ")
        P=float(a)+float(b)+float(c)
        print("Perimeeter on ",P)
elif kujund=="rööpkülik":
    a=input("Kirjuta 1 külg ")
    while a.replace(".","",1).isdigit()==False:
        a=input("Kirjuta õige külg ")
    b=input("Kirjuta 2 külg ")
    while b.replace(".","",1).isdigit()==False:
        b=input("Kirjuta õige külg ")
    if tegevus=="pindala":
        S=float(a)*float(b)
        print("Pindala on ", S)
    else:
        P=2*(float(a)+float(b))
        print("Perimeeter on ",P)
else:
    r=input("Kirjuta raadius ")
    while r.replace(".","",1).isdigit()==False:
        r=input("Kirjuta õige raadius ")
    if tegevus=="pindala":
        S=pi*float(r)**2
        print("Pindala on ",S)
    else:
        C=pi*float(r)*25
        print("Perimeeter on ",C)

#Ü0 2
print()
print("Ülesanne 0 2")
print()
kujund=input("Vali kujund (ristkülik, rööpkülik, kolmnurk, ring) ").lower()
while True:
    if kujund not in ["ristkülik", "rööpkülik", "kolmnurk", "ring"]:
        kujund=input("Palun kirjutage õige kujund! ").lower()
    else:
        break
tegevus=input("Mis sa otsi? (pindala, perimeeter) ").lower()
while True:
    if tegevus not in ["pindala","perimeeter"]:
        tegevus=input("Palun kirjuta õige tegevus! ").lower()
    else:
        break
if kujund=="ristkülik":
    a=input("Kirjuta 1 külg ")
    while True:
        if a.replace(".","",1).isdigit()==False:
            a=input("Kirjuta õige külg ")
        else:
            break
    b=input("Kirjuta 2 külg ")
    while True:
        if b.replace(".","",1).isdigit()==False: # 1.5 => 15 
            b=input("Kirjuta õige külg ")
        else:
            break
    if tegevus=="pindala":
        S=float(a)*float(b)
        print("Pindala on ", S)
    else:
        P=2*(float(a)+float(b))
        print("Perimeeter on ",P)
elif kujund=="kolmnurk":
    a=input("Kirjuta alus ")
    while True:
        if a.replace(".","",1).isdigit()==False:
            a=input("Kirjuta õige alus ")
        else:
            break
    if tegevus=="pindala":
        h=input("Kirjuta kõrgus ")
        while True:
            if h.replace(".","",1).isdigit()==False:
                h=input("Kirjuta õige kõrgus ")
            else:
                break
        S=(float(a)*float(h))/2
        print("Pindala on ", S)
    else:
        b=input("Kirjuta 2 külg ")
        while True:
            if b.replace(".","",1).isdigit()==False:
                b=input("Kirjuta õige külg ")
            else:
                break
        c=input("Kirjuta 3 külg ")
        if c.replace(".","",1).isdigit()==False:
            c=input("Kirjuta õige külg ")
        P=float(a)+float(b)+float(c)
        print("Perimeeter on ",P)
elif kujund=="rööpkülik":
    a=input("Kirjuta 1 külg ")
    while True:
        if a.replace(".","",1).isdigit()==False:
            a=input("Kirjuta õige külg ")
        else:
            break
    b=input("Kirjuta 2 külg ")
    while True:
        if b.replace(".","",1).isdigit()==False:
            b=input("Kirjuta õige külg ")
        else:
            break
    if tegevus=="pindala":
        S=float(a)*float(b)
        print("Pindala on ", S)
    else:
        P=2*(float(a)+float(b))
        print("Perimeeter on ",P)
else:
    r=input("Kirjuta raadius ")
    while True:
        if r.replace(".","",1).isdigit()==False:
            r=input("Kirjuta õige raadius ")
        else:
            break
    if tegevus=="pindala":
        S=pi*float(r)**2
        print("Pindala on ",S)
    else:
        C=pi*float(r)*25
        print("Perimeeter on ",C)



#print("Ülesanne 10")
#x=1
#while True:
#    if x>100:
#        break
#    elif x%5==0:
#        print(x, end=" ")
#    x+=1
#
#print("Ülesanne 17 ")
#try:
    #num_horiz=int(input("Siseta ruutude arv horisontaalselt =>> \n"))
    #num_horiz=randint(1,20)
#except:
    #print("Value Error")
#try:
    #num_vert=int(input("Siseta ruutude arv vertikalselt =>> \n"))
    #num_vert=randint(1,20)
#except:
    #print("Value Error")
#for y in range (num_vert):
    #for x in range(num_vert)
        #print("das", end=" ")
    #print()
#
#print("Ülesanne 16 ")
#ans = randint(1, 10)
#while True:
#    g=input("mis numbri ma arvasin?(1-10, mängu lõpetamiseks kirjutage *lõpp* ) \n")
#    if g.lower() == "lõpp":
#        print("mängi on läbi!")
#        break
#    if not g.isnumeric():
#        print("Väle andmetüüp!")
#    g=int(g)
#    if g == ans:
#        print("Õige! sa arvasid ära!")
#        break
#    if g>10 or g<1:
#        print("Vahemik on vale")
#    elif g!=ans:
#        print("vale! proovi veel korra!")
#
#print("Ülesanne 3")
#try:
#    f = int(input("mitu algarvu sa tahad? "))
#    for d in range(0,f,1):
#        print("Ülesanne: ")
#        a = randint(1,50)
#        b = randint(1,50)
#        c = a + b 
#        for i in range (0,5,1):
#            answer = int(input(f"{a}+{b}=?"))
#            if answer == a+b:
#                print("See on õige")
#                break
#            else:
#                print("Proovi veel korra")
#                print()
#        print(f"õige on {c} ")
#except:
#    print("See ei ole õige")
#
#print("Ülesanne 3")
#print("arv", "   ruut ", "   kuup")
#for i in range(1, 11):
#    print(f" {i}      {i**2}      {i**3}")
#
#import string
#print("ülessane 0 STR")
#print("Guess letter (Aa-Zz)")
#letter = random.choice(string.ascii_letters)
#while True: 
#    answ=input("Your guess: ")
#    if letter== answ:
#        print("good job")
#        break
#    else:
#        print("Try again")
#print("22")
#n=1
#while True:
#    print("Tahan kommi!")
#    a=input().lower()
#    if a == "komm":
#        print("Äitah! oli vaja", n, " katse")
#        break
#    else:
#        n = n + 1
#print("Ülesanne 8")
#while 1:
#    try:
#        mainnumber = int(input("Vali number 1-100: "))
#        break
#    except ValueError:
#        print("Proovi veel korra")
#if mainnumber<1 or mainnumber>100:
#    print("Vali õige number")
#else:
#    paaris = 0
#    paaritu = 0
#    x = 0
#    while x != mainnumber:
#        x = x + 1
#        print(int(x), end= " ")
#        if x % 2 == 0:
#           paaris+=1
#        else:
#            paaritu += 1
#print("Paaris: ", paaris)
#print("Paaritu: ", paaritu)
#print("Ülesanne 11")
#n=randint(1,10)
#while True:
#    text=input("Sisetage number: ")
#    if text == "stopp":
#        print("Number oli", n)
#        break
#    elif int(text)==n:
#        print("sa võitsid")
#        break
#    else:
#        print("Proovi veel korra")
#        continue
#while True:
#    UserName=input("Login")
#    Password=input("Password")
#    if UserName=="Edvard" and Password=="123":
#        print("Korras")
#        print("sa võid tööle asuda")
#        break
#    else:
#        print("viga")
