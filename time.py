#encoding:utf-8

import datetime
def subtime(t1,t2):
    lst =[]
    time1 = str(t1)
    time2 = str(t2)
    bY = str(time1[0:4])
    eY = str(time2[0:4])
    bM = str(time1[4:6])
    eM = str(time2[4:6])
    bD = str(time1[6:8])
    eD = str(time2[6:8])
    bH = str(time1[8:10])
    eH = str(time2[8:10])
    time1 =bY+'-'+bM+'-'+bD+' '+bH
    time2 =eY+'-'+eM+'-'+eD+' '+eH
    date1=datetime.datetime.strptime(time1,'%Y-%m-%d %H')
    date2=datetime.datetime.strptime(time2,'%Y-%m-%d %H')
    i=datetime.timedelta(hours=1)
    while i<(date2-date1):
        lst.append((date1+i).strftime('%Y%m%d%H'))
        i+=datetime.timedelta(hours=1)
    return lst

lst = subtime(2015111819,2015113016)
print lst

