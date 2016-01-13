from __future__ import division
import os
import string
import numpy
import math
import filelst



class sip_sport:
    def __init__(self,sip,sport):
        self.sip=[sip,]
        self.sport=[sport,]
        self.count=1
        self.eval=''
        self.dev=0
    def sport_append(self,sport): 
        self.sport.append(sport) 
        self.count+=1 
    def add_eval(self,evaluate):  
        self.eval=evaluate 
    def add_dev(self,deviation):
        self.dev=deviation
class sip_dip:
    def __init__(self,sip,dip):
        self.sip=[sip,]
        self.dip=set([dip,])
        self.dip_count=1
        self.eval=''
        self.dev=0
    def dip_append(self,dip): 
        self.dip.add(dip) 
        self.dip_count+=1 


def min_max(fileout,filein):
    flin=open(filein,'r')
    m=[]
    ma=[]
    mi=[]
    for i in range(0,6):
        ma.append(float('-inf'))
        mi.append(float('inf'))
    for line in flin:
        row = line.strip().split()
        for i in range(1,4):
            if float(row[i])< mi[i]:
                mi[i]=float(row[i])
            if float(row[i])>ma[i]:
                ma[i]=float(row[i])
    flin.close()
    flin=open(filein,'r')
    flout=open(fileout,'a')
    m.append(0)
    for i in range(1,6):
        m.append(ma[i]-mi[i])
    for line in flin:
        row = line.strip().split()
        flout.write(row[0])
        for i in range(1,4):
            mm=(float(row[i])-mi[i])/m[i]
            flout.write(' '+str(mm))
        flout.write(' '+row[4]+'\n')
    flout.close()
                      


    


def random_evaluate(fileout,begin,end):
    flst= filelst.getRequestFileLst(begin,end)
    sip ={}
    for lst in flst:
        f1in=open('../Data/'+lst,'r')
        for line in f1in:
            row = line.strip().split()
            if len(row)==8:
                if not row[0] in sip:
                    sip[row[0]]=sip_sport(row[0],row[1])
                else:
                    sip[row[0]].sport_append(row[1])           
        f1in.close()

    for ip in sip:
        l=[]
        for port in sip[ip].sport:
            l.append(float(port))
        narray=numpy.array(l)
        sum1=narray.sum()
        narray2=narray*narray
        sum2=narray2.sum()
        mean=sum1/len(l)
        var=sum2/len(l)-mean**2
        dev=math.sqrt(var)
        sip[ip].add_dev(dev)
        if 3980<=dev and dev<=20000:
            sip[ip].add_eval('great')
        elif 296<=dev and dev<3980:
            sip[ip].add_eval('good')
        elif 0<=dev and dev<296:
            sip[ip].add_eval('poor')
        else:
            sip[ip].add_eval('warning')
    # ssip=sorted(sip.iteritems(),key=lambda d:d[1].dev)
    fout = open(fileout,'a')
    for ip in sip:
        fout.write(ip+' '+str(sip[ip].dev)+' '+sip[ip].eval+'\n')
    fout.close()
def sipquery_dip_rate(fileout,begin,end):
    flst= filelst.getRequestFileLst(begin,end)
    sip ={}
    sip_count=0
    sip_q={}
    for lst in flst:
        f1in=open('../Data/'+lst,'r') 
        for line in f1in:
            row = line.strip().split()              
            if len(row)==8:
                if not row[0] in sip:
                    sip[row[0]]=sip_dip(row[0],row[2])
                    sip_q[row[0]]=1
                    sip_count+=1
                else:
                    sip[row[0]].dip_append(row[2])
                    sip_q[row[0]]+=1
        f1in.close()
    fout = open(fileout,'a')   
    for ip in sip:
        c=len(sip[ip].dip)
        r=sip[ip].dip_count/c
        fout.write(ip+' '+str(sip[ip].dip_count)+' '+str(r)+'\n')
    fout.close()
def merge(fileout,f1,f2):
    f1in=open(f1,'r')  
    f2in=open(f2,'r')  
    fout=open(fileout,'a')
    l=[]
    i=0
    for line in f1in:
        row = line.strip().split()
        l.append([]) 
        for m in range(1,len(row)):
            l[i].append(row[m])
        i+=1
    f1in.close()
    i=0    
    for line in f2in:
       row = line.strip().split() 
       l[i]=row+l[i]
       i+=1
    f2in.close()
    for j in range(i):
        for k in range(len(l[j])):
            fout.write(l[j][k]+' ')
        fout.write('\n')  
    fout.close()                


def cc(fileout,begin,end='0'):
    if end=='0'and float(begin)%100==0 :
        end=str(float(begin)+23)
    elif end=='0'and float(begin)%100!=0:
        end=str(float(begin)+99)
    else:
        pass    
    random_evaluate('ha',begin,end)
    sipquery_dip_rate('haha',begin,end)
    merge('hahaha','ha','haha')
    min_max(fileout,'hahaha')
    

if __name__ == '__main__':
    #random_evaluate('ha','2015112219','2015112223')
    #sipquery_dip_rate('haha','2015112219','2015112223')
    #merge('hahaha','ha','haha')
    #min_max('ccc','hahaha')
    cc('cc','2015112301','2015112400')