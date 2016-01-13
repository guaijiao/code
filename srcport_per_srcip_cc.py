from __future__ import division
import os
import string
import numpy
import math
import filelst
import time



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

def random_evaluate(fileout):
    sip ={}
    j=1
    f1in=open('../Data/srcport_per_srcip','r')
    for line in f1in:
        row = line.strip().split("\t")
        if len(row)==3:
            if len(sip)==0:
                sip[row[0]]=sip_sport(row[0],row[1])
                for i in range(int(row[2])-1):
                    sip[row[0]].sport_append(row[1])
            elif row[0] in sip:
                for x in range(int(row[2])):
                    sip[row[0]].sport_append(row[1])

            else :           
        

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
                    if 3980<=dev:
                        sip[ip].add_eval('great')
                    elif 296<=dev and dev<3980:
                        sip[ip].add_eval('good')
                    elif 0<=dev and dev<296:
                        sip[ip].add_eval('poor')   

                # ssip=sorted(sip.iteritems(),key=lambda d:d[1].dev)
                fout = open(fileout,'a')
                for ip in sip:
                    fout.write(ip+' '+str(sip[ip].dev)+' '+sip[ip].eval+'\n')
                fout.close()
                sip.clear()
                sip[row[0]]=sip_sport(row[0],row[1])
                for i in range(int(row[2])-1):
                    sip[row[0]].sport_append(row[1])
                print '..........................................'+str(j)+'\n'
                print line

                j+=1

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
        if 3980<=dev:
            sip[ip].add_eval('great')
        elif 296<=dev and dev<3980:
            sip[ip].add_eval('good')
        elif 0<=dev and dev<296:
            sip[ip].add_eval('poor')   

    # ssip=sorted(sip.iteritems(),key=lambda d:d[1].dev)
    fout = open(fileout,'a')
    for ip in sip:
        fout.write(ip+' '+str(sip[ip].dev)+' '+sip[ip].eval+'\n')
    fout.close()
    sip.clear()
    print '..........................................'+str(j)+'\n'
    print line

    j+=1
    f1in.close()
if __name__ == '__main__':
    random_evaluate('3')