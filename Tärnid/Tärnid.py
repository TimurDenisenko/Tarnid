from math import *

#Ü6
print()
print("Ülesanne 6")
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

x=0
while x<5:
    print("* "*5)
    x+=1
x=0
print()
while x<10:
    print("* "*x)
    x+=1
x=11
print()
while x>0:
    print("* "*(x-1))
    x-=1

#Ü0
print()
print("Ülesanne 0")
print()
while True:
    kujund=input("Vali kujund (ristkülik, rööpkülik, kolmnurk, ring) ").lower()
    if kujund not in ["ristkülik", "rööpkülik", "kolmnurk", "ring"]:
        print("Palun kirjutage õige kujund!")
    else:
        while True:
            tegevus=input("Mis sa otsi? (pindala, perimeeter) ").lower()
            if tegevus not in ["pindala","perimeeter"]:
                print("Palun kirjuta õige tegevus! ")
            else:
                break
        break
if kujund=="ristkülik":
    if tegevus=="pindala":
        while True:
            a=input("Kirjuta 1 külg ")
            if a.replace(".","",1).isdigit()==False:
                print("Kirjuta õige külg ")
                continue
            while True:
                b=input("Kirjuta 2 külg ")
                if b.replace(".","",1).isdigit()==False:
                    print("Kirjuta õige külg ")
                    continue
                break
            S=float(a)*float(b)
            print("Pindala on ", S)
    else:
        while True:
            a=input("Kirjuta 1 külg ")
            if a.replace(".","",1).isdigit()==False:
                print("Kirjuta õige külg ")
                continue
            while True:
                b=input("Kirjuta 2 külg ")
                if b.replace(".","",1).isdigit()==False:
                    print("Kirjuta õige külg ")
                    continue
                break
            P=2*(float(a)+float(b))
            print("Perimeeter on ",P)
elif kujund=="kolmnurk":
    if tegevus=="pindala":
        while True:
            a=input("Kirjuta alus ")
            if a.replace(".","",1).isdigit()==False:
                print("Kirjuta õige alus ")
                continue
            while True:
                h=input("Kirjuta kõrgus ")
                if h.replace(".","",1).isdigit()==False:
                        print("Kirjuta õige kõrgus ")
                        continue
                break
            S=(float(a)*float(h))/2
            print("Pindala on ", S)
    else:
        while True:
            a=input("Kirjuta 1 külg ")
            if a.replace(".","",1).isdigit()==False:
                print("Kirjuta õige külg ")
                continue
            while True:
                b=input("Kirjuta 2 külg ")
                if b.replace(".","",1).isdigit()==False:
                    print("Kirjuta õige külg ")
                    continue
                while True:
                    c=input("Kirjuta 3 külg ")
                    if c.replace(".","",1).isdigit()==False:
                        print("Kirjuta õige külg ") 
                        continue
                    break
                break
            P=float(a)+float(b)+float(c)
            print("Perimeeter on ",P)
elif kujund=="rööpkülik":
    if tegevus=="pindala":
        while True:
            a=input("Kirjuta 1 külg ")
            if a.replace(".","",1).isdigit()==False:
                print("Kirjuta õige külg ")
                continue
            while True:
                b=input("Kirjuta 2 külg ")
                if b.replace(".","",1).isdigit()==False:
                    print("Kirjuta õige külg ")
                    continue
                break
            S=float(a)*float(b)
            print("Pindala on ", S)
    else:
        while True:
            a=input("Kirjuta 1 külg ")
            if a.replace(".","",1).isdigit()==False:
                print("Kirjuta õige külg ")
                continue
            while True:
                b=input("Kirjuta 2 külg ")
                if b.replace(".","",1).isdigit()==False:
                    print("Kirjuta õige külg ")
                    continue
                break
            P=2*(float(a)+float(b))
            print("Perimeeter on ",P)
else:
    if tegevus=="pindala":
        while True:
            r=input("Kirjuta raadius ")
            if r.replace(".","",1).isdigit()==False:
                print("Kirjuta õige raadius ")
                continue
            else:
                S=pi*float(r)**2
                print("Pindala on ", S)
            break
    else:
        while True:
            r=input("Kirjuta raadius ")
            if r.replace(".","",1).isdigit()==False:
                print("Kirjuta õige raadius ")
                continue
            else:
                C=pi*float(r)*25
                print("Perimeeter on ",C)
            break


#print("Ülesanne 10")
#x=1
#while True:
#    if x>100:
#        break
#    elif x%5==0:
#        print(x, end=" ")
#    x+=1

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