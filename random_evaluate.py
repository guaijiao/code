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
        self.dip=[dip,]
        self.dip_count=1
        self.eval=''
        self.dev=0
    def dip_append(self,dip): 
        self.dip.append(dip) 
        self.dip_count+=1 
    def add_eval(self,evaluate):  
        self.eval=evaluate
    def add_dev(self,deviation):
        self.dev=deviation
def min_max(min=0,max=1):
    


def random_evaluate(fileout,begin,end):
    flst= filelst.getRequestFileLst(begin,end)
    for lst in flst:
        f1in=open('../Data/'+lst,'r')
        sip ={}
        i=0
        for line in f1in:
            row = line.strip().split()
            if not row[0] in sip:
                sip[row[0]]=sip_sport(row[0],row[1])
                i+=1
            else:
                sip[row[0]].sport_append(row[1])            
        f1in.close()

        for ip in sip:
            l=[]
            for port in sip[ip].port:
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
        ssip=sorted(sip.iteritems(),key=lambda d:d[1].dev)
        fout = open(fileout,'a')
        for ip in ssip:
            fout.write(ip[0]+' '+str(ip[1].dev)+' '+ip[1].eval+'\n')

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
            while(len(row)==8):
                if not row[0] in sip:
                    sip[row[0]]=sip_dip(row[0],row[2])
                    sip_q[row[0]]=1
                    sip_count+=1
                else:
                    sip[row[0]].dip_append(row[2])
                    sip_q[row[0]]+=1
        f1in.close()

    for ip in sip:
        fout = open(fileout,'a')
        for ip in sip:
            r=sip_q[ip]/sip[ip].dip_count
            fout.write(ip+' '+str(r)+'\n')
        fout.close()
if __name__ == '__main__':
    # random_evaluate('haha','2015112219','2015112223')
    sipquery_dip_rate('hahah','2015112219','2015112223')