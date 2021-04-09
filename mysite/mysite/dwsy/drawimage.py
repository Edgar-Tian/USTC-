import sys
sys.path.append('/data/env/django_release/lib/python3.8/site-packages')
from mysite.dwsy import datahandle
import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.shortcuts import render
import os
import base64
from io import BytesIO
import numpy as np
def input_form(requests):
    return render(requests,'drawimage.html')
def recv(r):
    r=r.split(" ")
    for i in range(len(r)):
        r[i]=float(r[i])
    return r
def draw_image(requests):
    requests.encoding = 'utf-8'
    data=requests.GET
    if True:
        x=recv(data['x'])
        y=recv(data['y'])
        xlabel=data['xlabel']
        ylabel=data['ylabel']
        k,b=datahandle.fit(x,y)
        y=np.array(y)
        x=np.array(x)
        y_axis=k*x+b
        plt.scatter(x,y,c='#000000')
        plt.plot(x,y_axis,'#000000')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        buffer=BytesIO()
        plt.savefig(buffer)
        plot_data=buffer.getvalue()
        imb=base64.b64encode(plot_data)
        ims=imb.decode()
        imd="data:image/png;base64,"+ims
        context={}
        context['img']=imd
        if b>=0:
            context['equa']='直线方程:y=%fx+%f'%(k,b)
        else:
            context['equa']='直线方查:y=%fx%f'%(k,b)
        return render(requests,'drawimageres.html',context)
#    except:
#        return HttpResponse('貌似出现了错误')
def result(requests):
    return render(requests,'drawimageres.html')
