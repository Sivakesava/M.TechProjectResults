#dt=1e-3,NORMAL REFINEMENT NORMS WITH EXACT INTEGRATION
import numpy
from numpy import matrix,array
import math
########log( L2_Norma)
L2_1=array([-0.42652492, -0.88049173, -1.25444867, -1.5298765 , -1.74163667, -1.91191911])
L2_2=array([-0.31987205, -0.99371161, -1.36518563, -1.75108068, -2.02936888, -2.26277648])
L2_4=array([-0.11652145, -0.90988648, -2.16827611, -2.64067899, -3.14964634])
L2_8=array([-0.19727749, -0.84096067, -2.1229141 , -2.77643564, -3.66284482, -3.99338852])
L2_16=array([-0.89135144, -3.19113269, -4.28694165])

########log( NOP )
Nop_1=array([ 2.40823997,  3.01029996,  3.36248247,  3.61235995,  3.80617997, 3.96454247])
Nop_2=array([ 2.15836249,  2.76042248,  3.112605  ,  3.36248247,  3.5563025 , 3.71466499])
Nop_4=array([ 2.        ,  2.60205999,  3.20411998,  3.39794001,  3.5563025 ])
Nop_8=array([ 1.90848502,  2.51054501,  2.86272753,  3.112605  ,  3.30642503,3.46478752])
Nop_16=array([ 2.46089784,  3.06295783,  3.41514035])

########WCT
WCT_1=array([  23.20324993,   91.170959  ,  206.89692497,  367.7253449 , 574.430053  ,  834.73116302])
for i in range(6):
    WCT_1[i]=math.log10(WCT_1[i])
WCT_2=array([   7.86905408,   30.50925612,   66.5066781 ,  114.79564404, 181.21402287,  258.88675594])
for i in range(6):
    WCT_2[i]=math.log10(WCT_2[i])
WCT_4=array([  3.94770408,  11.97381902,  44.25191689,  68.75628686,  97.01135206])
for i in range(5):
   WCT_4[i]=math.log10(WCT_4[i])
WCT_8=array([  4.90037704,   8.59861684,  14.68995905,  23.28215194, 34.21295285,  47.7324791 ])
for i in range(6):
    WCT_8[i]=math.log10(WCT_8[i])
WCT_16=array([ 17.74432802,  27.45050812,  43.54876995])
for i in range(3):
   WCT_16[i]=math.log10(WCT_16[i])

print 'dt=1e-3'
import pylab as py

#########PLOTS
'''L2_1plot=py.plot(10**Nop_1,L2_1,'rD-')
L2_2plot=py.plot(10**Nop_2,L2_2,'b*-')
L2_4plot=py.plot(10**Nop_4,L2_4,'go-')
L2_8plot=py.plot(10**Nop_8,L2_8,'k>-')
L2_16plot=py.plot(10**Nop_16,L2_16,'ms-')
py.legend(('N=1','N=2','N=4','N=8','N=16'),loc=1)
'''
L2_1plot=py.plot(Nop_1,L2_1,'rD-')
L2_2plot=py.plot(Nop_2,L2_2,'b*-')
L2_4plot=py.plot(Nop_4,L2_4,'go-')
L2_8plot=py.plot(Nop_8,L2_8,'k>-')
L2_16plot=py.plot(Nop_16,L2_16,'ms-')
py.legend(('N=1','N=2','N=4','N=8','N=16'),loc=3)
py.title('Exact Integration')
py.xlabel('log(Nop)')
py.ylabel('log(L2)')

py.show()
#L2_8plot=py.plot(Nop_8,L2_8,color='k')
#L2_16plot=py.plot(Nop_16,L2_16,color='m')
WCT_1plot=py.plot(WCT_1,L2_1,'rD-')
WCT_2plot=py.plot(WCT_2,L2_2,'b*-')
WCT_4plot=py.plot(WCT_4,L2_4,'go-')
WCT_8plot=py.plot(WCT_8,L2_8,'k>-')
WCT_16plot=py.plot(WCT_16,L2_16,'ms-')
py.legend(('N=1','N=2','N=4','N=8','N=16'),loc=3)
'''
WCT_1plot=py.plot(10**WCT_1,L2_1,'rD-')
WCT_2plot=py.plot(10**WCT_2,L2_2,'b*-')
WCT_4plot=py.plot(10**WCT_4,L2_4,'go-')
WCT_8plot=py.plot(10**WCT_8,L2_8,'k>-')
WCT_16plot=py.plot(10**WCT_16,L2_16,'ms-')
py.legend(('N=1','N=2','N=4','N=8','N=16'),loc=1)'''
py.title('Exact Integration')
py.xlabel('log(WCT)')
py.ylabel('log(L2)')
py.show()
