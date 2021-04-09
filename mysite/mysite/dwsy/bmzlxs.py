from django.http import HttpResponse
from django.shortcuts import render
from mysite.dwsy.datahandle import fit,mean,std,Uncertain
import math
def form(requests):
    return render(requests,'bmzlxs.html')
def handle(requests):
    requests.encoding='utf-8'
    try:
        ret={}
        data=requests.GET
        m=data['m']
        m=m.split(' ')
        for i in range(len(m)):
            m[i]=float(m[i])
        X=data['X']
        X = X.split(' ')
        for i in range(len(X)):
            X[i] = float(X[i])
        k,b=fit(X,m)
        if b>=0:
            ret['k_equa']='最小二乘法拟合的方程为:y=%fx+%f'%(k,b)+',其中劲度系数k=%fN/m'%k
        else:
            ret['k_equa']='最小二乘法拟合的方程为:y=%fx%f'%(k,b)+',其中劲度系数k=%fN/m'%k
        d=data['d']
        d=d.split(' ')
        for i in range(len(d)):
            d[i]=float(d[i])
        d_m=mean(d)
        d_std=std(d)
        ret['d_t']='d的均值:%fcm  ,  d的标准差:%fcm'%(d_m,d_std)
        l0s=data['l0s']
        l0s=float(l0s)
        ls=data['ls']
        ls=ls.split(' ')
        for i in range(len(ls)):
            ls[i]=float(ls[i])
        ls_m=mean(ls)
        ls_std=std(ls)
        ret['ls_t']='l的均值:%fcm  ,  l的标准差:%fcm'%(ls_m,ls_std)
        P=data['P']
        ud=Uncertain(d,P,0.01,3)
        uls=Uncertain(ls,P,0.001,math.sqrt(3))
        if data['tool']=='quan':
            o = k * (ls_m - l0s) / (2 * 3.14 * d_m)
        elif data['tool']=='si':
            o=k*(ls_m-l0s)/(2*d_m)
        else: 
            return render(requests,'bmzlxsres.html',{'k_equa':'请选择金属丝或圈'})
        u=o*math.sqrt(ud*ud/(d_m)+uls*uls/(ls_m-l0s))
        ret['d_uncertain']='d的展伸不确定度u(d)=%fcm'%ud+',P='+P
        ret['l_uncertain']='l的展伸不确定度u(l)=%fcm'%uls+',P='+P
        ret['o_uncertain']='表面张力系数不确定度u(o)=%fN/m'%u+',P='+P
        ret['o_t']='表面张力系数o=%f±%fN/m'%(o,u)+',P='+P
        return render(requests,'bmzlxsres.html',ret)
    except:
        return render(requests,'bmzlxsres.html',{'k_equa':'好像有地方错了,检查一遍'})
def result(requests):
    return render(requests,'bmzlxsres.html')
