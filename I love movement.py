import subprocess
import time
from VALID import ns, OK, OKI

def orden(n):
    while True:
        n=input("¿Qué orden, di o id?: ")
        if n==("id") or n==("di"):
            break
    if n==("di"):
        orde=(r,p,m,l,k,j,o,h,g,f,e,d,c,b,a)
    else:
        orde=(a,b,c,d,e,f,g,h,o,j,k,l,m,p,r)
    return orde

while True:
    numero=OKI(input("Inserta número: "))
    
    MODE=ns(input("¿VER DEMO?: "))
    if MODE==("s"):
        a=(" **************")
        b=("* *************")
        c=("** ************")
        d=("*** ***********")
        e=("**** **********")
        f=("***** *********")
        g=("****** ********")
        h=("******* *******")
        o=("******** ******")
        j=("********* *****")
        k=("********** ****")
        l=("*********** ***")
        m=("************ **")
        p=("************* *")
        r=("************** ")
        rect=("---------------")
        ORDEN=orden(input("¿Qué orden, di o id?: "))
        for i in range(0,numero):
            for i in(ORDEN):
                print("I LOVE MOVEMENT")
                print(i)
                print(rect)
                print(i)
                print(rect)
                time.sleep(0.08)
                subprocess.call(["cmd.exe","/C","cls"])


    else:
        subprocess.call(["cmd.exe","/C","cls"])
        n=numero
        while n>0:
            print("ESTE PROGRAMA SE AUTODESTRUIRÁ EN:")
            print(chr(7),n)
            n-=1
            time.sleep(1)
            subprocess.call(["cmd.exe","/C","cls"])
        print("¡BOOOOOM!")
        time.sleep(3)
    conti=ns(input("¿Dispone de más tiempo que perder?: "))
    if conti==("n"):
        break

