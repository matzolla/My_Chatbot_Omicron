#from goto import with_goto
import os
import sys
import scenario
#def goto(linenum):
#    global line
#    line= linenum
def relaunch():
    args=""
    for i in sys.argv:
        args=args+" "+str(i)
    #print "python"+args
    os.system("python"+ args)

a=input('entrer un text')
k=[]
s=[]
def xeleph():
    if a=="y":
        k.append(a)
        c=input("encore")
    #print(k
    if c=="b":
        r=input("c'est bon")
        k.append(c)
        s.append(c)
        if r=='p':
            x,y=scenario.facteur_pronostique(k)

#testing
#a=['bonjour','bonsoir','ok','diagnostic','epsilon','optimus']
#b=['bonjour','ok']

#i in a for i in b
#print(any(i in a for i in b))

#x,y=facteur_pronostique(a,b)
#print(x)
#print("taux: {},\nfacteur_pronostique_majeur: {}".format(y,x))
