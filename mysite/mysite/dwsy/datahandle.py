import sys
sys.path.append('/data/env/django_release/lib/python3.8/site-packages')
import numpy as np
#from /data/env/django_release/lib/python3.8/site-packages import numpy as np
#from data.env.django_release.lib.python3.8.site-packages import numpy as np
import math
import base64
Kp={'0.68':1,'0.95':1.96,'0.99':2.58}
t68={3:1.32,4:1.20,5:1.14,6:1.11,7:1.09,8:1.08,9:1.07,10:1.06,15:1.04,20:1.03}
t95={3:4.30,4:3.18,5:2.78,6:2.57,7:2.46,8:2.37,9:2.31,10:2.26,15:2.15,20:1.96}
t99={3:9.93,4:5.84,5:4.60,6:4.03,7:3.71,8:3.50,9:3.36,10:3.25,15:2.98,20:2.86}
tp={'0.68':t68,'0.95':t95,'0.99':t99}

def fit(data_x,data_y):
    print(sys.path)
    data_x=np.array(data_x)
    data_y=np.array(data_y)
    n=len(data_x)
    m_x=np.mean(data_x)
    m_y=np.mean(data_y)
    k=(sum(data_x*data_y)-n*m_x*m_y)/(sum(data_x*data_x)-n*m_x*m_x)
    b=m_y-k*m_x
    # x_max=max(data_x)
    # y_max=max(data_y)
    # plt.scatter(data_x,data_y)
    # y=k*data_x+b
    r=(sum(data_x*data_y)-n*m_x*m_y)/(math.sqrt((sum(data_x*data_x)-n*m_x*m_x)*(sum(data_y*data_y)-n*m_y*m_y)))
    return k,b

def std(x):
    x=np.array(x)
    m_x=np.mean(x)
    ret=math.sqrt(sum((x-m_x)*(x-m_x))/(len(x)-1))
    return ret

def mean(x):
    x=np.array(x)
    return np.mean(x)


def Uncertain(x,P,delta,C):
    x_std=std(x)
    ua=tp[P][len(x)]*x_std/(math.sqrt(len(x)))
    ub=Kp[P]*delta/C
    u=math.sqrt(ua*ua+ub*ub)
    return u
    
