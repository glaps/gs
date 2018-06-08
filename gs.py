#!/bin/python
import random, sys

if "-n" and "-i" in sys.argv[1:]:
    n,i = int(sys.argv[2]), int(sys.argv[4])
else:
    print("no args -n and -i")
    sys.exit()

con = 0

class mashin:
    count = 0
    def __init__(self,msg):
        self.msg = msg
        self.flag = False
    def chek(self):
        if self.msg and not self.flag:
            self.flag=True
            self.__class__.count+=1
            return ran()
        else:
            return "get"

def exams():
    nams = [f'a{y}' for y in range(n)]
    obj = {i:None for i in nams}
    return nams, obj

def ran():
    return [random.randrange(0,n) for _ in range(4)]

def fun(r,f=None, con=0):
    msg = "alina"
    if con > n/2:
        con+=1
        if f:
            obj[nams[r]] = mashin(msg)
            fun(obj[nams[r]].chek())
        elif r:
            for y in r:
                obj[nams[y]] = mashin(msg)
            fun(obj[nams[r[0]]].chek()),fun(obj[nams[r[1]]].chek()), fun(obj[nams[r[2]]].chek()),fun(obj[nams[r[0]]].chek())
def counter(obj):
    coun = 0
    for i in obj:
        try:
            if obj[i].flag or not obj[i].flag:
                print(i,obj[i])
                coun+=1
        except: pass
    return coun
ren = 0
while i:
    nams, obj = exams()
    fun(random.randrange(0, n), f=True)
    counter(obj)
    ren = counter(obj)
    i-=1
print("in {}% cases all nodes received the packet".format(ren/n))











